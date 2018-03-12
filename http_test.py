import requests
class requests_class():

    def request_get(self,url,param,headers):
        result_get= requests.get(url,param,headers=headers)
        return  result_get.json()

       def requests_post(self, url, param, headers):
        result_post = requests.post(url, param, headers=headers)
        return result_post.json()


#如下是测试代码
if __name__ == "__main__":
    captcha=requests_class()
    url = "https://test-jc-api.haochang.tv/api/login/telphone/captcha"
    param = {"telphone": "18600000000", "captcha": "1234"}
    headers = {"x-api-test": "true"}
    a =captcha.requests_post(url, param, headers)
    print (a)


    '''url="https://new-test-api.haochang.tv/api/login/telphone"
    param={"telphone":"18696782786","captcha":"1234"}
    headers= {"x-api-test":"true","X-HTTP-Method-Override":"PUT"}
    #创建实例调用

    tester=requests_class()
    r2=tester.requests_post(url,param,headers)
    print (r2)'''
