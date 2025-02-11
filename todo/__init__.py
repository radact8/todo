from flask import Flask
app = Flask(__name__)
from todo import main


from todo import db
db.create_tasks_table()
db.create_dates_table()