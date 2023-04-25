import json
import time


def read_file(file_name):
    with open(file_name, 'r',  encoding='UTF-8') as file:
        return file.read()


def write_file(file_name, data):
    with open(file_name, 'w',  encoding='UTF-8') as file:
        return file.write(data)


def read_jsonFile(file_name):
    with open(file_name, 'r',  encoding='UTF-8') as file:
        return json.load(file)


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
