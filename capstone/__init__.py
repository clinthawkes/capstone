import random
import MySQLdb.cursors
import re
from flask import Flask, request, redirect, render_template, url_for, session
#from flask_mysqldb import MySQL
from capstone.db_connector import connect_to_database, execute_query

app = Flask(__name__)
app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
    return render_template('index.html')

# creation of user account, necessary to view account details page
@app.route('/register', methods = ['POST'])
def register():
    username = request.form['createUsername']
    password1 = request.form['createPassword1']
    password2 = request.form['createPassword2']
    # generate a random bank balance between $10 - $1,000,000
    bankBalance = random.randint(10, 1000000)
    # check username is unique
    cursor = mysql.connection.cursor()
    check_name = cursor.execute('SELECT (username,) FROM `accounts` WHERE `user` = %s')
    if (check_name > 0):
        return render_template('register_error1.html')
    # check password requirements are met
    specialChar = ['$', '@', '#', '%']
    if not any(char in specialChar for char in password1):
        return render_template('register_error2.html')
    if not any(char.islower() for char in password1):
        return render_template('register_error2.html')
    if not any(char.isupper() for char in password1):
        return render_template('register_error2.html')
    if not any(char.isdigit() for char in password1):
        return render_template('register_error2.html')
    if len(password1) < 8:
        return render_template('register_error2.html')
    # if passwords don't match return error page 3
    if (password1 != password2):
        return render_template('register_error3.html')
    query = 'INSERT INTO `accounts` (`user`, `password`, `balance`) VALUES (%s, %s, %s)'
    data = (username, password1, bankBalance)
    db_connection = connect_to_database()
    execute_query(db_connection, query, data)
    # will redirect to the login page (displaying success message)
    # if they have successfully created an account    
    return render_template('login_new.html')

# login checks username and password against stored usernames and passwords in the database -
# if matching a session is created
@app.route('/login', methods = ['POST'])
def login():
    user = request.form['username']
    password = request.form['password']
    # check if user account exists
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM `accounts` WHERE `user` = %s AND password = %s', (user, password,))
    userAccount = cursor.fetchone()
    # if user account exists create session data which can be accessed in other routes
    if userAccount:
        session['loggedin'] = True
        session['id'] = account['id']
        session['user'] = account['user']
        # redirect to their account details page
        return render_template('account.html', user=user)
    else:    
        return render_template('login_error.html')

# allows user to log out from their session
@app.route('/logout',  methods = ['POST'])
def logout():
   # Remove session data and log user out of their account
   session.pop('loggedin', None)
   session.pop('id', None)
   session.pop('user', None)
   # Redirect to login page
   return redirect(url_for('login'))        

# loads user's account details page if they are logged in - 
# if not they are redirected to login page
@app.route('/account/<user>', methods=['GET'])
def account(user):
    # check user is logged in
    if 'loggedin' in session:
        display_row = 'SELECT * from `accounts` WHERE `user` = %s' %(user)
        row_result = execute_query(db_connection, display_row).fetchone();
        return render_template('account.html', user = session['user'], row = row_result)
    # if not logged in redirect to login page
    else:
        return redirect(url_for('login'))



if __name__ == "__main__":
    #app.run(host='127.0.0.1', port=5000)
