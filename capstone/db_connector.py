import mysql.connector
import hashlib

def connect_to_database():
    '''
    connects to a database and returns a database objects
    '''
    db_connection = mysql.connector.connect(host='localhost', user='hawkesc', password='capstone2020', database='bank_app')
    return db_connection

def execute_query(db_connection = None, query = None, query_params = ()):
    '''
    executes a given SQL query on the given db connection and returns a Cursor object

    db_connection: a MySQLdb connection object created by connect_to_database()
    query: string containing SQL query

    returns: A Cursor object as specified at https://www.python.org/dev/peps/pep-0249/#cursor-objects.
    You need to run .fetchall() or .fetchone() on that object to actually acccess the results.

    '''

    if db_connection is None:
        print("No connection to the database found! Have you called connect_to_database() first?")
        return None

    if query is None or len(query.strip()) == 0:
        print("query is empty! Please pass a SQL query in query")
        return None

    print("Executing %s with %s" % (query, query_params));
    # Create a cursor to execute query. Why? Because apparently they optimize execution by retaining a reference according to PEP0249
    cursor = db_connection.cursor()

    '''
    params = tuple()
    #create a tuple of paramters to send with the query
    for q in query_params:
        params = params + (q)
    '''
    #TODO: Sanitize the query before executing it!!!
    cursor.execute(query, query_params)
    # this will actually commit any changes to the database. without this no
    # changes will be committed!
    #db_connection.commit();
    return cursor

def add_user(username, password, balance):
    connection = connect_to_database()

    query = 'INSERT INTO accounts(user, password, balance) VALUES(%s, %s, %s)'
    data = (username, password, balance)                  # convert hexadecimal to a string
    execute_query(connection, query, data)
    connection.commit()

    passwd = str.encode(password)                        # convert string to bytes
    encrypted_password0 = hashlib.md5(passwd)             # returns md5 hash
    encrypted_password = encrypted_password0.hexdigest()    # returns encoded data in hexadecimal format
    query1 = 'INSERT INTO accounts_md5(user, encrypted_password, balance) VALUES(%s, %s, %s)'
    data1 = (username, str(encrypted_password), balance)                  # convert hexadecimal to a string
    execute_query(connection, query1, data1)
    connection.commit()

    passwd = str.encode(password)                        # convert string to bytes
    encrypted_password0 = hashlib.sha256(passwd)          # returns sha-256 hash
    encrypted_password = encrypted_password0.hexdigest()    # returns encoded data in hexadecimal format 
    query2 = 'INSERT INTO accounts_sha256(user, encrypted_password, balance) VALUES(%s, %s, %s)'
    data2 = (username, str(encrypted_password), balance)                  # convert hexadecimal to a string
    execute_query(connection, query2, data2)
    connection.commit()
     
    connection.close() 
    return 


if __name__ == '__main__':
    print("Executing a sample query on the database using the credentials from db_credentials.py")
    db = connect_to_database()
    query = "SELECT * from accounts;"
    results = execute_query(db, query);
    print("Printing results of %s" % query)

    for r in results.fetchall():
        print(r)
