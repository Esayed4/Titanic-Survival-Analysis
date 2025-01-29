# Import the necessary library for connecting to SQL Server
import pypyodbc as odbc
# Import necessary libraries for data manipulation and download
import pandas as pd
import gdown
import zipfile

# Define constants for the database connection
DRIVER_NAME = 'ODBC Driver 17 for SQL Server'  # Ensure this is correct
SERVER_NAME = 'DESKTOP-Q2DO090'  # Your computer name
DATABASE_NAME = 'Titanic'
USERNAME = 'Esayed'  # Your SQL Server username
PASSWORD = '154b20*Azhar'  # Your SQL Server password

# Construct the connection string for SQL Server Authentication
conn_str = f"""DRIVER={{{DRIVER_NAME}}};\
                SERVER={{{SERVER_NAME}}}; \
                DATABASE={{{DATABASE_NAME}}}; \
                UID={USERNAME}; \
                PWD={PASSWORD};"""  # Include username and password

# Attempt to connect to the database
try:
    conn = odbc.connect(conn_str)
    print("Connected to SQL Server")
except Exception as e:
    print("Error connecting to SQL Server:", e)



# Google Drive file ID for downloading the Titanic dataset
file_id = '1A2_DHJIXQKQH0-DgG6_ewNVE7rMNoiO-'
url = f'https://drive.google.com/uc?id={file_id}'

# Specify the output filename for the downloaded ZIP file
output = 'titanic.zip'
# Download the ZIP file from Google Drive (commented out)
# gdown.download(url, output)

# Define the path where the extracted files will be saved
saved_path = 'D:/Esayed/data_engineering/projects/data_analyst/titanic/titanic_files'

# Initialize paths for train, test, and gender submission files
train_file_path = saved_path + '/'
test_file_path = saved_path + '/'
gender_submission_file_path = saved_path + '/'

# Open the ZIP file and list its contents
with zipfile.ZipFile(output, 'r') as zip_ref:
    # List all the contents of the zip file
    file_names = zip_ref.namelist()
    print(file_names)

    # Update file paths based on the contents of the ZIP file
    train_file_path = train_file_path + file_names[2]
    test_file_path = test_file_path + file_names[1]
    gender_submission_file_path = gender_submission_file_path + file_names[0]

    # Extract all the contents to a directory
    zip_ref.extractall(saved_path)

# Read each file into a pandas DataFrame
train_df = pd.read_csv(train_file_path)
test_df = pd.read_csv(test_file_path)
gender_submission_df = pd.read_csv(gender_submission_file_path)

# Adjust PassengerId to be a string in each DataFrame
train_df['PassengerId'] = train_df['PassengerId'].astype(str)
test_df['PassengerId'] = test_df['PassengerId'].astype(str)
gender_submission_df['PassengerId'] = gender_submission_df['PassengerId'].astype(str)

# Function to insert data into SQL Server tables
def insert_data(table_name, df, conn):
    # Get the column names from the DataFrame
    columns_name = list(df.columns)
    
    # Create placeholders for the SQL query
    placeholders = ', '.join(['?'] * len(columns_name))
    
    # Construct the INSERT SQL query
    insert_sql = f"INSERT INTO {table_name} ({', '.join(columns_name)}) VALUES ({placeholders})"

    try:
        # Create a cursor object to execute SQL queries
        cursor = conn.cursor()
        
        # Iterate over each row in the DataFrame
        for _, row in df.iterrows():
            data_to_insert = []
            
            # Iterate over each column in the row
            for column in columns_name:
                # Check if the value is NaN
                if pd.isna(row[column]):
                    # Append an empty string for NaN values
                    data_to_insert.append('')
                else:
                    # Append the actual value
                    data_to_insert.append(row[column])
            
            # Convert the list to a tuple for insertion
            data_to_insert = tuple(data_to_insert)

            # Execute the INSERT query
            cursor.execute(insert_sql, data_to_insert)
            # Commit the changes
            conn.commit()
            print("Data inserted successfully.")
    except Exception as e:
        print("Error inserting data:", e)
    finally:
        # Close the cursor object
        cursor.close()

# Insert data into the respective tables
insert_data('Test', test_df, conn)
insert_data('Train', train_df, conn)
insert_data('Gender_submission', gender_submission_df, conn)

# Ensure to close the connection when done
if 'conn' in locals():
    conn.close()
