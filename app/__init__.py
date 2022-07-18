import os
import json
from crypt import methods
from email.policy import default
from datetime import datetime
from sqlite3 import Time
from flask import Flask, render_template, request
from dotenv import load_dotenv
from peewee import * 
from peewee import fn
from playhouse.shortcuts import model_to_dict

load_dotenv()
app = Flask(__name__)

# MySQL database connection
if os.getenv("TESTING") == "true":
    print("Running in test mode")
    mydb = SqliteDatabase('file:memory?mode=memory&cache=shared', uri=True)
else:
    mydb = MySQLDatabase(os.getenv("MYSQL_DATABASE"),
                     user=os.getenv("MYSQL_USER"),
                     password=os.getenv("MYSQL_PASSWORD"),
                     port=3306)

print(mydb)


class TimelinePost(Model):
    name = CharField()
    email = CharField()
    content = TextField()
    created_at = DateTimeField(default=datetime.now)

    class Meta:
        database = mydb

mydb.connect()
mydb.create_tables([TimelinePost])



#Landing page routing
@app.route("/")
def index():
    return render_template("index.html", title="Ivannas Portfolio", url=os.getenv("URL"))

@app.route("/about")
def about_us():
    return render_template("about.html")
  
@app.route("/hobbies")
def hobbies():
    return render_template("hobbies.html")
  
@app.route("/timeline")
def timeline():
    return render_template("timeline.html")
  
  
@app.route('/api/timeline_post', methods=['POST'])
def post_time_line_post():
    if("name" not in request.form):
        return "Invalid name", 400
    elif(request.form['content'] == ""):
        return "Invalid content", 400
    elif("@" not in request.form['email']):
        return "Invalid email", 400
    else:
        name = request.form['name']
        email = request.form['email']
        content = request.form['content']
        timeline_post = TimelinePost.create(name=name, email=email, content=content)

        return model_to_dict(timeline_post)

@app.route('/api/timeline_post', methods=['GET'])
def get_timeline_post():
    return {
        'timeline_posts': [
            model_to_dict(p)
            for p in TimelinePost.select().order_by(TimelinePost.created_at.desc())
            ]
        }


if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0")
