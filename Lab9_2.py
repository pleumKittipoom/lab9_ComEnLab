from flask import Flask 
  
app = Flask(__name__) 

@app.route("/hello") 
def hello(): 
    return "Hello World CPE1 !!!"

@app.route("/cpe") 
def cpe(): 
    return "<h1><i>Hello CPE2 !!!</i></h1>"   

@app.route("/") 
def index(): 
    return "สวัสดีชาวโลก Lab 9_2"
  
if __name__ == "__main__": 
    app.run(debug=True, host='0.0.0.0')