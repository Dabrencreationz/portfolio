from flask import Flask
import requests

@app.route('/')
def home():
    return "Welcome to Brenda\'s portfolio!"

@app.route('/')
def about():
    return "The portfoilio is to showcase the skills, knowledge and other tools acquired with learning via ALX Africa. I joined the program in August 2022 and it runs for one full year. During this period, I have been able to acquire some skills in python, C, MYSQL, Javascript, HTML and CSS. You will get to learn more about me by going through my skills profile."

@app.route('/')
def projects():
    return "Here, I showcased my skills in some of the projects I collaborated with some of my colleagues in ALX Africa."

@app.route('/')
def skills():
    return "Here are a list of some skills I have knowledge and experience on."

@app.route('/')
def donation():
    return "You can help bring my passion to live by contributing to my project via https//www.github.com/Dabrencreationz/portfolio, or by donating for the project to continue. I will appreciate your support no matter how little."

@app.route('/')
def testimonies():
    return "Hear some testimonies from those I have worked with and clients I have delivered to."

app = Flask(__name__)
