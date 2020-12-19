from time import sleep

from http_util import HttpRequestUtil
phone = '13567896827'
password = '123456'
time_sleep = 60
# web_host = "http://47.111.225.107:88"
web_host = "https://www.legouwangjin.com"
# user_agent = 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko'
user_agent = 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'


def login(phone, password):
    http_util = HttpRequestUtil()
    http_util.set_type('POST')
    http_util.set_url(web_host + '/user/login')
    params = {
        'phone': phone,
        'password': password
    }
    http_util.set_params(params)
    http_header = {
        'Content-Type': 'application/json',
        'User-Agent': user_agent
    }
    http_util.set_new_header(http_header)
    response = http_util.http_post_json()
    print("login response is {}".format(response))
    # {'status': 1, 'message': '登录成功!', 'data': {'token': 'euD4gx7qJIY9tNa96eSJyuPE74WxyiK8LXolyKcsGrYOUTgIkuUntKwHQwwZ4yavp3J1rxuhgj3tviVqEUEe85ep', 'phone': '13567896827', 'isAuth': 2, 'isSetPayPass': 0}}
    token = None
    if response and response['status'] ==1 :
        token = response['data']['token']
    print("login token is {}".format(token))
    return token


def get_goods_cate():
    http_util = HttpRequestUtil()
    http_util.set_type('GET')
    http_util.set_url(web_host + '/goods/goodsCate')

    response = http_util.http_get()
    print("getGoodsCate response is {}".format(response))
    # {'status': 1, 'message': '获取成功!', 'data': {'list': [{'id': 1, 'logo': '', 'title': '普惠区', 'desc': '', 'start_time': '23:38:00', 'endTime': '23:58:00', 'timeNow': '16:18:20', 'list': [{'id': 70821465118463, 'cate_id': 1, 'title': '4112', 'logo': 'http://www.nbdaiqile.com/FkMh_ft7HIDjRG6aGki_e2v7QL1G', 'goods_status': 1, 'number_stock': 1, 'price': '2342.00'}, {'id': 70821467400419, 'cate_id': 1, 'title': '234', 'logo': 'http://www.nbdaiqile.com/FuaG0TIlcPK3_vUJKo35XR9E2f-n', 'goods_status': 1, 'number_stock': 1, 'price': '2342.00'}, {'id': 70821456939923, 'cate_id': 1, 'title': '234', 'logo': 'http://www.nbdaiqile.com/FhlbuaDdqm9Uf0g_rcbk7e_P6gGC', 'goods_status': 1, 'number_stock': 1, 'price': '4234.00'}, {'id': 70821389646518, 'cate_id': 1, 'title': '1234', 'logo': 'http://www.nbdaiqile.com/FgkpctZSLFnfa7o6QadBLiPFsXEj', 'goods_status': 1, 'number_stock': 1, 'price': '2341.00'}]}, {'id': 2, 'logo': '', 'title': '中端区', 'desc': '', 'start_time': '23:38:00', 'endTime': '23:58:00', 'timeNow': '16:18:20', 'list': [{'id': 69884140939406, 'cate_id': 2, 'title': '中国风国画', 'logo': 'http://www.nbdaiqile.com/FuLQl9NLmE2NXiPwaBzuhGOzF3YG', 'goods_status': 2, 'number_stock': 1, 'price': '25602.00'}, {'id': 69900868631029, 'cate_id': 2, 'title': '清代郑板桥墨宝', 'logo': 'http://www.nbdaiqile.com/FuSLdtclyIEkpcOgzWPvonhbffo3', 'goods_status': 2, 'number_stock': 1, 'price': '231.53'}, {'id': 69902943653129, 'cate_id': 2, 'title': '秦代紫金壶', 'logo': 'http://www.nbdaiqile.com/FquCV1O4G780PDKL8Z72jZsE8Sn4', 'goods_status': 2, 'number_stock': 1, 'price': '620.53'}, {'id': 69902999322339, 'cate_id': 2, 'title': '新疆和田美玉', 'logo': 'http://www.nbdaiqile.com/Fq9cjvL1LPhy5HB9-4AcHWSgk53K', 'goods_status': 2, 'number_stock': 1, 'price': '5100.00'}]}, {'id': 3, 'logo': '', 'title': '至尊区', 'desc': '', 'start_time': '23:38:00', 'endTime': '23:58:00', 'timeNow': '16:18:20', 'list': [{'id': 70821449489752, 'cate_id': 3, 'title': '123', 'logo': 'http://www.nbdaiqile.com/FhTjUwcuCDGt6HGJKmpkSbnbU222', 'goods_status': 1, 'number_stock': 1, 'price': '2342.00'}, {'id': 69895726859567, 'cate_id': 3, 'title': '金朝水墨丹青', 'logo': 'http://www.nbdaiqile.com/FhgINS2rRVLDblu-9iNqz4xsRsm1', 'goods_status': 2, 'number_stock': 1, 'price': '120.44'}, {'id': 69900885096119, 'cate_id': 3, 'title': '明代景德镇花瓶', 'logo': 'http://www.nbdaiqile.com/FqqUzqUZOPzkxT2GCKyslHo9fR86', 'goods_status': 2, 'number_stock': 1, 'price': '449.82'}, {'id': 69902940851720, 'cate_id': 3, 'title': '元代翡翠骏马', 'logo': 'http://www.nbdaiqile.com/Ft2T01ZFAgFkIrNtWxH7DQpGwDBU', 'goods_status': 2, 'number_stock': 1, 'price': '231.53'}]}], 'startTime': '23:38:00', 'endTime': '23:58:00', 'timeNow': '16:18:20'}}
    good_list = None
    if response and response['status'] == 1:
        good_list = response['data']['list']
    return good_list


def order(token,goods_id):
    http_util = HttpRequestUtil()
    http_util.set_type('POST')
    http_util.set_url(web_host + '/order/buy')
    params = {
        'goods_id': goods_id
    }
    http_util.set_params(params)
    http_header = {
        'Content-Type':'application/json',
        'token': token,
        'User-Agent': user_agent
    }
    http_util.set_new_header(http_header)
    response = http_util.http_post_json()
    print("order response is {},goods_id is {}".format(response,goods_id))
    return response


if __name__ == '__main__':
    token = login(phone, password)
    goods_list = get_goods_cate()
    if goods_list:
        for goods in goods_list:
            title = goods['title']
            start_time = goods['start_time']
            end_time = goods['endTime']
            this_goods_list = goods['list']
            print("title is {},start_time is {},end_time is {}".format(title,start_time,end_time))
            if this_goods_list and len(this_goods_list) > 0:
                for current_goods in this_goods_list:
                    status = current_goods['goods_status']
                    num_stock = current_goods['number_stock']
                    price = current_goods['price']
                    current_title = current_goods['title']
                    goods_id = current_goods['id']
                    print("current_title is {},goods_id is {},price is {},status is {},num_stock is {}"
                          .format(current_title,goods_id,price,status,num_stock))
                    if status == 1:
                        order_result = order(token,goods_id)
                        print('----- 恭喜你，可以抢购，结果 order_result is {}，标题{},价格{} 等待{}秒后再抢'.format(order_result,current_title,price,time_sleep))
                        sleep(time_sleep)
                    else:
                        print("+++++ 很遗憾，该商品没法抢购，状态status is {}, 状态1是可以抢购，2是已售出".format(status))
