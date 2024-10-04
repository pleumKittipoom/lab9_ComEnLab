from flask import Flask, render_template
 
app = Flask(__name__) 

@app.route('/hello/<name>')
def index(name): 
   title = 'lab 9_7 CPE 2 ---'
   return render_template('hello.html', name=name, title=title)
    
if __name__ == "__main__": 
    app.run(debug=True, host='0.0.0.0')