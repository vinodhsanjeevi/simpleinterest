from flask import Flask, jsonify, request
app = Flask(__name__)
information = {
    "Amount": 1000,
    "rate": 5,
    "time": 2
    }
@app.route('/whatisthis')
def find():
    return "this is for calculate simple interest by using flask..."
@app.route('/hi')
def hello():
    queryparam = request.args.get('queryparam')
    if queryparam == "yes":
        return jsonify({ "Output":(information['Amount'] * information['rate'] * information['time'])/100 })
    else:
        return "sorry"
app.run(port = 5000)
