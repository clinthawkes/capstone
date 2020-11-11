import os
import string
import random
import mysql.connector
import re
from flask import Flask, flash, request, redirect, render_template, url_for, session
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
        token = request.form['attackToken']
        referrer = request.form['referrer']
        # generate a random bank balance between $10 - $1,000,000
        bankBalance = random.randint(10, 1000000)
        # check username is unique
        query1 = 'SELECT user FROM accounts WHERE user = %s'
        data1 = (username, )
        db_connection = connect_to_database()
        check_name = execute_query(db_connection, query1, data1).fetchall()
        if (check_name):
            flash('Username Not Available. Please Try Again!', 'danger')
            return render_template('register.html', attackToken=token, referrer=referrer)
        # check password requirements are met
        specialChar = ['$', '@', '#', '%', '!', '^', '&', '*', '(' ')']
        if not any(char in specialChar for char in password1):
            flash('Password Does Not Meet Requirements. Please Try Again!', 'danger')
            return render_template('register.html', attackToken=token, referrer=referrer)
        if not any(char.islower() for char in password1):
            flash('Password Does Not Meet Requirements. Please Try Again!', 'danger')
            return render_template('register.html', attackToken=token, referrer=referrer)
        if not any(char.isupper() for char in password1):
            flash('Password Does Not Meet Requirements. Please Try Again!', 'danger')
            return render_template('register.html', attackToken=token, referrer=referrer)
        if not any(char.isdigit() for char in password1):
            flash('Password Does Not Meet Requirements. Please Try Again!', 'danger')
            return render_template('register.html', attackToken=token, referrer=referrer)
        if len(password1) < 8:
            flash('Password Does Not Meet Requirements. Please Try Again!', 'danger')
            return render_template('register.html', attackToken=token, referrer=referrer)
        # if passwords don't match return error page 3
        if (password1 != password2):
            flash('Passwords Do Not Match. Please Try Again!', 'danger')
            return render_template('register.html', attackToken=token, referrer=referrer)
        query = 'INSERT INTO accounts (user, password, balance) VALUES (%s, %s, %s)'
        data = (username, password1, bankBalance)
        db_connection = connect_to_database()
        execute_query(db_connection, query, data)
        db_connection.commit()
        # will redirect to the login page (displaying success message)
        # if they have successfully created an account
        flash('Registration Successful! Please Login Below', 'success') 
        if referrer:
            #manipulates text so the page viewed before going to the registration page is where
            #the user is directed after they have successfully created a new user
            referrer = referrer.split('/')
            referrer = referrer[len(referrer) - 1]
            return render_template('/' + referrer + '.html', attackToken=token)
        #this is only rendered if the user went to the registration page directly
        #e.g. typed faultyvault.com/register in the address bar of the browser
        return render_template('login.html', attackToken=0)
    else:
        token = request.args.get('attackToken')
        referrer = request.referrer
        if referrer:
            #removes any query data from the referring url
            if '?' in referrer:
                referrer = referrer.split('?', 2)
                referrer = referrer[0]
            return render_template('register.html', referrer=referrer, attackToken=token)
        #this is only rendered if the user went to the registration page directly
        #e.g. typed faultyvault.com/register in the address bar of the browser
        return render_template('register.html', referrer='/login')


# login checks username and password against stored usernames and passwords in the database -
# if matching a session is created
@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['username']
        password = request.form['password']
        token = request.form['attackToken']
        # check if user account exists
        connection = connect_to_database()
        query = 'SELECT * FROM accounts WHERE user = %s AND password = %s'
        data = (user, password)
        userAccount = execute_query(connection, query, data).fetchall()
        # if user account exists load account page
        if userAccount:
            return render_template('account.html', user=userAccount)
        else:
            flash('Incorrect Username/Password', 'danger')
            return render_template('login.html', attackToken=token)
    else:
        token = request.args.get('attackToken')
        return render_template('login.html', attackToken=token)


# allows user to log out from their session
@app.route('/logout',  methods = ['POST'])
def logout():
   # Remove session data and log user out of their account
   session.pop('loggedin', None)
   session.pop('username', None)
   session.pop('password', None)
   session.pop('data', None)
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
        # if user account exists load account page
        if userAccount:
            return render_template('account.html', user=userAccount)
        else:
            flash('Incorrect Username/Password', 'danger')
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

# displays an example of a phishing email received by the user
# containing a malicious link to a non-vulnerable web page
@app.route('/phishing_safe')
def phishing_safe():
     return render_template('phishing_safe.html')

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


##################################################################
#####       VULNERABILTY 3: SECURITY MISCONFIGURATION       ######
##################################################################

@app.route('/account_admin/<user>', methods=['GET'])
def account_admin(user):
    # check user is logged in
    if 'loggedin' in session:
        display_row = 'SELECT * from `accounts` WHERE `user` = %s' %(user)
        row_result = execute_query(db_connection, display_row).fetchone();
        return render_template('account_admin.html', user = session['user'], row = row_result)
    # if not logged in redirect to login page
    else:
        return redirect(url_for('login_misconfig'))


@app.route('/login_misconfig', methods = ['POST', 'GET'])
def login_misconfig():
    if request.method == 'POST':
        user = request.form['username']
        password = request.form['password']
        # check if user account exists
        connection = connect_to_database()
        query = 'SELECT * FROM default_accounts WHERE user = %s AND password = %s'
        data = (user, password)
        userAccount = execute_query(connection, query, data).fetchall()
        # if user account exists return account page
        if userAccount:
            return render_template('account_admin.html', user=userAccount)
        else:
            #this retrieves the log data for the error message
            query2 = 'SELECT * FROM mysql.general_log a ORDER BY event_time desc LIMIT 6;'
            log = execute_query(connection, query2).fetchall() 
            query3 = 'SHOW VARIABLES LIKE "%version%";'
            log2 = execute_query(connection, query3).fetchall() 
            #these next statements format the error message so it is displayed properly
            for row in log:
                for col in row:
                    if isinstance(col, str):
                        for char in col:
                            if char == '"':
                                char = "'"
            flash('Incorrect Username/Password', 'danger')
            return render_template('login_misconfig.html', log=log, log2=log2)
    else:
        return render_template('login_misconfig.html')

##################################################################
#####          VULNERABILTY 4: BROKEN AUTHENTICATION        ######
##################################################################

# set a weak secret key
app.secret_key = "secretkey";

# loads python interpreter page
@app.route('/cookie_decoder')
def cookie_decoder():
    return render_template('cookie_decoder.html')

# login route which sets up a user session upon successful login
@app.route('/login_sessions', methods = ['POST', 'GET'])
def login_sessions():
    if request.method == 'POST':
        user = request.form['username']
        password = request.form['password']
        connection = connect_to_database()
        query = 'SELECT * FROM accounts WHERE user = %s AND password = %s'
        data = (user, password)
        userAccount = execute_query(connection, query, data).fetchall()
        # if user account exists create session data which can be accessed in other routes
        if userAccount:
            session['loggedin'] = True
            session['username'] = user
            session['password'] = password
            session['data'] = userAccount
            return render_template('account_sessions.html', user=userAccount)
        # if error in login
        else:
            flash('Incorrect Username/Password', 'danger')
            return render_template('login_sessions.html')
    else:
        return render_template('login_sessions.html')


# displays user's account page if they have a current session    
@app.route('/account_sessions/<user>', methods=['GET'])
def account_sessions(user): 
    # if a user is already logged in with a current session
    if not session.get('username') is None:    
        user = session.get('data')
        return render_template('account_sessions.html', user = user)
    # if not logged in redirect to login page
    else:
        flash('You are not logged in', 'danger')
        return render_template('login_sessions.html')

# ineffective log out route which does not remove session data
@app.route('/logout_sessions',  methods = ['POST'])
def logout_sessions():
   # Redirect to login_sessions page
   return redirect(url_for('login_sessions'))



if __name__ == "__main__":
    app.run()