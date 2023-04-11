import json

import requests
from app.api import *
from app.entity.user import User


def getGoodsList(user):
    cookie = user.getCookie()
    params = {'cookie': cookie}
    resp = requests.post(goods_image_api, params=params)
    return resp.text


def login(user):
    if user.is_login:
        return
    params = {
        'name': user.name,
        'pwd': user.pwd,
    }
    resp_json = None
    try:
        resp = requests.post(login_api, params=params, timeout=5)
        resp_json = json.loads(resp.text)
        if resp_json['is_login'] == 'fail':
            return False
        return resp_json['user']
    except:
        return False


def register(user):
    if user.is_login:
        return
    params = {
        'name': user.name,
        'pwd': user.pwd,
    }
    resp = None
    try:
        resp = requests.post(register_api, params=params, timeout=5)
    except:
        return False
    return resp.text


def become_business(user):
    if user.is_business:
        return False
    params = {
        'name': user.name,
        'pwd': user.pwd,
    }
    resp = None
    try:
        resp = requests.post(register_api, params=params, timeout=5)
    except:
        return False


def get_random_goods():
    resp = requests.post(random_goods_api)
    resp_json = json.loads(resp.text)
    return resp_json


if __name__ == '__main__':
    get_random_goods()
