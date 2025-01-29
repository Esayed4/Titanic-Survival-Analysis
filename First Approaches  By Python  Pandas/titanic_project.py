import pandas as pd
import gdown
import zipfile
import numpy as np

# Google Drive file ID
file_id = '1A2_DHJIXQKQH0-DgG6_ewNVE7rMNoiO-'
url = f'https://drive.google.com/uc?id={file_id}'

# Download the ZIP file
output = 'titanic.zip'
gdown.download(url, output)


saved_path = 'D:/Esayed/data_engineering/projects/data analyst/titanic/titanic_files'
train_file_path= saved_path+'/'
test_file_path= saved_path+'/'
gender_submission_file_path= saved_path+'/'


# Now, open the ZIP file

with zipfile.ZipFile(output, 'r') as zip_ref:
    # List all the contents of the zip file
    
    file_names = zip_ref.namelist()
    print(file_names)


    train_file_path= train_file_path+file_names[2]
    test_file_path= test_file_path+file_names[1]
    gender_submission_file_path= gender_submission_file_path+file_names[0]
    
    # Extract all the contents to a directory
    zip_ref.extractall(saved_path)




train_df=pd.read_csv(train_file_path)
test_df=pd.read_csv(test_file_path)
gender_submission_df=pd.read_csv(gender_submission_file_path)


column_names=test_df.columns+gender_submission_df.columns[1]


#merge the gender_submission data set  with test  data set

merged_df = pd.merge(test_df, gender_submission_df, how='inner', on='PassengerId')
print('the first ten of the merged data set')
print(merged_df.head())


#concatinate the merged_df   with train  data set

Survived_column = train_df.pop('Survived')
train_df.insert( len(train_df.columns),'Survived',Survived_column)

Final_df=pd.concat([train_df,merged_df])



# description
print('describe the Final data set')
print(Final_df.describe())



#information


print('information the Final data set')
print(Final_df.info())




#print the first 10 rows
print('the first ten of train data set')
print(Final_df.head())



#delete dublications
Final_df.drop_duplicates()

#drob the unwanted columns
Final_df= Final_df.drop(['Cabin','Ticket'],axis=1)
print(Final_df.info())

#handel null values

avg_age=Final_df['Age'].mean()
Final_df['Age'] = Final_df['Age'].fillna(value=avg_age)


avg_fare=Final_df['Fare'].mean()
Final_df['Fare']=Final_df['Fare'].fillna(avg_fare)

Final_df= Final_df.dropna()

print(Final_df.info())

#-----------------make some transformations

#round the age column

Final_df['Age']=np.ceil(Final_df['Age'])
Final_df['Age'] = Final_df['Age'].astype('Int8')
print(Final_df['Age'])

#add age clasification column


age_classifications = []

# Classify ages
ages = Final_df['Age']
for age in ages:
    if age <= 17:
        age_classifications.append('Children')
    elif age <= 40:
        age_classifications.append('Adults')
    else:
        age_classifications.append('Seniors')

# Create a new DataFrame column for age classifications
age_clas_column = pd.DataFrame(age_classifications, columns=['age_classification'])
Final_df['age_classification']=age_classifications
print(Final_df['age_classification'])
print(Final_df.info())




path='D:/Esayed/data_engineering/projects/data analyst/titanic'
Final_df.to_csv(path+'/titanic.csv',index=False)