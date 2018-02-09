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
    test.save(job_info_dict)
