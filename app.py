from waitress import serve
from flask import Flask, jsonify
import base64
import os

app = Flask(__name__)

@app.route('/image', methods=['GET'])
def get_image():
    with open('img.jpg', 'rb') as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    return jsonify({"image": encoded_string})

if __name__ == "__main__":
    serve(app, host='0.0.0.0', port=int(os.environ.get('PORT', 3000)))
