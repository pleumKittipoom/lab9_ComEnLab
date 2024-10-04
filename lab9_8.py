from flask import Flask, render_template
 
app = Flask(__name__) 

@app.route('/result')
def result(): 
   score = {'Eng': 75, 'Cal': 50, 'Phy': 80}
   drink = [
       {'name': 'Chocolate', 'price': 75},
       {'name': 'Coffee', 'price':80}
   ]

   return render_template('result.html', result=score, drink=drink)
    
if __name__ == "__main__": 
    app.run(debug=True, host='0.0.0.0')