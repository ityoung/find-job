from pymongo import MongoClient

MongoConfig = {
    "host": "localhost",
    "port": 27017
}


class JobInfo():
    def __init__(self):
        client = MongoClient(MongoConfig['host'], MongoConfig['port'])
        self.db = client.find_job
        self.collection = self.db.jobs_info

    def save(self, job_info_dict):
        self.collection.insert_one(job_info_dict)

    def read(self):
        # TODO: find element.
        pass

    def is_exist(self, job_info_dict):
        url = job_info_dict['url']
        res = self.collection.find_one({'url': url})
        if res:
            return True
        return False


if __name__ == '__main__':
    job_info_dict = {
        "title": "test",
        "salary": "test",
        "require": "test",
        "content": "test",
        "company": "test",
        "address": "test"
    }
    test = JobInfo()
    # test.save(job_info_dict)
    print(test.is_exist({'url': 'https://www.lagou.com/jobs/3358212.html', 'salary': '3k-5k', 'businessZones': ['徐东', '友谊大道', '车站', '徐东', '友谊大道', '车站'], 'workYear': '应届毕业生', 'positionName': '数据分析专员/实习生', 'companyFullName': '北京拓普丰联信息工程有限公司湖北分公司', 'jobDetail': '[]'}))