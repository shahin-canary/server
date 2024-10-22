from flask import Flask

app = Flask(__name__)

@app.route("/api/storyboard")
def hello():
    return '''
        <html>
            <head>
                <style>
                    body {
                        display: flex;
                        justify-content: center;
                        align-items: center;
                        height: 100vh;
                        background-color: #f0f0f0;
                    }
                    h1 {
                        font-size: 72px; /* Big font size */
                        color: #ff5733; /* Color of the text */
                    }
                </style>
            </head>
            <body>
                <h1>Hello, World!</h1>
            </body>
        </html>
    '''

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)  # Only for local development
 