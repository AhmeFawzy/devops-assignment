from flask import Flask, jsonify
import random
import string

app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def hello():
    return "hello", 200

@app.route('/random', methods=['GET'])
def random_string():
    result = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    return jsonify({"random_string": result}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)