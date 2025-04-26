import sqlite3

# Connect to SQLite
connection = sqlite3.connect("student.db")

# Create a cursor object for DB operations
cursor = connection.cursor()

# Create the STUDENT table
table_info = """
CREATE TABLE IF NOT EXISTS STUDENT (
    NAME VARCHAR(25),
    CLASS VARCHAR(25),
    SECTION VARCHAR(25),
    MARKS INT
);
"""
cursor.execute(table_info)

# Insert 50 records into STUDENT table
students = [
    ("Student_" + str(i), "Class_" + str((i % 10) + 1), chr(65 + (i % 5)), 50 + (i % 50))
    for i in range(1, 51)
]

cursor.executemany("INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS) VALUES (?, ?, ?, ?);", students)

# Commit the changes
connection.commit()

# Retrieve and show few records
cursor.execute("SELECT * FROM STUDENT LIMIT 10;")  # Retrieve first 10 students
rows = cursor.fetchall()

print("Few records from STUDENT table:")
for row in rows:
    print(row)

# Close the connection
connection.close()
