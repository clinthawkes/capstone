import random
from flask import Flask, request, redirect, render_template, url_for
from capstone.db_connector import connect_to_database, execute_query

app = Flask(__name__)
app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods = ['POST'])
def register():
    username = request.form[createUsername]
    password1 = request.form[createPassword1]
    password2 = request.form[createPassword2]
    # generate a random bank balance between $10 - $1,000,000
    bankBalance = random.randint(10, 1000000)
    # check username is unique
    # check password requirements are met
    # if passwords don't match return error page 3
    if (password1 != password2)
        return render_template('register_error3.html')
    query = 'INSERT INTO `accounts` (`user`, `password`, `balance`) VALUES (%s, %s, %s)'
    data = (username, password1, bankBalance)
    db_connection = connect_to_database()
    execute_query(db_connection, query, data)
    # will redirect to the login page (displaying success message)
    # if they have successfully created an account    
    return render_template('login_new.html')

@app.route('/login')
def login():
    return render_template('login.html')

# incorporate into login() function above   
@app.route('/login_error')
def login_error():
    return render_template('login_error.html')    

# append id to end of account URL
@app.route('/account/<int:id>', methods=['GET'])
def account(id):
    display_row = 'SELECT * from `accounts` WHERE `id` = %s' %(id)
    row_result = execute_query(db_connection, display_row).fetchone();
    return render_template('account.html', row = row_result)



if __name__ == "__main__":
    #app.run(host='127.0.0.1', port=5000)
