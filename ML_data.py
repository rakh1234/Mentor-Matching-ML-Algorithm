import pyodbc
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def connect_to_database():
    connection_string = 'DRIVER=DRIVER;SERVER=SERVER;DATABASE=DATABASE;UID=UID;PWD=PWD'

    try:
        connection = pyodbc.connect(connection_string)
        print("Connection successful!")
        return connection
    except pyodbc.Error as e:
        print("Error connecting to the database:", e)
        return None

def fetch_data():
    connection = connect_to_database()

    if connection is None:
        return None

    cursor = connection.cursor()

    query = '''
    SELECT UserID, Name, Email, Phone, UserType, Interests, Experience
    FROM Users
    WHERE UserType IN ('Mentor', 'BusinessInterest')
    '''
    cursor.execute(query)
    data = cursor.fetchall()

    connection.close()

    columns = [column[0].lower() for column in cursor.description]
    data_dicts = [dict(zip(columns, row)) for row in data]

    df = pd.DataFrame(data_dicts)

    return df

data_df = fetch_data()

if 'interests' not in data_df.columns or 'experience' not in data_df.columns:
    raise ValueError("The columns 'Interests' and/or 'Experience' do not exist in the dataframe.")

# Preprocess the text data using TfidfVectorizer
tfidf = TfidfVectorizer()
# Handling missing values
combined_text = data_df['interests'].fillna('') + ' ' + data_df['experience'].fillna('')
tfidf_matrix = tfidf.fit_transform(combined_text)

# Calculate cosine similarity considering both user and mentor profiles
similarity_matrix = cosine_similarity(tfidf_matrix)

# Find the top suitable mentor for each user considering user-specific interests
for i in range(len(data_df)):
    user_id = data_df.loc[i, 'userid']

    if data_df.loc[i, 'usertype'] == 'Mentor':
        continue  # Skip mentors in the user list

    # Calculate cosine similarity considering both user and mentor profiles
    similarity_scores = cosine_similarity(tfidf_matrix[i], tfidf_matrix).ravel()
    
    # Set similarity scores of non-mentors to -1 to filter them out
    similarity_scores[data_df[data_df['usertype'] != 'Mentor'].index] = -1
    mentor_indices = similarity_scores.argsort()[::-1][:6]

    print(f"Top mentors for user {user_id} ({data_df.loc[i, 'name']}):")
    for idx in mentor_indices:
        mentor_name = data_df.loc[idx, 'name']
        print(mentor_name)

    print()
