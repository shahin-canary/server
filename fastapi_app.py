import os 
import torch 
import base64   
import uvicorn 
from PIL import Image
from io import BytesIO  
from pydantic import BaseModel 
from diffusers import DiffusionPipeline   
from fastapi import FastAPI, HTTPException 
from fastapi.responses import StreamingResponse



# Initialize the FastAPI app
app = FastAPI()

# Pydantic model to define the expected input data structure
class GenerateRequest(BaseModel):
    prompt: str

# POST endpoint to generate an image
@app.post("/generate/")
def generate_image(request: GenerateRequest):
    try:
        # pipe = DiffusionPipeline.from_pretrained("stabilityai/stable-diffusion-xl-base-1.0", torch_dtype=torch.float16, use_safetensors=True, variant="fp16")
        # pipe.to("cuda" if torch.cuda.is_available() else "cpu")
        # pipe.load_lora_weights("models/charctr_bwy.safetensors")

        # Get prompt from request data
        prompt = request.prompt or "sks charctr_kyz standing with a whiteboard that reads: 'Input prompt is an empty string...'"
        print("prompt: ", prompt)
         
        image = Image.new('RGB', (200, 200), color=(150, 150, 250)) 
        # Save the image to a BytesIO buffer
        img_io = BytesIO()
        image.save(img_io, 'PNG')
        img_io.seek(0)

        # Return the image from the buffer as a StreamingResponse
        return StreamingResponse(img_io, media_type="image/png")
    
    except Exception as e:
        # Raise a HTTP 500 error with the error message if something goes wrong
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    uvicorn.run(app, host="0.0.0.0", port=port)






    