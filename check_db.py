
import sqlite3

conn = sqlite3.connect("practice.db")

rows = conn.execute(
    "SELECT id, task FROM tasks ORDER BY id"
).fetchall()

print("Saved tasks in SQLite:")
for row in rows:
    print(row)

conn.close()
