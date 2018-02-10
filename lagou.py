import uuid
import requests
import json
from bs4 import BeautifulSoup
# import lxml
from mongo_config import JobInfo
# import re
from black_list import BLACK_ZONE

class LagouCrawler():
    def __init__(self):
        self.is_school_job = "0"
        self.kd = "数据"

    def get_uuid(self):
        return str(uuid.uuid4())

    def get_job_list(self, page):
        url = "https://www.lagou.com/jobs/positionAjax.json"
        querystring = {"px": "new", "city": "武汉", "needAddtionalResult": "false", "isSchoolJob": self.is_school_job}
        if self.gj:
            querystring['gj'] = self.gj
        payload = "first=false&pn=" + str(page) + "&kd=%E6%95%B0%E6%8D%AE"
        cookie = "JSESSIONID=" + self.get_uuid() + "; user_trace_token=" + self.get_uuid() + "; LGUID=" + self.get_uuid() + "; index_location_city=%E6%88%90%E9%83%BD; SEARCH_ID=" + self.get_uuid() + '; _gid=GA1.2.717841549.1514043316; _ga=GA1.2.952298646.1514043316; LGSID=' + self.get_uuid() + "; LGRID=" + self.get_uuid() + "; "
        headers = {'cookie': cookie,'origin': "https://www.lagou.com",'x-anit-forge-code': "0",'accept-encoding': "gzip, deflate, br",'accept-language': "zh-CN,zh;q=0.8,en;q=0.6",'user-agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",'content-type': "application/x-www-form-urlencoded; charset=UTF-8",'accept': "application/json, text/javascript, */*; q=0.01",'referer': "https://www.lagou.com/jobs/list_Java?px=new&city=%E6%88%90%E9%83%BD",'x-requested-with': "XMLHttpRequest",'connection': "keep-alive",'x-anit-forge-token': "None",'cache-control': "no-cache",'postman-token': "91beb456-8dd9-0390-a3a5-64ff3936fa63"}
        response = requests.request("POST", url, data=payload, headers=headers, params=querystring)
        return json.loads(response.text)

    def get_job_info_page(self, position_id):
        url = "https://www.lagou.com/jobs/%s.html" % position_id
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)'
                          'Chrome/45.0.2454.85 Safari/537.36 115Browser/6.0.3',
            'Host': 'www.lagou.com',
            'Connection': 'keep-alive',
            'Origin': 'http://www.lagou.com'
        }

        res = requests.get(url, headers=headers)
        return res.text

    def get_job_detail(self, position_id):
        page = self.get_job_info_page(position_id)
        soup = BeautifulSoup(page, 'lxml')
        job_desc = soup.select('dd[class="job_bt"]')
        job_desc = str(job_desc)
        return job_desc
        # count = 0
        # has_detail = False
        # while count < 3:
        #     page = self.get_job_info_page(position_id)
        #     soup = BeautifulSoup(page, 'lxml')
        #     job_desc = soup.select('dd[class="job_bt"]')
        #     job_desc = str(job_desc)
        #     if job_desc == '[]':
        #         count += 1
        #         continue
        #     has_detail = True
        # if has_detail:
        #     x = re.sub(r"<p>", "", job_desc)
        #     x = re.sub(r"</p>", "", x)
        #     x = re.sub(r'.*<dd class="job_bt">', "", x)
        #     x = re.sub(r'<h3 class="description">', "", x)
        #     x = re.sub(r'</h3>\n', "", x)
        #     x = re.sub(r'<div>', "", x)
        #     x = re.sub(r'</div>\n.*', "", x)
        #     return x
        # return None

    def is_in_black_list(self, zone):
        if zone and (set(BLACK_ZONE) & set(zone)):
            return True
        return False

    def run(self, mongo_coll, **kwargs):
        self.is_school_job = kwargs.get("is_school_job", "0")
        self.gj = kwargs.get("gj", None)
        res = self.get_job_list(1)
        assert res['code'] == 0
        positionResult = res['content']['positionResult']
        totalCount = positionResult['totalCount']
        job_result = positionResult['result']
        rounds = int(totalCount / 15) + 1
        for j in range(rounds):
            for i in range(len(job_result)):
                this_job = job_result[i]
                position_id = this_job['positionId']
                # job_detail = test.get_job_detail(position_id)
                info_dict = {
                    'salary': this_job['salary'],
                    'workYear': this_job['workYear'],
                    'businessZones': this_job['businessZones'],
                    'companyFullName': this_job['companyFullName'],
                    'positionName': this_job['positionName'],
                    'url': "https://www.lagou.com/jobs/%s.html" % position_id
                }
                if mongo_coll.is_exist(info_dict):
                    continue
                if self.is_in_black_list(this_job['businessZones']):
                    continue
                mongo_coll.save(info_dict)
                print(info_dict)
            if j < rounds - 1:
                res = self.get_job_list(j+1)
                assert res['code'] == 0
                job_result = res['content']['positionResult']['result']


if __name__ == "__main__":
    find_list = [
        {
            'is_school_job': "1"
        },
        {
            'is_school_job': "0",
            'gj': "3年及以下"
        },
        {
            'is_school_job': "0",
            'gj': "不要求"
        }
    ]
    lagou_mongo = JobInfo()
    lagou_crawler = LagouCrawler()
    for i in find_list:
        lagou_crawler.run(lagou_mongo, **i)
    # detail = test.get_job_detail("4007500")
    # print(detail)