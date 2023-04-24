from os.path import join, splitext, exists
import os

import click

from midjourney.model import model


@click.command()
@click.argument('path')
def run(path):
    model.load_model()
    input_dir = join(path, 'inputs')
    output_dir = join(path, 'outputs')
    for file in os.listdir(input_dir):
        root, ext = splitext(file)
        if ext != '.txt':
            continue
        output = join(path, 'outputs', root) + ".png"
        if exists(output):
            continue
        else:
            with open(join(path, 'inputs', file)) as f:
                prompt = f.read().strip()
                model.generate_image2(prompt, filepath=output)
            
if __name__ == "__main__":
    run()
        