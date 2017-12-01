import MySQLdb,json
import time

from flask import Flask, render_template,request
app = Flask(__name__)

DB_HOST = '127.0.0.1' 
DB_USER = 'root' 
DB_PASS = 'pass' 
DB_NAME = 'Qamaleontis'

def Update_Personal(lat,lon):
	cursor = cur()
	cursor.callproc('Update_Personal',(lat,lon))
	cursor.execute('commit;')#esta es la forma de hacer commit con MySQL
def Select_Personal_Info():
	cursor = cur()
	cursor.callproc('Select_Personal_Info')
	return cursor.fetchall()
def cur():
	datos = [DB_HOST, DB_USER, DB_PASS, DB_NAME]
	conn = MySQLdb.connect(*datos) # Conectar a la base de datos
	cursor = conn.cursor()
	return cursor	
def degrees_to_cardinal(d):
	dirs = ["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE","S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"]
	#ix = int((d + 11.25)/22.5)
	ix = int((d)/22.5) 
	return dirs[ix % 16]
def curDict():
	datos = [DB_HOST, DB_USER, DB_PASS, DB_NAME]
	conn = MySQLdb.connect(*datos) # Conectar a la base de datos
	cursor = conn.cursor(MySQLdb.cursors.DictCursor)
	return cursor	
	
#GetLastRecords
def sensores():
	cursor = cur()
	cursor.execute('CALL Select_Last_Sensors()')
	return cursor.fetchall()
def carmen(valores):
	tower_id=1
	time="rait now"
	carmen='{'+'"id_tower":'+str(tower_id)+',"Sensors":['
	for x in valores:
		carmen=carmen+'{'+\
		'"id":'+str(x[0])+','+\
		'"id_tower":'+str(x[1])+','+\
		'"data":'+'"'+str(x[2])+'"'+','+\
		'"date":'+'"'+str(x[3])+'"'+','+\
		'"time":'+'"'+str(x[4])+'"'+','+\
		'"sensor_name":'+'"'+str(x[5])+'"'+','+\
		'"description":'+'"'+str(x[6])+'"'+','+\
		'"sensor_number":'+'"'+str(x[7])+'"'+'}'+','
		if x[7]==1:
			degree=degrees_to_cardinal(int(x[2]))
		if x[7]==4:
			wind=x[2]
		if x[7]==8:
			rain=x[2]
	state=status(wind,rain)
	print "wind:",wind
	print "rain:",rain
	print state
	gps=getGPS()

	carmen=carmen[:-1]
	carmen=carmen+'],'+'"status":'+'"'+state+'"'+','+'"GPS":{'+'"lat":'+'"'+gps[1]+'"'+','+'"long":'+'"'+gps[2]+'"'+'}'+','+'"wind":'+'"'+str(degree)+'"'+'}'
	return carmen
def getGPS():
	rows=personalInfo()
	return rows
def personalInfo():
	cursor = cur()
	cursor.execute('CALL Select_Personal_Info()')
	return cursor.fetchone()
def status(wind, rain):
	if float(wind)<=15.0:
		if float(rain)==0.0:
			state="Despejado"
		if float(rain)>0.0:
			state="Lluvia"
	if float(wind)>15.0:
		if float(rain)==0.0:
			state="Nublado"
		if float(rain) > 0.0:
			state="Tormenta"
	return state
#GetLastRecords
#Routes
@app.route('/GetLastRecords')
def GetLastRecords():
	valores=sensores()
	jayson=carmen(valores)
	
	decoded = json.dumps(jayson)
	#print decoded
	#print jayson
	return jayson

@app.route('/RecoveryEvent')
def RecoveryEvent():
	cursor = cur()
	cursor.execute('UPDATE `CURRENT_EVENT` SET `e_lat`=0,`e_lon`=0 WHERE 1')
#UPDATE `CURRENT_EVENT` SET `e_lat`=0,`e_lon`=0 WHERE 1	
	
@app.route('/AlertON',methods=['GET', 'POST'])
def AlertON():
	if request.method == 'POST':#significa que actualizaremos la base de datos
		lat = request.form.get("lat")
		lon = request.form.get("lon")
		category = request.form.get("category")

		tim= time.strftime("%H:%M:%S")
		dat= time.strftime("%Y-%m-%d")

		UpdateCurrentEvent(lat,lon,category,tim,dat)
		return "Done"
	if request.method == 'GET':#significa que actualizaremos la base de datos
		rows,columns = list(Select_Last_Current_Event())
		decoded = json.dumps(rows)
		return decoded

#ocupan curDict
def SelectLastEvent():
	cursor = curDict()
	cursor.execute('CALL Select_Last_Event()')
	num_fields = len(cursor.description)
	field_names = [i[0] for i in cursor.description]
	#print field_names
	return cursor.fetchall(),field_names
#################################################################################################
#############################TEST FUCKING AREA!!!################################################

@app.route('/GetLastRecordsDict')
def GetLastRecordsDict():
	rows,columns = list(Select_Last_Sensors())
	decoded = json.dumps(rows)
	#print decoded
	
	return decoded
def Select_Last_Sensors():
	cursor = curDict()
	cursor.execute('CALL Select_Last_Sensors()')
	num_fields = len(cursor.description)
	field_names = [i[0] for i in cursor.description]
	#print field_names
	return cursor.fetchall(),field_names
def cur():
	datos = [DB_HOST, DB_USER, DB_PASS, DB_NAME]
	conn = MySQLdb.connect(*datos) # Conectar a la base de datos
	cursor = conn.cursor()
	return cursor
def UpdateCurrentEvent(lat,lon,category,tim,dat):	
	cursor = cur()
	cursor.callproc('Update_Current_Event',(lat,lon,category,tim,dat))
	cursor.execute('commit;')
def Select_Last_Current_Event():
	cursor = curDict()
	cursor.execute('CALL Select_Last_Current_Event()')
	num_fields = len(cursor.description)
	field_names = [i[0] for i in cursor.description]
	#print field_names
	return cursor.fetchall(),field_names
def curDict():
	datos = [DB_HOST, DB_USER, DB_PASS, DB_NAME]
	conn = MySQLdb.connect(*datos) # Conectar a la base de datos
	cursor = conn.cursor(MySQLdb.cursors.DictCursor)
	return cursor		

if(__name__=="__main__"):
    app.run(debug=True, host='0.0.0.0')


