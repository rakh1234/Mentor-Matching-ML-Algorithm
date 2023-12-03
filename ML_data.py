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

    # Convert the fetched data to a list of dictionaries with the expected column names
    columns = [column[0].lower() for column in cursor.description]
    data_dicts = [dict(zip(columns, row)) for row in data]

    # Create a pandas dataframe from the list of dictionaries
    df = pd.DataFrame(data_dicts)

    return df

# Fetch user and mentor data from the database
data_df = fetch_data()

# Check if 'Interests' and 'Experience' columns exist
if 'interests' not in data_df.columns or 'experience' not in data_df.columns:
    raise ValueError("The columns 'Interests' and/or 'Experience' do not exist in the dataframe.")

# Preprocess the text data using TfidfVectorizer
tfidf = TfidfVectorizer()
# Concatenate 'Interests' and 'Experience' columns, handling missing values
combined_text = data_df['interests'].fillna('') + ' ' + data_df['experience'].fillna('')
tfidf_matrix = tfidf.fit_transform(combined_text)

# Calculate cosine similarity between user and mentor profiles
similarity_matrix = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Find the top suitable mentor for each user
top_mentors = []
for i in range(len(data_df)):
    user_id = data_df.loc[i, 'userid']

    if data_df.loc[i, 'usertype'] == 'Mentor':
        continue  # Exclude mentors from being matched

    similarity_row = similarity_matrix[i].copy()

    # Exclude the user from the similarity calculation
    similarity_row[i] = 0

    mentor_id = data_df.loc[similarity_row.argmax(), 'userid']
    mentor_name = data_df.loc[data_df['userid'] == mentor_id, 'name'].values[0]

    top_mentors.append((data_df.loc[i, 'name'], mentor_name))

for user_name, mentor_name in top_mentors:
    print(f"{user_name} -> {mentor_name}")
