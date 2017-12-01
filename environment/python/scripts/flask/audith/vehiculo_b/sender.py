#!/usr/bin/python
#coding=utf-8
import json
import serial
import time
import shlex
import MySQLdb
import re
from random import randint

DB_HOST = '127.0.0.1' 
DB_USER = 'root' 
DB_PASS = 'pass' 
DB_NAME = 'Qamaleontis'

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
#!/usr/bin/python
#coding=utf-8


ttyUSB0 = serial.Serial(             
port='/dev/ttyUSB0',
baudrate = 9600,
parity=serial.PARITY_NONE,
stopbits=serial.STOPBITS_ONE,
bytesize=serial.EIGHTBITS,
timeout=1
)
def Select_Last_Current_Event():
	cursor = curDict()
	cursor.execute('CALL Select_Last_Current_Event()')
	num_fields = len(cursor.description)
	field_names = [i[0] for i in cursor.description]
	#print field_names
	return cursor.fetchall(),field_names

def cur():
	datos = [DB_HOST, DB_USER, DB_PASS, DB_NAME]
	conn = MySQLdb.connect(*datos) # Conectar a la base de datos
	cursor = conn.cursor()
	return cursor
while 1:

	
	try:
		ttyUSB0.write("GS")
		read=ttyUSB0.readline()
		print read
		if(read):
			query=''
			tupples = json.loads(read)
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
		
		#todo esto es despues de procesar lo del JSON
		rows,columns = list(Select_Last_Current_Event())
		decoded = json.dumps(rows)
		tupples=tupples = json.loads(decoded)
		
		#if(tupples[0]['active']==1):
		print "active"

		rows,columns = list(Select_Last_Current_Event())
		decoded = json.dumps(rows)
		print decoded
		ttyUSB0.write(str(decoded)+"\r")

			#result=cursor.execute("INSERT INTO RECORDS (id_record,id_sensor,id_tower,data,date,time) values"+query)
		time.sleep(3)#el final de este codigo
		decoded=''
	except:
		print read
		print "problemas de procesamiento"