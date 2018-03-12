from http_test import requests_class
class GetToken:
    def __init__(self,telphone):
        self.telphone=telphone

    def get_captcha(self):#获取验证码
        captcha=requests_class()
        url = "https://new-test-api.haochang.tv/api/login/telphone/captcha"
        param = {"telphone": self.telphone}
        headers = {"x-api-test": "true"}
        captcha.requests_post(url,param,headers)

    def post_logging(self): #手机号请求登录
        logging=requests_class()
        url = "https://new-test-api.haochang.tv/api/login/telphone"
        param = {"telphone": self.telphone, "captcha": "1234"}
        headers = {"x-api-test": "true", "X-HTTP-Method-Override": "PUT"}
        json_result=logging.requests_post(url,param,headers)
        print(json_result)
        print (type(json_result))
        return json_result['authorizeToken']#返回tocken








if __name__ == '__main__':
    a = GetToken('18696782786')
    a.get_captcha()
    token=a.post_logging()
    print (token)

