import os
from flask import Flask, render_template, request, json
from dotenv import load_dotenv
import json
from peewee import *
from datetime import datetime

load_dotenv()
app = Flask(__name__)

# connect to MySQL database
mydb = MySQLDatabase(os.getenv("MYSQL_DATABASE"),
                     user=os.getenv("MYSQL_USER"),
                     password=os.getenv("MYSQL_PASSWORD"),
                     port=3306)

print(mydb)

@app.route("/")
def index():
    return render_template("index.html", title="Ivannas Portfolio", url=os.getenv("URL"))

@app.route("/about")
def about_us():
    return render_template("about.html")
  
@app.route("/hobbies")
def hobbies():
    return render_template("hobbies.html")


if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0")
