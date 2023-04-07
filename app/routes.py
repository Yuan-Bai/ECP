import requests
from app.api import *


def getGoodsList(user):
    cookie = user.getCookie()
    param = {'cookie': cookie}
    resp = requests.post(goods_image_api, param=param)
    print(resp)
