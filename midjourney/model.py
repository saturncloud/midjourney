from os.path import join

from diffusers import StableDiffusionPipeline, DPMSolverMultistepScheduler
import torch
import numpy as np
from PIL import Image
import os
import io


directory = "/tmp/generatedimages"
if not os.path.exists(directory):
    os.makedirs(directory)


class Model():
    def __init__(self, model_name, device):
        self.device=device
        self.model_id = model_name
        self.pipe = None

    def load_model(self):
        if self.pipe is None:
            dpm = DPMSolverMultistepScheduler.from_pretrained(join(MODEL_PATH, "dpm"))
            pipe = StableDiffusionPipeline.from_pretrained(join(MODEL_PATH, "pipe"))
            pipe = pipe.to(self.device)
            pipe.enable_attention_slicing()
            self.pipe = pipe
        return self.pipe
    
    def generate_image(self, prompt):
        image = self.pipe(prompt).images[0]
        image = np.asarray(image)
        im = Image.fromarray(image)
        filename = f"{prompt}.png"
        filepath = os.path.join(directory, filename)
        im.save(filepath)
        return filepath

    def generate_image2(self, prompt, filepath=None):
        image = self.pipe(prompt).images[0]
        img_bytes = io.BytesIO()
        image.save(img_bytes, format='PNG')
        img_bytes.seek(0)
        if filepath is None:
            filename = f"{prompt}.png"
            filepath = os.path.join(directory, filename)
        with open(filepath, 'wb') as f:
            f.write(img_bytes.read())
        return filepath

    
model_name = os.getenv("MODEL_NAME")
device = os.getenv("DEVICE")
MODEL_PATH = os.getenv("MODEL_PATH", "/home/jovyan/shared/emeka/midjourney/pretrained")
model = Model(model_name, device)


def save_model():
    dpm = DPMSolverMultistepScheduler.from_pretrained(model_name, subfolder="scheduler")
    dpm.save_pretrained(join(MODEL_PATH, "dpm"))
    pipe = StableDiffusionPipeline.from_pretrained(model_name, torch_dtype=torch.float16)
    pipe.save_pretrained(join(MODEL_PATH, "pipe"))

    

if __name__ == "__main__":
    save_model()
    