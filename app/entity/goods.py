

class Goods:
    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.price = kwargs['price']
        self.describe = kwargs['describe']
        self.image_url = kwargs['image_url']
        self.sales_volume = kwargs['sales_volume']
        self.stock = kwargs['stock']

    # 获取评论信息，属于请求
    def get_review(self):
        pass
