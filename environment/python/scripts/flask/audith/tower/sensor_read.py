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

rand=0#eliminar esto una vez que existan los sensores
if (rand == 0):
	s2 = "0R0,Dn=0D,Dm=1D,Dx=2D,Sn=3.0M,Sm=4.0M,Sx=5.0M,Rc=6.00M,Rd=7s,Ri=8.0M,Hc=9.0M,Hd=10s,Hi=11.0M,Rp=12.0M,Hp=13.0M,Th=14.0C,Vh=15.0N,Vs=16.0V"
"""this comment"""
if (rand==1):
	s2 = "0R1,Pr=0.0Pa,Tp=36C"
if s2:
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
			print sensors
		else:
			level = ''.join(procs[x]).split("=")
			values.append(level[1])
	listS = re.sub("[a-z|A-Z]","",str(values))#aqui tenemos la lista pero es un string bien gandalla
	tim = time.strftime("%H:%M:%S")
	dat = time.strftime("%Y-%m-%d")	 
	myId = 1
	listX = listS.translate(None,"[]'' ").split(",")#convertimos en objetos mas sensillos de manejar con este translate
	print listX
	
	
	for x in range(len(listX)):#este ciclo es para crear la query para MysQL
		query=query+"("+"NULL"+","+str(x+sensors)+","+str(myId)+","+str(listX[x])+","+"\""+str(dat)+"\""+","+"\""+str(tim)+"\""+"),"
	query=query[:-1]
	print query
	
	result=cursor.execute("INSERT INTO RECORDS (id_record,id_sensor,id_tower,data,date,time) values"+query)
	
	conn.commit()
	cursor.close()