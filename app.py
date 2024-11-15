import base64 
from flask_cors import CORS  
from flask import Flask, request, jsonify, send_file
from diffusers import DiffusionPipeline
import torch
import os
from io import BytesIO
from PIL import Image


app = Flask(__name__)
 

 
@app.route("/generate", methods=["POST"])
def generate_image():
    try:

        pipe = DiffusionPipeline.from_pretrained("stabilityai/stable-diffusion-xl-base-1.0", torch_dtype=torch.float16, use_safetensors=True, variant="fp16") 
        pipe.to("cuda" if torch.cuda.is_available() else "cpu") 
        pipe.load_lora_weights("models/charctr_bwy.safetensors")


        data = request.get_json()
        prompt = data.get("prompt", "An astronaut riding a green horse")
 
        # image = pipe(prompt=prompt, num_inference_steps=50).images[0]
        image = Image.new('RGB', (200, 200), color=(150, 150, 250))

        # Save the image to a BytesIO buffer
        img_io = BytesIO()
        image.save(img_io, 'PNG')
        img_io.seek(0)

        # Return the image from the buffer
        return send_file(img_io, mimetype="image/png")
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)