from flask import Flask, request, jsonify
import requests
from flask_cors import CORS


app = Flask(__name__)

@app.route('/api', methods=['POST'])
def api():
    data = request.get_json()
    datos = "secret="+data['secret']+"&response="+data['response']
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    response = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data, headers=headers)
    return jsonify(response.json())

if __name__ == '__main__':
    app.run()
