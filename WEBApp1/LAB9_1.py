from flask import Flask 
  
app = Flask(__name__) 


@app.route('/<opt>/<a>/<b>') 
def opt(opt,a,b): 
    if(opt == "add"):
      ans = float(a)+float(b)
      return f'<h3>{a} + {b} = {ans}</h3>'
    
    elif(opt == "sub"):
      ans = float(a)-float(b)
      return f'<h3>{a} - {b} = {ans}</h3>'
    
    elif(opt == "mul"):
      ans = float(a)*float(b)
      return f'<h3>{a} * {b} = {ans}</h3>'
    
    elif(opt == "div"):
      ans = float(a)/float(b)
      return f'<h3>{a} / {b} = {ans}</h3>'



@app.route('/')
def index():
    return 'Lab 9_4'
    
  
if __name__ == "__main__": 
    app.run(debug=True, host='0.0.0.0')