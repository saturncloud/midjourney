from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware

from midjourney.model import model


app = FastAPI()

# Add CORS middleware to allow cross-origin requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)
model.load_model()
    
@app.get("/")
def index():
    return {"message": "Welcome to the app"}


@app.post('/generate_image')
def generate_image(prompt: str):
    if not prompt:
        return {"error": "Please provide a prompt"}
    filepath = model.generate_image2(prompt)
    return FileResponse(filepath, media_type='image/png')


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)