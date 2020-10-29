import os
import string
import random
import mysql.connector
import re
from flask import Flask, request, redirect, render_template, url_for, session
from capstone.db_connector import connect_to_database, execute_query

app = Flask(__name__)
app = Flask(__name__, static_url_path='/static')


@app.route('/')
def index():
    return render_template('index.html')

# creation of user account, necessary to view account details page
@app.route('/register', methods = ['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['createUsername']
        password1 = request.form['createPassword1']
        password2 = request.form['createPassword2']
        # generate a random bank balance between $10 - $1,000,000
        bankBalance = random.randint(10, 1000000)
        # check username is unique
        query1 = 'SELECT user FROM accounts WHERE user = %s'
        data1 = (username, )
        db_connection = connect_to_database()
        check_name = execute_query(db_connection, query1, data1).fetchall()
        #cursor = mysql.connection.cursor()
        #check_name = cursor.execute('SELECT (username,) FROM `accounts` WHERE `user` = %s')
        if (check_name):
            return render_template('register_error1.html')
        # check password requirements are met
        specialChar = ['$', '@', '#', '%', '!', '^', '&', '*', '(' ')']
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
        query = 'INSERT INTO accounts (user, password, balance) VALUES (%s, %s, %s)'
        data = (username, password1, bankBalance)
        db_connection = connect_to_database()
        execute_query(db_connection, query, data)
        db_connection.commit() 
        # will redirect to the login page (displaying success message)
        # if they have successfully created an account    
        return render_template('login_new.html')
    else:
        return render_template('register.html')


# login checks username and password against stored usernames and passwords in the database -
# if matching a session is created
@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['username']
        password = request.form['password']
        # check if user account exists
        connection = connect_to_database()
        query = 'SELECT * FROM accounts WHERE user = %s AND password = %s'
        data = (user, password)
        userAccount = execute_query(connection, query, data).fetchall() 
        # if user account exists create session data which can be accessed in other routes
        if userAccount:
            #session['loggedin'] = True
            #session['id'] = account['id']
            #session['user'] = account['user']
            # redirect to their account details page
            return render_template('account.html', user=userAccount)
        else:    
            return render_template('login_error.html')
    else:
        referrer = request.referrer
        return render_template('login.html', referrer=referrer)


# allows user to log out from their session
@app.route('/logout',  methods = ['POST'])
def logout():
   # Remove session data and log user out of their account
   session.pop('loggedin', None)
   session.pop('id', None)
   session.pop('user', None)
   # Redirect to main page
   return redirect(url_for('index'))        


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

@app.route('/withdraw', methods=['POST'])
def withdraw():
        user = request.form['username']
        db_connection = connect_to_database()
        cursor = db_connection.cursor()
        cursor.execute("UPDATE `accounts` SET `balance` = 0 WHERE `user` = '%s'" % (request.form['username']))
        db_connection.commit()
        query = "SELECT * FROM accounts WHERE user = %s"
        data = (request.form['username'], )
        updated = execute_query(db_connection, query, data).fetchall()
        #row_result1 = execute_query(db_connection1, newBalance, data).fetchone() 
        #return "ok"
        return render_template('account.html', user = updated)


##################################################################
#####             VULNERABILTY 1: SQL INJECTION             ######
##################################################################

# using string concatenation instead of parameterized queries to access
# a single user's account or dump the contents of the database
@app.route('/login_sql_inj', methods = ['GET', 'POST'])
def login_sql_inj():
    if request.method == 'POST':
        user = request.form['username']
        password = request.form['password']
        # check if user account exists
        db_connection = connect_to_database()
        cursor = db_connection.cursor()
        query = "SELECT * FROM `accounts` WHERE `user` = '" + user + "' AND `password` = '" + password + "' ";
        cursor.execute(query)
        userAccount = cursor.fetchall()
        #db_connection.commit()
        # if user account exists create session data which can be accessed in other routes
        if userAccount:
            #session['loggedin'] = True
            #session['id'] = account['id']
            #session['user'] = account['user']
            # redirect to their account details page
            return render_template('account.html', user=userAccount)
        else:    
            return render_template('login_sql_inj.html')
    else:
        return render_template('login_sql_inj.html')
        
##################################################################
#####          VULNERABILTY 2: CROSS SITE SCRIPTING         ######
##################################################################

# displays an example of a phishing email received by the user 
# containing a malicious link to a vulnerable web page with an
# XSS payload
@app.route('/phishing')
def phishing():
     return render_template('phishing.html')
     
@app.route('/hacker_info' , methods = ['GET','POST'])
def hacker_info():
    user = request.args.get('username')
    password = request.args.get('password')
    if user:
        f = open("/var/www/capstone/capstone/static/files/hacked.txt", "a")
        data = str(user) + " " + str(password) + ',' 
        f.write(data)
        f.close()
    f = open("/var/www/capstone/capstone/static/files/hacked.txt", "r")
    contents = f.read()
    final = contents.split(',')
    f.close()
    return render_template('hacker_info.html', contents=final)

# autoescaping is turned off in in login_xss.html
@app.route('/login_xss', methods = ['GET'])
def login_xss():
    user = request.args.get('username')
    password = request.args.get('password')    
    connection = connect_to_database()
    query = 'SELECT * FROM accounts WHERE user = %s AND password = %s'
    data = (user, password)
    userAccount = execute_query(connection, query, data).fetchall() 
    if userAccount:
        return render_template('account_xss.html', user=userAccount)
    else:    
        return render_template('login_xss.html', username=user)
  

if __name__ == "__main__":
    app.run()
