import requests
import json

url = "https://www.lagou.com/jobs/positionAjax.json?city=%E6%AD%A6%E6%B1%89&needAddtionalResult=false&isSchoolJob=1"

# payload = {
# "first": "true",
# "pn": 1,
# "kd": "数据"
# }

# HEADER
headers = {'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
           'Accept-Encoding': 'gzip, deflate',
           'Host': 'www.lagou.com',
           'Origin': 'http://www.lagou.com',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36',
           'X-Requested-With': 'XMLHttpRequest',
           'Referer': 'http://www.lagou.com',
           'Proxy-Connection': 'keep-alive',
           'X-Anit-Forge-Code': '0',
           'X-Anit-Forge-Token': None}

# COOKIES
# cookies = {'JSESSIONID': 'ABAAABAAAGGABCB5F9ED05611D6254D53996480825BFBE6',
#            'user_trace_token': '20170914160307-ebb5e93b-30ec-417f-af80-65cdfa2ee3dc',
#            'LGUID': '20170914160309-2609c9ac-9923-11e7-9234-525400f775ce',
#            'X_HTTP_TOKEN': '434480c84af463429fd146ff1bcebdcc',
#            'ab_test_random_num':'0',
#            'showExpriedIndex': '1',
#            'showExpriedCompanyHome': '1',
#            'showExpriedMyPublish': '1',
#            'hasDeliver': '61',
#            'gate_login_token': '22dcc8991b8cb146e02550628e9dbab7e090eccefee8bdb8',
#            'mds_login_authToken': '"QRR497iENQtCyImV5KG3jN58lQKF5yi4JfMBuBv0fK+w0tPNHgQHUBsv0cUX4QKxZcNtRmeoaZTdg1tOISTF1gyN7kYYhaSLUCE+34xQdD8kDex6Tjlli8a2xp8/fAvb8VUtyxwLklE33haLpWY3E9hSPTyekBSZxNu7jr/FFkF4rucJXOpldXhUiavxhcCELWDotJ+bmNVwmAvQCptcy5e7czUcjiQC32Lco44BMYXrQ+AIOfEccJKHpj0vJ+ngq/27aqj1hWq8tEPFFjdnxMSfKgAnjbIEAX3F9CIW8BSiMHYmPBt7FDDY0CCVFICHr2dp5gQVGvhfbqg7VzvNsw=="',
#            '_putrc': 'FB6D078F82747CC8',
#            'login': 'true',
#            'unick': '%E6%9D%A8%E6%96%B0',
#            'TG-TRACK-CODE': 'search_code',
#            '_gid': 'GA1.2.228306814.1518180697',
#            'Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6': '1518180697',
#            'Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6': '1518184747',
#            '_ga': 'GA1.2.1393215065.1505376192',
#            'LGSID': '20180209212935-4509479f-0d9d-11e8-afb8-5254005c3644',
#            'LGRID': '20180209215901-61c9cfe3-0da1-11e8-80a6-525400f775ce',
#            'SEARCH_ID': '7413cdae625a473f85197dec81417da6',
#            'index_location_city': '%E5%85%A8%E5%9B%BD'}

cookies = {'JSESSIONID': 'ABAAABAAAGGABCB5F9ED05611D6254D53996480825BFBE6',
           '_gat': '1',
           'user_trace_token': '20170914160307-ebb5e93b-30ec-417f-af80-65cdfa2ee3dc',
           'PRE_UTM': '',
           'PRE_HOST': '',
           'PRE_SITE': '',
           'PRE_LAND': 'https%3A%2F%2Fwww.lagou.com%2Fzhaopin%2F',
           'LGUID': '20170914160309-2609c9ac-9923-11e7-9234-525400f775ce',
           'SEARCH_ID': '7413cdae625a473f85197dec81417da6',
           'Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6': '1518180697',
           'Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6': '1518184747',
           '_ga': 'GA1.2.2003702965.1486066203',
           'LGSID': '20180209212935-4509479f-0d9d-11e8-afb8-5254005c3644',
           'LGRID': '20180209215901-61c9cfe3-0da1-11e8-80a6-525400f775ce'}

res = requests.post(url, headers=headers, cookies=cookies, data="first=true&pn=1&kd=%E6%95%B0%E6%8D%AE")
print(res)
print(res.text)