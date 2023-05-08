from app.api import goods_image_api, random_goods_api
from app.routes import req
from app.settings import ROW, COL


class Goods:
    def __init__(self, **kwargs):
        self.id = kwargs['id'] if kwargs.__contains__("id") else None
        self.name = kwargs['name'] if kwargs.__contains__("name") else None
        self.price = kwargs['price'] if kwargs.__contains__("price") else None
        self.introduce = kwargs['introduce'] if kwargs.__contains__("introduce") else None
        self.image_url = kwargs['image_url'] if kwargs.__contains__("image_url") else None
        self.sales_volume = kwargs['sales_volume'] if kwargs.__contains__("sales_volume") else None
        self.amount = kwargs['amount'] if kwargs.__contains__("amount") else None
        self.type = kwargs['type'] if kwargs.__contains__("type") else None

    # 获取评论信息，属于请求
    def get_review(self):
        pass

    def update_by_json(self, goods_json):
        self.id = goods_json.get('id')
        self.name = goods_json.get('goods_name')
        self.price = goods_json.get('price')
        self.introduce = goods_json.get('introduce')
        self.image_url = goods_json.get('image_url')
        self.amount = goods_json.get('amount')
        self.type = goods_json.get('type')


def get_goods_list():
    params = {
        'nums': ROW * COL
    }
    data = req.get_data(req.to_python(req.request('post', random_goods_api, params=params)))
    goods_list = []
    if data is None:
        return
    for goods_data in data:
        goods = Goods()
        goods.update_by_json(goods_data)
        goods_list.append(goods)
    return goods_list
