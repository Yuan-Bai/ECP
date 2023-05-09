import json
import time
from PIL import Image
import pillow_avif


def read_file(file_name):
    with open(file_name, 'r',  encoding='UTF-8') as file:
        return file.read()


def write_file(file_name, data):
    with open(file_name, 'w',  encoding='UTF-8') as file:
        return file.write(data)


def read_jsonFile(file_name):
    with open(file_name, 'r',  encoding='UTF-8') as file:
        return json.load(file)


def avif_to_jpg(AVIFfilename):
    AVIFimg = Image.open(AVIFfilename)
    AVIFimg.save(AVIFfilename.replace("avif", 'jpg'), 'JPEG')


class Timer:
    def __init__(self, duration, func=None):
        self.duration = duration
        self.func = func
        self.start_time = 0
        self.active = False

    def activate(self):
        self.active = True
        self.start_time = time.time()

    def deactivate(self):
        self.active = False
        self.start_time = 0

    def update(self):
        current_time = time.time()
        if current_time - self.start_time >= self.duration:
            if self.func and self.active:
                self.func()
            self.deactivate()


if __name__ == '__main__':
    import os

    file = r'C:/Users/29946/Desktop/temp/'
    for root, dirs, files in os.walk(file):
        for file in files:
            if file.__contains__('.avif'):
                avif_to_jpg(root+file)
                os.remove(root+file)

