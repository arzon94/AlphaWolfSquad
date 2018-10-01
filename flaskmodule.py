from flask import Flask, jsonify, render_template, request
# from yourmodule import function_that_return_xml
import getsentiment 
app = Flask(__name__)

@app.route('/_add_numbers')
def add_numbers():
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    return jsonify(result=a + b)

@app.route('/_get_sentiment')
def _get_sentiment():
    scale = request.args.get('scale', '30min', type=str)
    result = getsentiment.bitcoin(scale)
    print(result)
    return jsonify(result=result)

@app.route('/')
def index():
    return render_template('index.html')

# @app.route("/")
# def hello():
#     # xml = function_that_return_xml()
#     # make fancy operations if you want
#     return 'hello'

if __name__ == "__main__":
    app.run()