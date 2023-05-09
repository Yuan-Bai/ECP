from app.utils import *
from app.routes import req
from app.api import *


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
        self.create_time = kwargs['create_time'] if kwargs.__contains__("create_time") else None
        self.business = Business()

    def auto_login(self):
        cookie_json = read_jsonFile('./app/cookie/cookie.json')
        self.name = cookie_json['user_name']
        self.pwd = cookie_json['user_pwd']
        params = {
            'name': self.name,
            'pwd': self.pwd
        }
        resp = req.to_python(req.request('post', login_api, params=params, timeout=3))
        if resp.get('retCode') != '200':
            print(resp.get('message'))
        else:
            self.is_login = True
            self.update_by_json(resp.get('data'))

    def register(self):
        params = {
            'name': self.name,
            'pwd': self.pwd
        }
        resp = req.to_python(req.request('post', register_api, params=params, timeout=3))
        if resp.get('retCode') != '200':
            print(resp.get('message'))
        else:
            # todo 报错密码账号，注册成功时存入账号密码
            self.auto_login()

    def get_business_info(self):
        pass

    @staticmethod
    def submit_indent(self, params):
        resp = req.get_data(req.to_python(req.request('post', get_business_info, params=params)))
        if resp.get('retCode') != '200':
            return True
        else:
            return False

    def update_by_json(self, user_json):
        if user_json is None:
            return
        self.id = user_json.get('id')
        self.address = user_json.get('address')
        self.phone = user_json.get('phone')
        self.balance = user_json.get('balance')
        self.gender = user_json.get('gender')
        self.image_url = user_json.get('image_url')
        self.identity = user_json.get('identity')
        self.create_time = user_json.get('create_time')
        self.is_login = True
        business_json = user_json.get('business')
        if business_json is None:
            return
        self.business.address = business_json.get('address')
        self.business.create_time = business_json.get('create_time')
        self.business.credit = business_json.get('credit')
        self.business.id = business_json.get('id')
        self.business.image_url = business_json.get('image_url')
        self.business.name = business_json.get('name')
        self.business.phone = business_json.get('phone')
        self.business.user_id = business_json.get('user_id')
        self.is_business = True


class Business:
    def __init__(self, **kwargs):
        self.address = kwargs['address'] if kwargs.__contains__("address") else None
        self.create_time = kwargs['create_time'] if kwargs.__contains__("create_time") else None
        self.user_id = kwargs['user_id'] if kwargs.__contains__("user_id") else None
        self.phone = kwargs['phone'] if kwargs.__contains__("phone") else None
        self.image_url = kwargs['image_url'] if kwargs.__contains__("image_url") else None
        self.name = kwargs['name'] if kwargs.__contains__("name") else None
        self.id = kwargs['id'] if kwargs.__contains__("id") else None
        self.credit = kwargs['credit'] if kwargs.__contains__("credit") else None
        self.introduce = kwargs['introduce'] if kwargs.__contains__("introduce") else None

    def update_by_json(self, business_json):
        self.address = business_json.get('address')
        self.create_time = business_json.get('create_time')
        self.credit = business_json.get('credit')
        self.id = business_json.get('id')
        self.image_url = business_json.get('image_url')
        self.name = business_json.get('name')
        self.phone = business_json.get('phone')
        self.user_id = business_json.get('user_id')
        self.introduce = business_json.get('introduce')


user = User()
