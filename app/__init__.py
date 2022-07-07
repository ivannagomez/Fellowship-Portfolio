import os
from flask import Flask, render_template, request, json
from dotenv import load_dotenv
import json
from peewee import *
from datetime import datetime
from playhouse.shortcuts import model_to_dict

load_dotenv()
app = Flask(__name__)

# MySQL database connection
mydb = MySQLDatabase(os.getenv("MYSQL_DATABASE"),
                     user=os.getenv("MYSQL_USER"),
                     password=os.getenv("MYSQL_PASSWORD"),
                     port=3306)

print(mydb)

# Timeline
class TimelinePost(Model):
    name = CharField()
    email = CharField()
    content = TextField()
    created_at = DateTimeField(default=datetime.now)

    class Meta:
        database = db

db.connect()
db.create_tables([TimelinePost])

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
def post_timeline_post():
    name = request.form['name']
    email = request.form['email']
    content = request.form['content']
    timeline_post = TimelinePost.create(name=name, email=email, content=content)

    return model_to_dict(timeline_post)

@app.route('/api/timeline_post', methods=['GET'])
def get_timeline_post(): 
    return{
        'timeline_posts': [
            model_to_dict(p)
            for p in TimelinePost.select().order_by(TimelinePost.created_at.desc())
        ]
    }

if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0")
