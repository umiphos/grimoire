import MySQLdb,json
import time

from flask import Flask, render_template,request
app = Flask(__name__)

#DB_HOST = 'localhost'
#DB_USER = 'root'
#DB_PASS = 'pass'
#DB_NAME = 'FM4Demo'

#datos = [DB_HOST, DB_USER, DB_PASS, DB_NAME]
#conn = MySQLdb.connect(*datos) # Conectar a la base de datos


@app.route('/',methods=['GET','POST'])
def loginAdmin():
	if request.method == 'POST':
		user_name = request.form.get("user_name")
		password  = request.form.get("password")
		print user_name,password
		return render_template('register_volutario.html')
		#magic with the information login to database
	if request.method == 'GET':
		return render_template('index.html')

@app.route('/loginVolunteer',methods=['GET','POST'])
def loginVolunteer():
	if request.method == 'POST':
		user_name = request.form.get("user_name")
		password  = request.form.get("password")
		print user_name,password
		return render_template('register_volutario.html')
		#magic with the information login to database
	if request.method == 'GET':
		return render_template('index.html')


@app.route('/new_user',methods=['GET','POST'])
def new_user():
	if request.method == 'POST':
		user_name = request.form.get("user_name")
		password  = request.form.get("password")
		director_key = request.form.get("director_key")
		level = request.form.get("level")
		name = request.form.get("name")
		lastname = request.form.get("lastname")
		#magic with the information login to database
	if request.method == 'GET':
		return render_template('index.html')




if(__name__=="__main__"):
    app.run(debug=True, host='0.0.0.0')
