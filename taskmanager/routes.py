from flask import render_template
from taskmanager import app,db

@app.route('/')
def home():
    return "Welcome to FoodZone DineReserve!"

@app.route('/about')
def about():
    return "This is the about page."