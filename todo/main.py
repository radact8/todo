from todo import app,db
from flask import render_template,request,redirect,url_for
import sqlite3
import datetime

DATABASE = 'database.db'


@app.route('/')
def index():
    db.create_tasks_table()
    con = sqlite3.connect(DATABASE)
    db_tasks = con.execute('SELECT * FROM tasks').fetchall()
    db_results = con.execute('SELECT * FROM task_result').fetchall()
    con.close()
    task_name = []
    results = []
    for task in db_tasks:
        task_name.append({'id':task[0],'name':task[1]})
    for result in db_results:
        results.append({'taskid':result[1],'result':result[2],'date':result[3]})

    if(len(task_name) == 0):
        db.create_tasks_list()
    
    for i in range(len(results)):
        print(results[i])

    size = len(task_name)
    return render_template('view.html',task_name=task_name,size=size)
    
@app.route('/form')
def form():
    con = sqlite3.connect(DATABASE)
    db_tasks = con.execute('SELECT * FROM tasks').fetchall()
    con.close()
    task_name = []
    for task in db_tasks:
        task_name.append({'id':task[0],'name':task[1]})

    size = len(task_name)
    return render_template('form.html',size=size)


#フォーム管理(main内)
@app.route('/check0',methods=['GET','POST'])
def check0():
    task_status = request.form.get('name0','name0')
    today = "20"+datetime.date.today().strftime("%y-%m-%d",)
    if(task_status == "o"):
        con = sqlite3.connect(DATABASE)
        con.execute("""INSERT INTO task_result (result, taskid)SELECT 1, 0 WHERE NOT EXISTS (SELECT 1 FROM task_result WHERE recorded_at = ?)""", (today,))
        con.commit()
        con.close()
    elif(task_status == "x"):
        con = sqlite3.connect(DATABASE)
        con.execute("INSERT INTO task_result (result,taskid) values(?,?)",(0,0))
        con.commit()
        con.close()    
    
    return redirect(url_for('index'))

@app.route('/check1',methods=['GET','POST'])
def check1():
    task_status = request.form.get('name1','name1')
    today = "20"+datetime.date.today().strftime("%y-%m-%d",)
    if(task_status == "o"):
        con = sqlite3.connect(DATABASE)
        con.execute("""INSERT INTO task_result (result, taskid)SELECT 1, 1 WHERE NOT EXISTS (SELECT 1 FROM task_result WHERE recorded_at = ?)""", (today,))
        con.commit()
        con.close()
    elif(task_status == "x"):
        con = sqlite3.connect(DATABASE)
        con.execute("INSERT INTO task_result (result,taskid) values(?,?)",(0,1))
        con.commit()
        con.close()  
    
    return redirect(url_for('index'))

@app.route('/check2',methods=['GET','POST'])
def check2():
    task_status = request.form.get('name2','name2')
    today = "20"+datetime.date.today().strftime("%y-%m-%d",)
    if(task_status == "o"):
        con = sqlite3.connect(DATABASE)
        con.execute("""INSERT INTO task_result (result, taskid)SELECT 1, 2 WHERE NOT EXISTS (SELECT 1 FROM task_result WHERE recorded_at = ?)""", (today,))
        con.commit()
        con.close()
    elif(task_status == "x"):
        con = sqlite3.connect(DATABASE)
        con.execute("INSERT INTO task_result (result,taskid) values(?,?)",(0,2))
        con.commit()
        con.close()  
    
    return redirect(url_for('index'))

@app.route('/check3',methods=['GET','POST'])
def check3():
    task_status = request.form.get('name3','name3')
    today = "20"+datetime.date.today().strftime("%y-%m-%d",)
    if(task_status == "o"):
        con = sqlite3.connect(DATABASE)
        con.execute("""INSERT INTO task_result (result, taskid)SELECT 1, 3 WHERE NOT EXISTS (SELECT 1 FROM task_result WHERE recorded_at = ?)""", (today,))
        con.commit()
        con.close()
    elif(task_status == "x"):
        con = sqlite3.connect(DATABASE)
        con.execute("INSERT INTO task_result (result,taskid) values(?,?)",(0,3))
        con.commit()
        con.close()  
    
    return redirect(url_for('index'))

@app.route('/check4',methods=['GET','POST'])
def check4():
    task_status = request.form.get('name4','name4')
    today = "20"+datetime.date.today().strftime("%y-%m-%d",)
    if(task_status == "o"):
        con = sqlite3.connect(DATABASE)
        con.execute("""INSERT INTO task_result (result, taskid)SELECT 1, 4 WHERE NOT EXISTS (SELECT 1 FROM task_result WHERE recorded_at = ?)""", (today,))
        con.commit()
        con.close()
    elif(task_status == "x"):
        con = sqlite3.connect(DATABASE)
        con.execute("INSERT INTO task_result (result,taskid) values(?,?)",(0,4))
        con.commit()
        con.close()  
    
    return redirect(url_for('index'))

@app.route('/check5',methods=['GET','POST'])
def check5():
    task_status = request.form.get('name5','name5')
    today = "20"+datetime.date.today().strftime("%y-%m-%d",)
    if(task_status == "o"):
        con = sqlite3.connect(DATABASE)
        con.execute("""INSERT INTO task_result (result, taskid)SELECT 1, 5 WHERE NOT EXISTS (SELECT 1 FROM task_result WHERE recorded_at = ?)""", (today,))
        con.commit()
        con.close()
    elif(task_status == "x"):
        con = sqlite3.connect(DATABASE)
        con.execute("INSERT INTO task_result (result,taskid) values(?,?)",(0,5))
        con.commit()
        con.close()  
    
    return redirect(url_for('index'))

@app.route('/check6',methods=['GET','POST'])
def check6():
    task_status = request.form.get('name6','name6')
    today = "20"+datetime.date.today().strftime("%y-%m-%d",)
    if(task_status == "o"):
        con = sqlite3.connect(DATABASE)
        con.execute("""INSERT INTO task_result (result, taskid)SELECT 1, 6 WHERE NOT EXISTS (SELECT 1 FROM task_result WHERE recorded_at = ?)""", (today,))
        con.commit()
        con.close()
    elif(task_status == "x"):
        con = sqlite3.connect(DATABASE)
        con.execute("INSERT INTO task_result (result,taskid) values(?,?)",(0,6))
        con.commit()
        con.close()  
    
    return redirect(url_for('index'))

@app.route('/check7',methods=['GET','POST'])
def check7():
    task_status = request.form.get('name7','name7')
    today = "20"+datetime.date.today().strftime("%y-%m-%d",)
    if(task_status == "o"):
        con = sqlite3.connect(DATABASE)
        con.execute("""INSERT INTO task_result (result, taskid)SELECT 1, 7 WHERE NOT EXISTS (SELECT 1 FROM task_result WHERE recorded_at = ?)""", (today,))
        con.commit()
        con.close()
    elif(task_status == "x"):
        con = sqlite3.connect(DATABASE)
        con.execute("INSERT INTO task_result (result,taskid) values(?,?)",(0,7))
        con.commit()
        con.close()  
    
    return redirect(url_for('index'))

#タスク入力
@app.route('/add0',methods=['GET','POST'])
def add0():
    task_name=request.form['add0']
    
    con = sqlite3.connect(DATABASE)
    con.execute("UPDATE tasks SET taskname=(?) WHERE taskid=1",(task_name,))
    con.commit()
    con.close()
    
    return redirect(url_for('index'))

@app.route('/add1',methods=['GET','POST'])
def add1():
    task_name=request.form['add1']
    
    con = sqlite3.connect(DATABASE)
    con.execute("UPDATE tasks SET taskname=(?) WHERE taskid=2",(task_name,))
    con.commit()
    con.close()
    
    return redirect(url_for('index'))

@app.route('/add2',methods=['GET','POST'])
def add2():
    task_name=request.form['add2']
    
    con = sqlite3.connect(DATABASE)
    con.execute("UPDATE tasks SET taskname=(?) WHERE taskid=3",(task_name,))
    con.commit()
    con.close()
    
    return redirect(url_for('index'))

@app.route('/add3',methods=['GET','POST'])
def add3():
    task_name=request.form['add3']
    
    con = sqlite3.connect(DATABASE)
    con.execute("UPDATE tasks SET taskname=(?) WHERE taskid=4",(task_name,))
    con.commit()
    con.close()
    
    return redirect(url_for('index'))

@app.route('/add4',methods=['GET','POST'])
def add4():
    task_name=request.form['add4']
    
    con = sqlite3.connect(DATABASE)
    con.execute("UPDATE tasks SET taskname=(?) WHERE taskid=5",(task_name,))
    con.commit()
    con.close()
    
    return redirect(url_for('index'))

@app.route('/add5',methods=['GET','POST'])
def add5():
    task_name=request.form['add5']
    
    con = sqlite3.connect(DATABASE)
    con.execute("UPDATE tasks SET taskname=(?) WHERE taskid=6",(task_name,))
    con.commit()
    con.close()
    
    return redirect(url_for('index'))

@app.route('/add6',methods=['GET','POST'])
def add6():
    task_name=request.form['add6']
    
    con = sqlite3.connect(DATABASE)
    con.execute("UPDATE tasks SET taskname=(?) WHERE taskid=7",(task_name,))
    con.commit()
    con.close()
    
    return redirect(url_for('index'))

@app.route('/add7',methods=['GET','POST'])
def add7():
    task_name=request.form['add7']
    
    con = sqlite3.connect(DATABASE)
    con.execute("UPDATE tasks SET taskname=(?) WHERE taskid=8",(task_name,))
    con.commit()
    con.close()
    
    return redirect(url_for('index'))


@app.route('/test',methods=['POST'])
def test():
    con = sqlite3.connect(DATABASE)
    db_tasks = con.execute('SELECT * FROM tasks').fetchall()
    db_result = con.execute('SELECT * FROM task_result').fetchall()
    con.close()

    tasks = []
    results = []
    view_results = []
    for task in db_tasks:
        tasks.append({'id':task[0],'name':task[1]})
    
    for result in db_result:
        results.append({'taskid':result[1],'result':result[2],'date':result[3]})

    print("20"+datetime.date.today().strftime("%y-%m-%d"))
    return render_template('testview.html',tasks = tasks,)
