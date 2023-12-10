CREATE DATABASE IF NOT EXISTS RiskAssessmentDB;
USE RiskAssessmentDB;
CREATE TABLE IF NOT EXISTS Companies (
    CompanyID INT PRIMARY KEY,
    CompanyName VARCHAR(255) NOT NULL,
    StockSymbol VARCHAR(10) NOT NULL
);
CREATE TABLE IF NOT EXISTS Reports (
    ReportID INT PRIMARY KEY,
    CompanyID INT,
    ReportYear INT NOT NULL,
    ReportContent TEXT NOT NULL,
    FOREIGN KEY (CompanyID) REFERENCES Companies(CompanyID)
);
CREATE TABLE IF NOT EXISTS FinancialData (
    FinancialID INT PRIMARY KEY,
    CompanyID INT,
    ReportID INT,
    FOREIGN KEY (CompanyID) REFERENCES Companies(CompanyID),
    FOREIGN KEY (ReportID) REFERENCES Reports(ReportID)
);
CREATE TABLE IF NOT EXISTS AIResults (
    ResultID INT PRIMARY KEY,
    CompanyID INT,
    RiskCategory VARCHAR(50) NOT NULL,
    RiskScore FLOAT NOT NULL,
    FOREIGN KEY (CompanyID) REFERENCES Companies(CompanyID)
);
CREATE TABLE IF NOT EXISTS Milestones (
    MilestoneID INT PRIMARY KEY,
    MilestoneName VARCHAR(255) NOT NULL,
    CompletionDate DATE -- Add other relevant fields
);
CREATE TABLE IF NOT EXISTS ProjectTasks (
    TaskID INT PRIMARY KEY,
    MilestoneID INT,
    TaskDescription TEXT NOT NULL,
    AssignedTo VARCHAR(50) NOT NULL,
    Status VARCHAR(20) NOT NULL,
    FOREIGN KEY (MilestoneID) REFERENCES Milestones(MilestoneID)
);