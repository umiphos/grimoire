import MySQLdb,json
import time

from flask import Flask, render_template,request
app = Flask(__name__)

DB_HOST = '127.0.0.1' 
DB_USER = 'root' 
DB_PASS = 'pass' 
DB_NAME = 'Qamaleontis'

import requests
def cur():
	datos = [DB_HOST, DB_USER, DB_PASS, DB_NAME]
	conn = MySQLdb.connect(*datos) # Conectar a la base de datos
	cursor = conn.cursor()
	return cursor
#@app.route('/', methods=["GET", "POST"])
#def new():
while True:
	res = requests.get('http://192.168.1.174:5000/GetLastRecordsDict')
	#if res.ok:
	#print res.content#.json()
	#while True:
	print res.text
	time.sleep(2)
	#return "TEST"
	
	query=''
	tupples = json.loads(res.text)
	tim = time.strftime("%H:%M:%S")
	dat = time.strftime("%Y-%m-%d")
	myId = 1
	for x in range(len(tupples)):#este ciclo es para crear la query para MysQL
		#print "test"
		query=query+"(NULL,"+str(tupples[x]['sensor_number'])+','+str(myId)+','+tupples[x]['data']+',"'+tupples[x]['date']+'","'+tupples[x]['time']+'"),'
	
	query=query[:-1]
	print query
	cursor = cur()
	cursor.execute('INSERT INTO RECORDS (id_record,id_sensor,id_tower,data,date,time) values'+query)
	cursor.execute('commit')
	time.sleep(2)

if(__name__=="__main__"):
    app.run(debug=True, host='0.0.0.0',port=5001)
