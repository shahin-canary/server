from flask import Flask, render_template
import base64

app = Flask(__name__)

# Utility function to encode image to Base64
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')


@app.route('/')
def storyboard():
    # Encode the image
    image_base64 = encode_image("img.jpg")  # Replace with your image path
    # Pass the base64 string to the HTML template
    return render_template('storyboard.html', image_data=image_base64)


if __name__ == '__main__':
    app.run(debug=True)
