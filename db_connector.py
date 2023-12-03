import pyodbc

def connect_to_database():
    # Replace the connection string with your database details
    connection_string = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost,1433;DATABASE=rocketerDB;UID=SA;PWD=Sha_@2030'

    try:
        connection = pyodbc.connect(connection_string)
        print("Connection successful!")
        return connection
    except pyodbc.Error as e:
        print("Error connecting to the database:", e)
        return None
    

def fetch_user_data():
    connection = connect_to_database()

    if connection is None:
        return None

    cursor = connection.cursor()

    # Example query to fetch all rows from User_info table
    query = "SELECT * FROM Users WHERE UserType ='BusinessInterest'"
    cursor.execute(query)
    user_data = cursor.fetchall()

    connection.close()

    return user_data



# Call the function to fetch user data
result = fetch_user_data()

if result is not None:
    # Print the fetched data
    for row in result:
        print("User data:", row)
else:
    print("No user data found in the table.")
    
   ############################################# 
    
def fetch_mentor_data():
    connection = connect_to_database()

    if connection is None:
        return None

    cursor = connection.cursor()

    # Example query to fetch all rows from User_info table
    query = "SELECT * FROM Users WHERE UserType ='Mentor'"
    cursor.execute(query)
    user_data = cursor.fetchall()

    connection.close()

    return user_data


# Call the function to fetch user data
result = fetch_mentor_data()

if result is not None:
    # Print the fetched data
    for row in result:
        print("Mentor data:", row)
else:
    print("No user mentor found in the table.")
