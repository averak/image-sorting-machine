import glob
import os.path

import matplotlib.pyplot as plt
import numpy as np
import tqdm
from matplotlib import image as mpimg
from matplotlib.backend_bases import KeyEvent


class Image:
    def __init__(self, filename: str):
        self.filename = filename
        self.content: np.ndarray = mpimg.imread(filename)


COLUMNS = 5
BATCH_SIZE = COLUMNS * 10

image_filenames = glob.glob("data/*.jpg")
images = [Image(filename) for filename in tqdm.tqdm(image_filenames)]
number_of_batch = 0

plt.figure(figsize=(20, 10))


def draw_images(images_batch: list[Image]):
    for i, image in enumerate(images_batch):
        print(f"{i}: {image.filename}")
        plt.subplot(len(images_batch) // COLUMNS + 1, COLUMNS, i + 1)
        plt.imshow(image.content)
        # plt.axis('off')
        # plt.xlabel(os.path.basename(image.filename))
        plt.ylabel(f"{i}: {os.path.basename(image.filename).split('_')[0]}")
        plt.draw()


def on_press_key(event: KeyEvent):
    global number_of_batch
    global images

    if event.key == "right":
        number_of_batch += 1
        print(f"{number_of_batch * BATCH_SIZE}/{len(image_filenames)}")
        draw_images(images[(number_of_batch * BATCH_SIZE):((number_of_batch + 1) * BATCH_SIZE)])
    elif event.key == "left":
        number_of_batch -= 1
        print(f"{number_of_batch * BATCH_SIZE}/{len(image_filenames)}")
        draw_images(images[(number_of_batch * BATCH_SIZE):((number_of_batch + 1) * BATCH_SIZE)])


plt.connect('key_press_event', on_press_key)
plt.show()
