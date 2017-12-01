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
def Select_Last_Sensors_Dict():
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

def cur():
	datos = [DB_HOST, DB_USER, DB_PASS, DB_NAME]
	conn = MySQLdb.connect(*datos) # Conectar a la base de datos
	cursor = conn.cursor()
	return cursor

ttyUSB0 = serial.Serial(             
port='/dev/ttyUSB0',
baudrate = 9600,
parity=serial.PARITY_NONE,
stopbits=serial.STOPBITS_ONE,
bytesize=serial.EIGHTBITS,
timeout=1
)



def Update_Current_Event(latitude,longitude,category,tim,dat):
	cursor = cur()
	cursor.callproc('Update_Current_Event',(latitude,longitude,category,tim,dat))
	cursor.execute('commit;')
	print "Done"
while True:

	try:
		read=ttyUSB0.readline()
		if(read):
			tupples = json.loads(read)
			try:
				if(tupples[0]['category']=="Normal" or tupples[0]['category']=="Lento" or tupples[0]['category']=="Congestionado" or tupples[0]['category']=="Detenido"):
					valores = json.loads(read)
					cursor = cur()
					Update_Current_Event(valores[0]['e_lat'],valores[0]['e_lon'],valores[0]['category'],valores[0]['time'],valores[0]['date'])
			except:
				print "There was no package for Alert"
	except:
		try:
			if(read=="GS"):
				print read
				ttyUSB0.write( Select_Last_Sensors_Dict()+"\n")
		except:
			print "There was a problem with the sensors request"
		


