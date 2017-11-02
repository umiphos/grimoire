import Tkinter as Tk
import MySQLdb

DB_HOST = '127.0.0.1' 
DB_USER = 'root' 
DB_PASS = '' 
DB_NAME = 'test'
""" conexion para linux
datos = [DB_HOST, DB_USER, DB_PASS, DB_NAME] 
conn = MySQLdb.connect(*datos) # Conectar a la base de datos 
cursor = conn.cursor()         # Crear un cursor 
"""


datos = [DB_HOST, DB_USER, DB_PASS, DB_NAME] 
conn = MySQLdb.connect(host=DB_HOST, port=3306, user=DB_USER, passwd=DB_PASS, db=DB_NAME) # Conectar a la base de datos 
cursor = conn.cursor()         # Crear un cursor 



########################################################################
class Sensores(Tk.Toplevel):
	""""""
	#----------------------------------------------------------------------
	def __init__(self):
		"""Constructor"""
		Tk.Toplevel.__init__(self)
		self.geometry("400x300")
		self.title("Sensores")
########################################################################
class Actuadores(Tk.Toplevel):
	#----------------------------------------------------------------------
	def __init__(self):
		"""Constructor"""
		Tk.Toplevel.__init__(self)
		self.geometry("400x300")
		self.title("Actuadores")

########################################################################
class Password(Tk.Toplevel):
    """"""
 
    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        Tk.Toplevel.__init__(self)
        self.geometry("400x300")
        self.title("Actualizar contrasena")

########################################################################

class MyApp(object):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, parent):
		"""Constructor"""
		self.root = parent
		self.root.title("Main frame")
		self.frame = Tk.Frame(parent)
		self.frame.pack()
		sensores= Tk.Button(self.frame, text="Sensores", command=self.sensoresFrame)
		sensores.pack()
		
		
		actuadores= Tk.Button(self.frame, text="Actuadores", command=self.ActuadoresFrame)
		actuadores.pack()
		
		password= Tk.Button(self.frame, text="Actualizar password", command=self.PasswordFrame)
		password.pack()

################################################################################################################################################
#####################################################In here goes the frames of the code########################################################
	def sensoresFrame(self):
		self.hide()
		subFrame = Sensores()
		handler = lambda: self.CloseSensoresFrame(subFrame)
		btn = Tk.Button(subFrame, text="Back to main", command=handler)
		btn.pack()
		
	def ActuadoresFrame(self):
		self.hide()
		subFrame = Actuadores()
		handler = lambda: self.CloseActuadoresFrame(subFrame)
		btn = Tk.Button(subFrame, text="Back to main", command=handler)
		btn.pack()

	def PasswordFrame(self):
		self.hide()
		subFrame = Password()
		handler = lambda: self.ClosePasswordFrame(subFrame)
		btn = Tk.Button(subFrame, text="Back to main", command=handler)
		btn.pack()
################################################################################################################################################
################################################################################################################################################
################################################################################################################################################
################################################################################################################################################
######################################################In here stand the handlers of the code.###################################################
	def CloseSensoresFrame(self, Sensores):
		""""""
		Sensores.destroy()
		self.show()
		
	def CloseActuadoresFrame(self, Actuadores):
		""""""
		Actuadores.destroy()
		self.show()
	def ClosePasswordFrame(self, Password):
		""""""
		Password.destroy()
		self.show()		
		
################################################################################################################################################
################################################################################################################################################
	def show(self):
		""""""
		self.root.update()
		self.root.deiconify()		
#----------------------------------------------------------------------
	def hide(self):
		""""""
		self.root.withdraw()
#----------------------------------------------------------------------
################################################################################################################################################    
if __name__ == "__main__":
    root = Tk.Tk()
    root.geometry("800x600")
    app = MyApp(root)
    root.mainloop()