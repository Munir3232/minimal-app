from flask import Flask


app = Flask(__name__)

# enable debugging mode
app.config["DEBUG"] = True



@app.route('/')
def hello():
     return 'hello'

if __name__=='__main__':
     app.run(debug=True)