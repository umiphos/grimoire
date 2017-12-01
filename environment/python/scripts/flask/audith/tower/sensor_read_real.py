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

datos = [DB_HOST, DB_USER, DB_PASS, DB_NAME]
conn = MySQLdb.connect(*datos) # Conectar a la base de datos
cursor = conn.cursor()

rand=randint(0,1)

ttyS0 = serial.Serial(             
port='/dev/ttyS0',
baudrate = 38400,
parity=serial.PARITY_NONE,
stopbits=serial.STOPBITS_ONE,
bytesize=serial.EIGHTBITS,
timeout=1
)
while 1:
	try:
		s2=str(ttyS0.readline())
		if s2:
			print s2
			procs = s2.split(",")
			
			#inicio sensores
			values = []
			query = ""
			sensors=0
			for x in range(len(procs)):
				if(x==0):
					if (procs[0]=="0R0"):
						sensors = 0
					if (procs[0]=="0R1"):
						sensors = 100
				else:
					level = ''.join(procs[x]).split("=")
					values.append(level[1].strip("\r\n"))
			#print values
			
			listS = re.sub("[a-z|A-Z]","",str(values))#aqui tenemos la lista pero es un string bien gandalla
			tim = time.strftime("%H:%M:%S")
			dat = time.strftime("%Y-%m-%d")	 
			myId = 1
			
			listX = listS.translate(None,"[]'' ").split(",")#convertimos en objetos mas sensillos de manejar con este translate
			
			for x in range(len(listX)):#este ciclo es para crear la query para MysQL
				query=query+"("+"NULL"+","+str(x+sensors)+","+str(myId)+","+str(listX[x])+","+"\""+str(dat)+"\""+","+"\""+str(tim)+"\""+"),"
			query=query[:-1]
			#print query
			
			result=cursor.execute("INSERT INTO RECORDS (id_record,id_sensor,id_tower,data,date,time) values"+query)
			conn.commit()
	except:
		print s2
		#print "problemas de procesamiento"