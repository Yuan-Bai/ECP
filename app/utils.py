from enum import Enum


def read_file(file_name):
    with open(file_name, 'r',  encoding='UTF-8') as file:
        return file.read()


def write_file(file_name, data):
    with open(file_name, 'w',  encoding='UTF-8') as file:
        return file.write(data)


class AREA(Enum):
    HomePage = 'HomePage'
    Classification = 'Classification'
    History = 'History'
    ShoppingCar = 'ShoppingCar'
    UserCenter = 'UserCenter'
