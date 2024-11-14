# import base64
# import time   
# from flask import Flask, jsonify
# from flask_cors import CORS  

# app = Flask(__name__)
# CORS(app) 


# # fetch_from_api


# # process prompt
# # prompt = "sketch of [V] chrctr_ijk"





# # inference? 

  
# # Utility function to encode image to Base64
# def encode_image(image_path):
#     with open(image_path, "rb") as image_file:
#         return base64.b64encode(image_file.read()).decode('utf-8')

# GEN_IMAGE_PATH = 'F:\canary\server\img.png'
# gen_image_base64 = encode_image(GEN_IMAGE_PATH)   

# @app.route("/canary/storyboard/image/api", methods=['GET', 'POST'])
# def storyboard():
#     if flask.request.method == 'POST':
#         data = flask.request.get_json()
#         if not data or not 'prompt' in data:
#             return jsonify({"error": "Invalid input"}), 400
#         prompt = data['prompt']
#     else:
#         prompt = "Generate an image of a person on a road."

#     generated_date = time.strftime("%d-%m-%Y", time.localtime())  
#     generated_time = time.strftime("%H:%M:%S", time.localtime())   

#     # Return both the message and the image in Base64 format
#     return jsonify({    
#         "prompt": prompt,   
#         "generated_image": gen_image_base64,    
#         "date": generated_date,  
#         "time": generated_time,  
#     })

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=10000)

# ## http://127.0.0.1:10000/canary/storyboard/image/api
# ## https://server-1-cak2.onrender.com/canary/storyboard/image/api



# import base64
# import time
# from flask import Flask, jsonify, request  # Import 'request' directly
# from flask_cors import CORS  

# app = Flask(__name__)
# CORS(app)

# # Utility function to encode image to Base64
# def encode_image(image_path):
#     try:
#         with open(image_path, "rb") as image_file:
#             return base64.b64encode(image_file.read()).decode('utf-8')
#     except FileNotFoundError:
#         return None  # Handle missing file by returning None or an error message

# GEN_IMAGE_PATH = 'F:\\canary\\server\\img.png'  # Ensure path uses double backslashes for Windows
# gen_image_base64 = encode_image(GEN_IMAGE_PATH)
# if gen_image_base64 is None:
#     print("Error: Image file not found at path:", GEN_IMAGE_PATH)

# @app.route("/canary/storyboard/image/api", methods=['GET', 'POST'])
# def storyboard():
#     if request.method == 'POST':  # Using 'request' directly
#         data = request.get_json()
#         if not data or 'prompt' not in data:
#             return jsonify({"error": "Invalid input"}), 400
#         prompt = data['prompt']
#     else:
#         prompt = "Generate an image of a person on a road."

#     generated_date = time.strftime("%d-%m-%Y", time.localtime())  
#     generated_time = time.strftime("%H:%M:%S", time.localtime())   

#     # Return both the message and the image in Base64 format
#     return jsonify({    
#         "prompt": prompt,   
#         "generated_image": gen_image_base64 if gen_image_base64 else "Image not found",    
#         "date": generated_date,  
#         "time": generated_time,  
#     })

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=10000)


from flask import Flask, request, jsonify, send_file
from diffusers import DiffusionPipeline
import torch
import os

app = Flask(__name__)

# Load the pipeline with model weights
pipe = DiffusionPipeline.from_pretrained(
    "stabilityai/stable-diffusion-xl-base-1.0",
    use_safetensors=True
)

# Ensure you're using CPU or GPU correctly
device = "cuda" if torch.cuda.is_available() else "cpu"
pipe.to(device)

# Correct path to LoRA weights
pipe.load_lora_weights("models/charctr_bwy.safetensors")


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "API is running"}), 200

@app.route("/generate", methods=["POST"])
def generate_image():
    try:
        data = request.get_json()
        prompt = data.get("prompt", "An astronaut riding a green horse")

        # Generate the image
        image = pipe(prompt=prompt,
        num_inference_steps=1,
        ).images[0]
        image.save("generated_img.png")

        # Return the generated image as a response
        return send_file("generated_img.png", mimetype="image/png"), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
