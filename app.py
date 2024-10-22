import base64
import time   
from flask import Flask, jsonify
from flask_cors import CORS  

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Utility function to encode image to Base64
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

GEN_IMAGE_PATH = 'img.png'

@app.route("/canary/storyboard/api", methods=['GET'])
def storyboard():

    gen_image_base64 = encode_image(GEN_IMAGE_PATH)   
    generated_date = time.strftime("%d-%m-%Y", time.localtime())  
    generated_time = time.strftime("%H:%M:%S", time.localtime())   
    prompt = "Generate an image of a person on a road."

    # Return both the message and the image in Base64 format
    return jsonify({    
        "prompt": prompt,   
        "generated_image": gen_image_base64,   
        "owner": "Shahin",  
        "date": generated_date,  
        "time": generated_time,  
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

## http://127.0.0.1:10000/canary/storyboard/api

 