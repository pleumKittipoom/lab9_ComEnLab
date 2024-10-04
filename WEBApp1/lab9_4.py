from flask import Flask 
  
app = Flask(__name__) 


@app.route('/add/<a>/<b>') 
def add(a,b): 
    ans = float(a)+float(b)
    return f'<h3>{a} + {b} = {ans}</h3>'

@app.route('/')
def index():
    return 'Lab 9_4'
    
  
if __name__ == "__main__": 
    app.run(debug=True, host='0.0.0.0')