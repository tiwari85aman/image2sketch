import os
import cv2
from sketch_algo1 import image_algo_one
from sketch_algo2 import image_algo_two
import click

@click.command()
@click.option('--source_dir', required=True, type=str)
def generate(source_dir):
    dir = source_dir
    for root, dirs, files in os.walk(dir):
        for each in files:
            print("Processing : {}".format(each))
            filename, extension = each.split(".")
            image_path = os.path.join(root, each)
            sketch_1 = image_algo_one(image_path)
            sketch_1_filename = filename + "_sketch1." + extension
            sketch_1_dir = os.path.join("./output", sketch_1_filename)
            print (sketch_1_dir)
            cv2.imwrite(sketch_1_dir, sketch_1)
            sketch_2 = image_algo_two(image_path)
            sketch_2_filename = filename + "_sketch2." + extension
            sketch_2_dir = os.path.join("./output", sketch_2_filename)
            cv2.imwrite(sketch_2_dir, sketch_2)


if __name__ == '__main__':
    generate()
