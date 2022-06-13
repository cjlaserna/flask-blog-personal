from dotenv import load_dotenv
import os
from flask import Flask, render_template, make_response
from .fetch import result

load_dotenv()
app = Flask(__name__)


@app.route('/')
def home():
    """ Landing Page """
    menu = [{'name': 'Home', 'url': '/'},
            {'name': 'Education', 'url': '#education'},
            {'name': 'Experiences', 'url': '#experiences'},
            {'name': 'Hobbies', 'url': '#hobbies'},
            {'name': 'Map', 'url': '#map'}
            ]
    title = 'MLH Fellowship Project'

    aboutMe = result['aboutMe']
    jobs = result['experiences']
    hobbies = result['hobbies']
    education = result['education']
    return render_template('./pages/home.html', menu=menu, aboutMe=aboutMe, jobs=jobs, hobbies=hobbies, education=education, title=title)
