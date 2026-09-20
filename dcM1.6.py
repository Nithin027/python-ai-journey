import sqlite3

conn = sqlite3.connect("students.db")
cursor = conn.cursor()


cursor.execute("""
    CREATE TABLE IF NOT EXISTS students(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL UNIQUE,
        grade  TEXT NOT NULL
        )
   """)

cursor.execute("INSERT OR IGNORE INTO students(name, grade) VALUES (?,?)",("Nithin", "A"))
conn.commit()

cursor.execute("INSERT OR IGNORE INTO students(name, grade) VALUES(?,?)", ("Leo", "B"))
conn.commit()

cursor.execute("UPDATE students SET grade = ? WHERE name = ?", ("A+", "Nithin"))

cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()
print(rows)

conn.close()