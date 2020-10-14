from flask import Flask, request, redirect, render_template, url_for
from capstone.db_connector import connect_to_database, execute_query

app = Flask(__name__)
app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/login')
def login():
    return render_template('login.html')
    
@app.route('/login_error')
def login_error():
    return render_template('login_error.html')    

@app.route('/account')
def account():
    return render_template('account.html')



if __name__ == "__main__":
    app.run(debug=True)
