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
    datos = "secret=6LcqoU0kAAAAALRhxRDXBCtwGTc6E-ezB5uAQO0O"+"&response="+data['response']
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    response = requests.post('https://www.google.com/recaptcha/api/siteverify', data=datos, headers=headers)
    respuesta = response.json()
    print("Respuesta: " + str(respuesta['success']))
    
    if respuesta['success'] == True:
        return jsonify({'success': True})
    else:
        print("Error:" + str(respuesta['error-codes']))
        return jsonify({'success': False})

if __name__ == '__main__':
    app.run(port=5000, debug=True)
