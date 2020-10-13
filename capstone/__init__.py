from flask import Flask, request, redirect, render_template, url_for
from capstone.db_connector import connect_to_database, execute_query

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/login')
def register():
    return render_template('login.html')

@app.route('/account')
def register():
    return render_template('acount.html')



if __name__ == "__main__":
    app.run(debug=True)
