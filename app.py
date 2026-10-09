
import streamlit as st
import sqlite3

st.set_page_config(page_title="Hackathon Practice", page_icon="🚀")

st.title("🚀 Hackathon Practice App")
st.write("My Python + Streamlit + SQLite setup is working!")

conn = sqlite3.connect("practice.db")
conn.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        task TEXT NOT NULL
    )
""")

task = st.text_input("Enter a task")

if st.button("Add Task"):
    if task.strip():
        conn.execute("INSERT INTO tasks (task) VALUES (?)", (task.strip(),))
        conn.commit()
        st.success("Task added successfully!")
    else:
        st.warning("Please enter a task.")

rows = conn.execute("SELECT id, task FROM tasks ORDER BY id DESC").fetchall()

st.subheader("Your Tasks")
if rows:
    st.dataframe(rows, use_container_width=True)
else:
    st.info("No tasks added yet.")

conn.close()
