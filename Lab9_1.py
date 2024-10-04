from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
     a = 'CPE'
     return f'Hello world {a}'

if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0')
    app.run(debug=True, port=80, host='0.0.0.0')