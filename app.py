import base64
from flask import Flask, jsonify
from flask_cors import CORS  # Import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Utility function to encode image to Base64
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

@app.route("/api/storyboard", methods=['GET'])
def storyboard():
    # Encode the image
    image_base64 = encode_image("img.jpg")  # Update with your image path

    # Return both the message and the image in Base64 format
    return jsonify({
        "message": "shahin here",
        "generated_image": image_base64
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)




# '''
#         <html>
#             <head>
#                 <style>
#                     body {
#                         display: flex;
#                         justify-content: center;
#                         align-items: center;
#                         height: 100vh;
#                         background-color: #f0f0f0;
#                     }
#                     h1 {
#                         font-size: 72px; /* Big font size */
#                         color: #ff5733; /* Color of the text */
#                     }
#                 </style>
#             </head>
#             <body>
#                 <h1>Hello, World!</h1>
#             </body>
#         </html>
#     '''