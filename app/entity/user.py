from app.utils import *


class User:
    def __init__(self, **kwargs):
        self.is_login = False
        self.is_business = False
        self.id = kwargs['id'] if kwargs.__contains__("id") else None
        self.name = kwargs['name'] if kwargs.__contains__("name") else None
        self.pwd = kwargs['pwd'] if kwargs.__contains__("pwd") else None
        self.address = kwargs['address'] if kwargs.__contains__("address") else None
        self.phone = kwargs['phone'] if kwargs.__contains__("phone") else None
        self.balance = kwargs['balance'] if kwargs.__contains__("balance") else None
        self.gender = kwargs['gender'] if kwargs.__contains__("gender") else None
        self.image_url = kwargs['image_url'] if kwargs.__contains__("image_url") else None
        self.identity = kwargs['identity'] if kwargs.__contains__("identity") else None
        self.business_id = kwargs['business_id'] if kwargs.__contains__("business_id") else None
        self.create_time = kwargs['create_time'] if kwargs.__contains__("create_time") else None
