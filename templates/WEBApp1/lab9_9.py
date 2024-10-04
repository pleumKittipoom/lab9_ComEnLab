'''   https://code-maven.com/using-templates-in-flask  '''

from flask import Flask, render_template, request
 
app = Flask(__name__) 

@app.route("/")
def hello():
    return render_template('echo.html')

@app.route("/echo", methods=['POST'])
def echo(): 
    return "You said: " + request.form['text1']

if __name__ == "__main__": 
    app.run(debug=True, host='0.0.0.0')