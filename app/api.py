ip = 'localhost'
port = '8081'

# 获取商品信息api，将返回ROWxCOL个商品信息
goods_image_api = 'http://{}:{}/ECP/getgoodslist'.format(ip, port)
# 登录api
login_api = 'http://{}:{}/ECP/login'.format(ip, port)
# 注册api
register_api = 'http://{}:{}/ECP/register'.format(ip, port)
# 获取随机货物信息api
random_goods_api = 'http://{}:{}/ECP/randomGoods'.format(ip, port)
# 成为商家的api
become_business_api = 'http://{}:{}/ECP/becomeBusiness'.format(ip, port)
# 上传商品api
upload_goods_api = 'http://{}:{}/ECP/upLoadGoods'.format(ip, port)
# 获取商家信息
get_business_info = 'http://{}:{}/ECP/getBusinessInfo'.format(ip, port)
