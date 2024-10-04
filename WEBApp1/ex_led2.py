'''   https://code-maven.com/using-templates-in-flask  '''

from flask import Flask, render_template, request
 
app = Flask(__name__) 

@app.route('/')
def hello():
    return render_template('ex_led2.html')

@app.route('/led/<id>', methods=['POST'])
def led(id): 
    # if id=='led1': 
    #     return f'{id.capitalize() } : ' + request.form['led1State']
    # elif id=='led2':
    #     return f'{id.capitalize() } : ' + request.form['led2State']

    if id=='1': 
        return render_template('ex_led2.html', ledstate=request.form['led1State'], id='1')
    elif id=='2': 
        return render_template('ex_led2.html', ledstate=request.form['led2State'], id='2')

  #  print("");

if __name__ == "__main__": 
    app.run(debug=True, host='0.0.0.0')