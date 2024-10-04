from flask import Flask 
  
app = Flask(__name__) 

@app.route('/post/<int:id>') 
def show_post(id): 
    return f'This post has the id {id}'
  
@app.route('/user/<username>') 
def show_user(username): 
    return f'Hello {username} !'

@app.route("/hello") 
def hello(): 
    return "Hello World Route!!!"
    
'''
@app.route("/") 
def index(): 
    return "สวัสดีชาวโลก Lab 9_2"'''



if __name__ == "__main__": 
    app.run(debug=True, host='0.0.0.0')