-- create_students_table.sql

-- Create students table for storing input data and prediction results
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    average_score REAL NOT NULL,
    attendance_rate REAL NOT NULL,
    behavior_score REAL NOT NULL,
    prediction INTEGER NOT NULL  -- 1 = At Risk, 0 = Not at Risk
);

-- Optional: Insert sample records for testing
INSERT INTO students (name, average_score, attendance_rate, behavior_score, prediction)
VALUES 
('Ahmed Hassan', 45.0, 75.0, 2.0, 1),
('Fatima Abdi', 78.0, 90.0, 5.0, 0),
('Khadar Mohamed', 52.0, 60.0, 3.0, 1);

-- Retrieve all records to verify
SELECT * FROM students;
