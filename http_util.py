import json
import logging
import ssl
from urllib import request, parse

logger = logging.getLogger('HttpRequestUtil')

# Python 2.7.9 之后引入了一个新特性
# 当你urllib.urlopen一个 https 的时候会验证一次 SSL 证书
ssl._create_default_https_context = ssl._create_unverified_context


class HttpRequestUtil:
    def __init__(self):
        self.url = ''
        self.params = ''
        self.type = 'post'
        # 默认post请求
        self.header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko'}
        # 默认请求头
        self.addheader = ''
        self.run_res = ''
        self.cookies = []

    def set_url(self, url):
        self.url = url
        return self

    def set_params(self, params):
        self.params = params
        return self

    def set_header(self, addheader):
        self.addheader = addheader
        return self

    def set_new_header(self,header):
        self.header = header
        return self

    def set_type(self, type):
        self.type = type
        return self

    def append_header(self, req):
        """将头信息追加到request请求头部"""
        for fie_id in self.addheader:
            req.add_header(fie_id, self.addheader[fie_id])
        return self

    def http_get(self):
        # print("url:" + str(self.url))
        # print("params:" + str(self.params))
        if not self.url:
            raise Exception('url must not empty !')
        # 参数拼接
        # params = parse.urlencode(self.params).encode(encoding='utf-8')
        params = parse.urlencode(self.params)
        # print(params)
        req = request.Request(url='%s%s%s' % (self.url, '?', params), headers=self.header,method=self.type)
        self.append_header(req)
        return self.http_send(req)

    def http_post(self):
        # logger.info("发送post请求")
        # logger.info("url:" + str(self.url))
        # logger.info("params:" + str(self.params))
        if not self.url:
            raise Exception('url must not empty !')
        # 普通数据使用
        params = parse.urlencode(self.params).encode(encoding='utf-8')
        req = request.Request(url=self.url, data=params, headers=self.header,method=self.type)
        self.append_header(req)
        return self.http_send(req)

    def http_post_json(self):
        # logger.info("发送post请求")
        # logger.info("url:" + str(self.url))
        # logger.info("params:" + str(self.params))
        if not self.url:
            raise Exception('url must not empty !')
        # json串数据
        params = json.dumps(self.params).encode(encoding='utf-8')
        req = request.Request(url=self.url, data=params, headers=self.header,method=self.type)
        self.set_header({"Content-Type": "application/json"})
        self.append_header(req)
        return self.http_send(req)

    # def http_cookie_manager(self, req):
    #     # 创建cookie处理器
    #     cj = httptest.cookiejar.CookieJar()
    #     opener = req.build_opener(req.HTTPCookieProcessor(cj), req.HTTPHandler)
    #     req.install_opener(opener)
    #     return self

    def http_send(self, req):
        try:
            res = request.urlopen(req)
            self.cookies = res.getheader('Set-Cookie')
            self.run_res = res.status
            # print(self.cookies)
            # print(self.run_res)
            resb = res.read()
            result = resb.decode(encoding='utf-8')
            # result = json.loads(resb)
        except Exception as e:
            result_exception = e
            logger.info("http_send exception is {}".format(result_exception))
            return result_exception
        json_result = json.loads(result)
        logger.info("result:".format(result))
        logger.info("json_result:".format(json_result))
        return json_result

    def get_response_status(self):
        return self.run_res
