import time
from flask import Flask, jsonify,Response,request,render_template
app = Flask(__name__)
################Classes


@app.route('/ex1',methods=['GET', 'POST'])
def ex1():
    if request.method == 'POST':
        return "We don't support POST method"
		
    if request.method == 'GET': 
        return render_template('ex1.html')
    return "Done"



@app.route('/ex2',methods=['GET', 'POST'])
def ex2():
    if request.method == 'POST':
        return "We don't support POST method"
		
    if request.method == 'GET': 
        return render_template('ex2.html')
    return "Done"

######################################

if(__name__=="__main__"):
    app.run(debug=True,host='0.0.0.0',port=5050)
