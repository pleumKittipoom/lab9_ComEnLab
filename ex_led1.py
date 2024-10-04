'''   https://code-maven.com/using-templates-in-flask  '''

from flask import Flask, render_template, request
 
app = Flask(__name__) 

@app.route("/")
def hello():
    return render_template('ex_led1.html')

@app.route("/<led>", methods=['POST'])
def led(led): 
    return f'{led.capitalize() } : '+ request.form['ledState']
    # return render_template('ex_led1.html', ledstate=request.form['ledState'])

if __name__ == "__main__": 
    app.run(debug=True, host='0.0.0.0')