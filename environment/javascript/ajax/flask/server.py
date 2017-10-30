import time
from flask import Flask, jsonify,Response,request,render_template
app = Flask(__name__)
################Classes


@app.route('/',methods=['GET', 'POST'])
def Configurate():
    if request.method == 'POST':
        return "We don't support POST method"
		
    if request.method == 'GET': 
        return render_template('index.html')
    return "Done"

######################################

if(__name__=="__main__"):
    app.run(debug=True,host='0.0.0.0',port=5050)
