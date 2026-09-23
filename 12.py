import sqlite3

conn = sqlite3.connect("students.db")
cursor = conn.cursor()

cursor.execute("""

    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL UNIQUE,
        grade TEXT NOT NULL
        )""")

conn.commit()

while True:
    print("\n1. Add Student")
    print("2. View all Students")
    print("3. Exit")
    choice = input("Choose an option:")


    if choice == "1":
        name = input("Enter student name: ")
        grade = input("Enter student grade ")
        cursor.execute("INSERT OR IGNORE INTO students (name,grade) VALUES (?,?)",(name, grade))
        conn.commit()
        print(f"{name}added!")

    elif choice == "2":
        cursor.execute("SELECT * FROM students")
        rows = cursor.fetchall()
        for row in rows:
            print(row)

    elif choice == "3":
        print("Goodbye!")
        conn.close()
        break
    else:
        print("Invalid option,try again")