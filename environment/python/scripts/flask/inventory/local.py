import MySQLdb,json
import time

from flask import Flask, render_template, request, redirect
app = Flask(__name__)

DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASS = 'pass'#thispassword for server
DB_NAME = 'FM4Demo'

########################################################################
@app.route('/',methods=['GET','POST'])
def loginAdmin():
    error = None
    if request.method == 'POST':
        print "Dentro de POST, login_admin"
        username = request.form['username']
        password = request.form['password']
        this = loginAdmin(username,password)
        if this==0:#si sale todo mal
            error = 'Login incorrecto...'
            return render_template('pages/login_admin.html',error=error)
        return redirect("/newAdmin",code=302)   
        #return render_template('pages/register/register_voluntario.html')
    if request.method == 'GET':
        print "Dentro de GET, login_admin"
        return render_template('pages/login_admin.html')
@app.route('/loginVolunteer',methods=['GET','POST'])
def loginVolunteer():
    error = None
    if request.method == 'POST':
        print "Dentro de POST, login_voluntario"
        username = request.form['username']
        password = request.form['password']
        this = loginVolunteer(username,password)
        if this==0:#si sale todo mal
            error = 'Login incorrecto...'
            return render_template('pages/login_voluntario.html',error=error)
        #return render_template('pages/register/register_voluntario.html')
        return redirect("/newAdmin",code=302)   
    if request.method == 'GET':
        print "Dentro de GET, login_voluntario"
        return render_template('pages/login_voluntario.html')

########################################################################
@app.route('/newAdmin',methods=['GET','POST'])#probado 
def newAdmin():
    error = None
    success = None
    if request.method == 'POST':
        #CALL InsertAdmin("user_name","pass","name","last_name","mail") 
        username = request.form['username']
        password = request.form['pass']
        name =  request.form['name']
        last_name = request.form['last_name']
        mail = request.form['mail']
        InsertNewAdmin(username,password,name,last_name,mail)
        success = "Usuario registrado"
        return render_template('pages/register/register_admin.html',success = success)
    if request.method == 'GET':
        return render_template('pages/register/register_admin.html')
@app.route('/newMigrant',methods=['GET','POST'])
def newMigrant():
    error = None
    success = None
    if request.method == 'POST':
        #CALL InsertMigrant("name","last_name","photo",1) 
        name = request.form['name']
        last_name = request.form['last_name']
        photo =  "img/fix.jpg"
        InsertMigrant(name, last_name, photo, 1)#se deja fijo, ya que aun no existen sesiones...con la sesion obtenemos el id de voluntario que ingreso al migrante.
        success = "Registro exitoso"
        return render_template('pages/register/register_migrant.html',success = success)
    if request.method == 'GET':
        return render_template('pages/register/register_migrant.html')
@app.route('/newVolunteer',methods=['GET','POST'])
def newVolunteer():
    error = None
    success = None
    if request.method == 'POST':
        #CALL InsertAdmin("user_name","pass","name","last_name","mail") 
        username = request.form['username']
        password = request.form['pass']
        name =  request.form['name']
        last_name = request.form['last_name']
        mail = request.form['mail']
        InsertVolunteer(username,password,name,last_name,mail)
        success = "Usuario registrado"
        return render_template('pages/register/register_admin.html',success = success)
    if request.method == 'GET':
        return render_template('pages/register/register_admin.html')


@app.route('/test',methods=['GET','POST'])
def test():
    #CALL InsertAdmin("user_name","pass","name","last_name","mail") 
    #CALL InsertMigrant("name","last_name","photo",1) 
    #CALL InsertVolunteer("user_name","pass","name","last_name","mail")
    InsertNewAdmin("user_name","pass","name","last_name","mail") 
    InsertMigrant("name","last_name","photo",1)
    InsertVolunteer("user_name","pass","name","last_name","mail")
    return "Hello"

#retornan 1 si es exitoso el login
#retornan 0 si no es exitoso el login
def loginAdmin(username,password):
    this=SelectLoginAdmin(username,password)
    print len(this)
    if(len(this)>=1):
        return 1
    return 0
def loginVolunteer(username,password):
    this=SelectLoginVolunteer(username,password)
    print len(this)
    if(len(this)>=1):
        return 1
    return 0
#################################Seccion de conexiones###################
def cur():
    datos = [DB_HOST, DB_USER, DB_PASS, DB_NAME]
    conn = MySQLdb.connect(*datos) # Conectar a la base de datos
    cursor = conn.cursor()
    return cursor

#######################Inserciones#########################
def InsertNewAdmin(var1,var2,var3,var4,var5):#validado en /test
    #CALL InsertAdmin("user_name","pass","name","last_name","mail") 
    cursor = cur()
    cursor.callproc("InsertAdmin",(var1,var2,var3,var4,var5))
    cursor.execute('commit;')
    return cursor.fetchall()
def InsertMigrant(var1,var2,var3,var4):#validado en /test
#CALL InsertMigrant("name","last_name","photo",1) 
    cursor = cur()
    cursor.callproc("InsertMigrant",(var1,var2,var3,var4))
    cursor.execute('commit;')
    return cursor.fetchall()    
def InsertVolunteer(var1,var2,var3,var4,var5):#validado en /test
#CALL InsertVolunteer("user_name","pass","name","last_name","mail");
    cursor = cur()
    cursor.callproc("InsertVolunteer",(var1,var2,var3,var4,var5))
    cursor.execute('commit;')
    return cursor.fetchall()
    
#######################Busquedas###########################
def SelectLoginAdmin(var1,var2):#validado en /test
    cursor = cur()
    cursor.callproc("LoginAdmin",(var1,var2))
    return cursor.fetchall()
def SelectLoginVolunteer(var1,var2):#validado en /test
    cursor = cur()
    cursor.callproc("LoginVolunteer",(var1,var2))
    return cursor.fetchall()
#################################Close
if(__name__=="__main__"):
    app.run(debug=True, host='0.0.0.0')
