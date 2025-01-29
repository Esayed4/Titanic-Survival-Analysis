Use Titanic;
-- Delete all data from the Final table
DELETE FROM Final;

-- Check if the 'merged_table' view exists; if not, create it
IF NOT EXISTS (SELECT * FROM sys.views WHERE name = 'merged_table' AND schema_id = SCHEMA_ID('dbo'))
BEGIN
    -- Create the 'merged_table' view by joining Test and Gender_submission tables
    EXEC ('CREATE VIEW merged_table AS
        SELECT 
            t1.*,
            t2.Survived
        FROM 
            Test t1
        INNER JOIN 
            Gender_submission t2 ON t1.PassengerId = t2.PassengerId;');
END;

-- Display data from the Train table
SELECT * FROM Train;

-- Insert data from the Train table into the Final table
INSERT INTO Final ([PassengerId],[Pclass] ,[Name], [Sex], [Age], [SibSp], [Parch], [Ticket], [Fare], [Cabin], [Embarked], [Survived])
SELECT PassengerId, Pclass, Name, Sex, Age, SibSp, Parch, Ticket, Fare, Cabin, Embarked, Survived
FROM Train;

-- Insert distinct data from the merged_table view into the Final table
INSERT INTO Final ([PassengerId],Pclass, [Name], [Sex], [Age], [SibSp], [Parch], [Ticket], [Fare], [Cabin], [Embarked], [Survived])
SELECT DISTINCT *
FROM merged_table;

-- Retrieve metadata about the columns in the Final table
SELECT 
    TABLE_NAME,
    COLUMN_NAME,
    DATA_TYPE AS column_datatype
FROM 
    INFORMATION_SCHEMA.COLUMNS
WHERE 
    TABLE_NAME = 'Final';

-- Count the number of null values in each column of the Final table
SELECT 
    COUNT(*) - COUNT(PassengerId) AS NullsInPassengerId,
    COUNT(*) - COUNT(Pclass) AS NullsInPclass,
    COUNT(*) - COUNT(Name) AS NullsInName,
    COUNT(*) - COUNT(Sex) AS NullsInSex,
    COUNT(*) - COUNT(Age) AS NullsInAge,
    COUNT(*) - COUNT(SibSp) AS NullsInSibSp,
    COUNT(*) - COUNT(Parch) AS NullsInParch,
    COUNT(*) - COUNT(Fare) AS NullsInFare,
    COUNT(*) - COUNT(Embarked) AS NullsInEmbarked,
    COUNT(*) - COUNT(Survived) AS NullsInSurvived
FROM 
    Final;

-- Replace null values in the Age column with the average age
UPDATE Final
SET Age = (SELECT AVG(Age) FROM Final WHERE Age IS NOT NULL)
WHERE Age IS NULL;

-- Replace null values in the Fare column with the average fare
UPDATE Final
SET Fare = (SELECT AVG(Fare) FROM Final WHERE Fare IS NOT NULL)
WHERE Fare IS NULL;

-- Round the Age column to the nearest whole number
UPDATE Final
SET Age = ROUND(Age, 0);

-- Change the data type of the Age column to INT
ALTER TABLE Final
ALTER COLUMN Age INT;

-- Check if the 'ageClassifications' column exists; if not, add it
IF NOT EXISTS (SELECT * FROM sys.columns WHERE name = 'ageClassifications' AND object_id = OBJECT_ID('Final'))
BEGIN
    ALTER TABLE Final
    ADD ageClassifications VARCHAR(50);
END;

-- Populate the 'ageClassifications' column based on age ranges
UPDATE Final
SET ageClassifications = 
    CASE 
        WHEN Age <= 17 THEN 'Children'
        WHEN Age <= 40 THEN 'Adults'
        ELSE 'Seniors'
    END;

-- Convert the Sex column to binary (1 for male, 0 for female)
UPDATE Final
SET Sex = 
    CASE 
        WHEN Sex = 'male' THEN 1
        ELSE 0
    END;

-- Change the data type of the Sex column to INT
ALTER TABLE Final
ALTER COLUMN Sex INT;

-- Display all data from the Final table
SELECT * FROM Final;
