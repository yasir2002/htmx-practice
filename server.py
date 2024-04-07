from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "http://127.0.0.1:5500"}})

@app.route('/api/data')
def get_data():
    data = "Hello from the server!"
    response = jsonify(data=data)
    response.headers.add("Access-Control-Allow-Origin", "http://127.0.0.1:5500")
    return response

if __name__ == '__main__':
    app.run(debug=True, port=5000)
