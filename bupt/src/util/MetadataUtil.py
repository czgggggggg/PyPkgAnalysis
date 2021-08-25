import requests #抓取python包的json信息
import json #解析抓取的json信息
import dateutil.parser #处理upload_time

# from utildate import parser

class MetadataUtil:
    def __init__(self, name):
        self.name = name

    def get_metadata(self, pkg_name, pkg_version=None):
        if pkg_version:
            json_url = "https://pypi.python.org/pypi/%S/%S/json" % (pkg_name, pkg_version)
        else:
            json_url = "https://pypi.python.org/pypi/%s/json" % pkg_name
        json_content = requests.request('GET', json_url)
        #return json_content  直接返回的json_content值是：<Response [200]>
        json_info = json.loads(json_content.text)
        return json_info #已经获取到json内容，但是格式有点问题

    def get_author(self, pkg_name):
        pkg_info = self.get_metadata(pkg_name = pkg_name)
        if pkg_name is None:
            return {} #字典类型
        maintainer = pkg_info['info'].get('maintainer', None)
        author = pkg_info['info'].get('author', None)
        author_email = pkg_info['info'].get('author_email', None)
        python_version = pkg_info['info'].get('python_version',None)
        return {'maintainer': maintainer, 'author': author, 'author_email': author_email}

    def get_versions(self, pkg_name):
        pkg_info = self.get_metadata(pkg_name = pkg_name)
        if pkg_name is None:
            return [] #列表类型
        #每一个version对应多个dist
        version_dists = [(version, dists) for version, dists in pkg_info['releases'].items() if len(dists) > 0]
        #每个dist中包含上传时间upload_time，每个version取对应的多个upload_time的最大值作为这个version的上传时间
        version_date = [(version, sorted([dateutil.parser.parse(dist['upload_time']) for dist in dists], reverse=True)[0])
                        for version, dists in version_dists]
        return version_date

        # version_dists = [(ver, dists) for ver, dists in pkg_info['releases'].items() if len(dists) > 0]
        # version_date = [(ver, sorted([dateutil.parser.parse(dist['upload_time']) for dist in dists], reverse=True)[0])
        #                 for ver, dists in version_dists]

def testMethod():
    print("test")