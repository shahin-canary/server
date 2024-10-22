from flask import Flask, jsonify
from flask_cors import CORS  # Import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route("/api/storyboard", methods=['GET'])
def storyboard():
    return jsonify({"message": "shahin here"})

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