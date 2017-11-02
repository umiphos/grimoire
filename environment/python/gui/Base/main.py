import Tkinter as Tk
import MySQLdb

DB_HOST = '127.0.0.1' 
DB_USER = 'root' 
DB_PASS = '' 
DB_NAME = 'simade_locadb'
""" conexion para linux
datos = [DB_HOST, DB_USER, DB_PASS, DB_NAME] 
conn = MySQLdb.connect(*datos) # Conectar a la base de datos 
cursor = conn.cursor()         # Crear un cursor 
"""


datos = [DB_HOST, DB_USER, DB_PASS, DB_NAME] 
conn = MySQLdb.connect(host=DB_HOST, port=3306, user=DB_USER, passwd=DB_PASS, db=DB_NAME) # Conectar a la base de datos 
cursor = conn.cursor()         # Crear un cursor 
class MyApp(object):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, parent):
		"""Constructor"""
		self.root = parent
		self.root.title("Main frame")
		self.frame = Tk.Frame(parent)
		self.frame.pack()
		Actuador_I= Tk.Button(self.frame, text="LED ON", command=self.text)
		Actuador_I.pack()
	
	def text(Actuador_I):
		print("LED button pressed")
		if	(Actuador_I["text"]=="LED ON"):
			Actuador_I["text"] = "LED OFF"
		else:
			Actuador_I["text"] = "LED ON"

	def sensoresFrame():
		cursor.execute("UPDATE actuators SET from_app='1' WHERE id_actuator=1")
		cursor.execute("UPDATE actuators SET from_app='1' WHERE id_actuator=2")
		conn.commit()
		
		
	def ActuadoresFrame():
		cursor.execute("UPDATE actuators SET from_app='0' WHERE id_actuator=1")
		cursor.execute("UPDATE actuators SET from_app='0' WHERE id_actuator=2")
		conn.commit()
		
if __name__ == "__main__":
    root = Tk.Tk()
    root.geometry("800x600")
    app = MyApp(root)
    root.mainloop()	