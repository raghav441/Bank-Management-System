from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# Function to get database connection
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="password here",  # <-- DO NOT FORGET TO ADD YOUR PASSWORD HERE
        database="bankdb"
    )

@app.route('/')
def form():
    # Renders the empty form initially
    return render_template('form.html')

@app.route('/insert', methods=['POST'])
def insert():
    # Grab data from the fancy form
    acc_no = request.form['acc_no']
    name = request.form['name']
    balance = request.form['balance']
    
    try:
        # Connect, insert, and close
        db = get_db_connection()
        cursor = db.cursor()
        
        sql = "INSERT INTO account (acc_no, name, balance) VALUES (%s, %s, %s)"
        values = (acc_no, name, balance)
        
        cursor.execute(sql, values)
        db.commit()
        
        cursor.close()
        db.close()
        
        # Send a success message back to the original page
        return render_template('form.html', success_message="Account successfully added!")
        
    except mysql.connector.Error as err:
        # If there's an error (like a duplicate account number), show it on the page safely
        return render_template('form.html', error_message=f"Database Error: {err.msg}")

if __name__ == '__main__':
    app.run(debug=True, port=3000)