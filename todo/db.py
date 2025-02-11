import sqlite3

DATABASE = 'database.db'

def create_tasks_table():
    con = sqlite3.connect(DATABASE)
    con.execute("CREATE TABLE IF NOT EXISTS tasks(taskid integer primary key autoincrement,taskname text not null)")
    con.close()

def create_tasks_list(): #中身は空
    con = sqlite3.connect(DATABASE)
    con.execute("SELECT COUNT(*) FROM tasks")
    for i in range(8):
        taskname = ""
        con.execute("INSERT INTO tasks (taskname) values(?)",(taskname,))
        con.commit()
    con.close()

def create_dates_table():
    con = sqlite3.connect(DATABASE)
    con.execute("CREATE TABLE IF NOT EXISTS task_result(id INTEGER PRIMARY KEY AUTOINCREMENT,taskid integer,result integr,recorded_at date DEFAULT(DATE('now')),FOREIGN KEY (taskid) REFERENCES tasks(id))")

def add_dates():
    con = sqlite3.connect(DATABASE)
    con.execute("INSERT INTO task_reault (result) (taskid)",())
    con.commit()
    con.close()