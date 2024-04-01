from flask import Flask, render_template, request, redirect
import mysql.connector as conn

app = Flask(__name__)

# # MySQL configurations
mydb = conn.connect(host = 'localhost',user = 'root' )

# mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        # Fetch form data
        student_name = request.form['fname']
        father_name = request.form['lname']
        mother_name = request.form['gname']
        phone_number = request.form['kname']
        email = request.form['mname']
        date_of_birth = request.form['tname']
        address = request.form['aname']
        blood_group = request.form['bname']
        department = request.form['cname']
        course = request.form['dname'] 
        password = request.form['ename']
        # Save data to MySQL
        cur = mydb.cursor()
        cur.execute("INSERT INTO users (student_name, father_name, student_mother_name, phone_number , email, date_of_birth, address, blood_group, department, course, password) VALUES (%s, %s, %s,%d ,%s ,%s, %s, %s ,%s ,%s ,%s)", (student_name, father_name, mother_name, phone_number, email, date_of_birth ,address ,blood_group ,department ,course, password ))
        mydb.commit()
        cur.close()
        
        return redirect('/')
    else:
       return "Method Not Allowed", 405

if __name__ == '__main__':
    app.run(debug=True)