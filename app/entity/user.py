from app.utils import *


class User:
    def __init__(self, **kwargs):
        self.is_login = False
        self.address = kwargs['address']
        self.name = kwargs['name']
        self.vip = kwargs['vip']
        self.balance = kwargs['balance']
        self.like = kwargs['like']

    def getCookie(self):
        return read_file('app/cookie/cookie')

    def login(self):
        pass

