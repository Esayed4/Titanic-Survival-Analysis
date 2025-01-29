-- Create database if it does not exist
IF NOT EXISTS (SELECT * FROM sys.databases WHERE name = 'Titanic')
BEGIN
    CREATE DATABASE [Titanic];
END;
GO

-- Use the database
USE Titanic;
GO

-- Create tables if they do not exist

IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'Train')
BEGIN
    CREATE TABLE Train (
        PassengerId int PRIMARY KEY,
        Survived INT,
        Pclass INT,
        Name VARCHAR(150),
        Sex VARCHAR(10),
        Age FLOAT,
        SibSp INT,
        Parch INT,
        Ticket VARCHAR(10),
        Fare FLOAT,
        Cabin VARCHAR(10),
        Embarked VARCHAR(10)
    );
END;
GO


IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'Test')
BEGIN
    CREATE TABLE Test (
        PassengerId VARCHAR(10) PRIMARY KEY,
        Pclass INT,
        Name VARCHAR(150),
        Sex VARCHAR(10),
        Age FLOAT,
        SibSp INT,
        Parch INT,
        Ticket VARCHAR(10),
        Fare FLOAT,
        Cabin VARCHAR(10),
        Embarked VARCHAR(10)
    );
END;
GO

IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'Gender_submission')
BEGIN
    CREATE TABLE Gender_submission (
        PassengerId VARCHAR(10) PRIMARY KEY,
        Survived INT
    );
END;
GO

IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'Final')
BEGIN
    CREATE TABLE Final (
        PassengerId VARCHAR(10) PRIMARY KEY,
        
        Pclass INT,
        Name VARCHAR(150),
        Sex VARCHAR(100),
        Age FLOAT,
        SibSp INT,
        Parch INT,
        Ticket VARCHAR(100),
        Fare FLOAT,
        Cabin VARCHAR(100),
        Embarked VARCHAR(100),
		Survived INT
    );
END;
GO