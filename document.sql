-- Use this file to initialize the database
CREATE DATABASE IF NOT EXISTS bankdb;
USE bankdb;

CREATE TABLE IF NOT EXISTS account (
    acc_no INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    balance INT NOT NULL
);

-- Optional: Add some dummy data for testing
INSERT INTO account (acc_no, name, balance) VALUES (101, 'Raghav Tiwari', 5000);