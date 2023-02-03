from flask import Flask, request, jsonify
import requests
from flask_cors import CORS, cross_origin


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/api', methods=['POST'])
@cross_origin()
def api():
    data = request.get_json()
    datos = "secret="+data['secret']+"&response="+data['response']
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    response = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data, headers=headers)
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(port=5000, debug=True)
