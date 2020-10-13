from flask import Flask, request, redirect, render_template, url_for
from db_connector import connect_to_database, execute_query

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
