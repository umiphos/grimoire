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
while 1:
	rows,columns = list(Select_Last_Current_Event())
	decoded = json.dumps(rows)
	print decoded
	time.sleep(2)
	ttyUSB0.write(str(decoded)+"\r")
