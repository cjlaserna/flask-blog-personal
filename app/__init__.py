import os
from flask import Flask, render_template, request
from .fetch import result
from peewee import *
import datetime
from dotenv import load_dotenv
from playhouse.shortcuts import model_to_dict
import re

load_dotenv()

app = Flask(__name__)

# checking for testing mode
if os.getenv("TESTING") == "true":
    print("Running in test mode")
    mydb = SqliteDatabase('file:memory?mode=memory&cache=shared', uri=True)
else:
    mydb = MySQLDatabase(os.getenv("MYSQL_DATABASE"),
                        user=os.getenv("MYSQL_USER"),
                        password=os.getenv("MYSQL_PASSWORD"),
                        host=os.getenv("MYSQL_HOST"),
                        port=3306
                        )


class TimelinePost(Model):
    name = CharField()
    email = CharField()
    content = TextField()
    created_at = DateTimeField(default=datetime.datetime.now)


    class Meta:
    	database = mydb


mydb.connect()
mydb.create_tables([TimelinePost])

# site nav
menu = [{'name': 'Home', 'url': '/'},
            {'name': 'Education', 'url': '/#education'},
            {'name': 'Experiences', 'url': '/#experiences'},
            {'name': 'Hobbies', 'url': '/#hobbies'},
            {'name': 'Map', 'url': '/#map'},
            {'name': 'Timeline', 'url': '/timeline'}
            ]  

# site routing
@app.route('/')
def home():
    """ Landing Page """
    title = 'MLH Fellowship Project'

    aboutMe = result['aboutMe']
    jobs = result['experiences']
    hobbies = result['hobbies']
    education = result['education']
    return render_template('./pages/home.html', menu=menu, aboutMe=aboutMe, jobs=jobs, hobbies=hobbies, education=education, title=title)

@app.route("/timeline")
def timeline():
    title = 'MLH Fellowship Timeline'
        
    # pagination	    
    try:
        page = int(request.args['pg'])
    except:
        page = 1

    if (page == 1):
        cursor = 0
    else:
        cursor = 10* (page - 1)
    limit = 10 * page
    timeline_response = [model_to_dict(p) for p in TimelinePost.select().order_by(TimelinePost.created_at.desc())[cursor:limit]]   
    
    return render_template('./pages/timeline.html', title="Timeline", menu=menu, posts=timeline_response, pg=page)

# API routing
@app.route("/api/timeline_post", methods=["POST"])
def post_time_line_post():
    try:
        name = request.form['name']
    except: 
        return "Invalid name", 400

    valid_email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    if re.fullmatch(valid_email, request.form['email']):   
        email = request.form['email']
    else: 
        return "Invalid email", 400
    
    try:
        content = request.form['content']
        if len(content) == 0:
            return "Invalid content", 400
    except KeyError:
        return "Invalid content", 400
        
    timeline_post = TimelinePost.create(
        name=name, email=email, content=content)

    return model_to_dict(timeline_post)


@app.route("/api/timeline_post", methods=["GET"])
def get_time_line_post():
    return {
        'timeline_posts': [
            model_to_dict(p)
            for p in TimelinePost.select().order_by(TimelinePost.created_at.desc())
        ]
    }

@app.route("/api/timeline_post", methods=["DELETE"])
def delete_time_line_posts():
    arg = request.form['id']
    
    sql = TimelinePost.delete().where(TimelinePost.id == arg)
    sql.execute()
    return { 
	'timeline_posts': [
		model_to_dict(p)
		for p in TimelinePost.select().order_by(TimelinePost.created_at.desc())
	]
    }

# error handlers
@app.errorhandler(404)
def page_not_found(e):
        return render_template('./pages/errorpage.html', title="Error 404", menu=menu), 404