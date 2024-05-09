from flask import Flask,jsonify,request
import requests
app = Flask(__name__)


@app.route('/')
def home():
    return "Hello world"


@app.route("/postJson", methods=['POST'])
def postJson():
    data = request.json
    print(data)
    return data,200

@app.route("/postParam", methods=['POST'])
def postParam():
    my_param = request.args
    jsonify(my_param)
    print(my_param.to_dict())
    return my_param,200

@app.route("/postDataform", methods=['POST'])
def postDataform():
    data = request.form
    jsonify(data)
    print(data.to_dict())
    return data,200

@app.route("/postHeader", methods=['POST'])
def postHeader():
    data = request.headers
    print(data)
    return 'test',200

@app.route("/getJson", methods=['GET'])
def getJson():
    url = "https://jsonplaceholder.typicode.com/posts"
    test_data = requests.get(url).json()
    print(test_data)
    return test_data,200
    
if __name__ == "__main__":
    app.run(debug=True)