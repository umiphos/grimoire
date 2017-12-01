import MySQLdb
import serial
import time
from flask import Flask, jsonify,Response,request,render_template
app = Flask(__name__)
################Classes


@app.route('/Configurate',methods=['GET', 'POST'])
def Configurate():
	if request.method == 'POST':#significa que actualizaremos la base de datos
		lat = request.form.get("lat")
		lon = request.form.get("lon")
		tim= time.strftime("%H:%M:%S")
		dat= time.strftime("%Y-%m-%d")	 
		
		Update_Personal(lat,lon)
		return "Done"
		
	if request.method == 'GET':#significa que actualizaremos la base de datos
		return render_template('Configurate.html')

@app.route('/AlertON',methods=['GET', 'POST'])
def AlertON():
	if request.method == 'POST':#significa que actualizaremos la base de datos
		lat = request.form.get("lat")
		lon = request.form.get("lon")
		category = request.form.get("category")

		tim= time.strftime("%H:%M:%S")
		dat= time.strftime("%Y-%m-%d")

		CreateEvent(lat,lon,category,tim,dat)
		last = list(SelectLastEvent())
		UpdateCurrentEvent(lat,lon,category,tim,dat)
		return "Done"
	if request.method == 'GET':#significa que actualizaremos la base de datos
		return render_template('AlertON.html')
#####################End Of Classes

#########################ya existen, solo las usamos como clases
DB_HOST = '127.0.0.1'
DB_USER = 'root'
DB_PASS = 'pass'
DB_NAME = 'Qamaleontis'

def CreateEvent(lat,lon,category,tim,dat):
	cursor = cur()
	cursor.callproc('Create_Event',(lat,lon,category,tim,dat))
	cursor.execute('commit;')


def cur():
	datos = [DB_HOST, DB_USER, DB_PASS, DB_NAME]
	conn = MySQLdb.connect(*datos) # Conectar a la base de datos
	cursor = conn.cursor()
	return cursor		
	
def Update_Personal(lat,lon):
	cursor = cur()
	cursor.callproc('Update_Personal',(lat,lon))
	cursor.execute('commit;')#esta es la forma de hacer commit con MySQL

def SelectLastEvent():
	cursor = cur()
	cursor.execute('CALL Select_Last_Event()')
	return cursor.fetchall()
	
def UpdateCurrentEvent(lat,lon,category,tim,dat):	
	cursor = cur()
	cursor.callproc('Update_Current_Event',(lat,lon,category,tim,dat))
	cursor.execute('commit;')	
######################################

if(__name__=="__main__"):
    app.run(debug=True,host='0.0.0.0',port=5050,ssl_context=('/home/pi/area/Qamaleontis/certs/server.crt', '/home/pi/area/Qamaleontis/certs/server.key'))
