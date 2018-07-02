import selenium.webdriver
import urllib.request
import urllib.parse
import json


# 创建获取json的request对象
def get_request(page_num):
    url = 'https://job.alibaba.com/zhaopin/socialPositionList/doList.json'
    data = {
        'pageSize': '10',
        't': '0.935039498596081',
        'keyWord': 'python',
        'pageIndex': str(page_num)
    }
    data = bytes(urllib.parse.urlencode(data), encoding='utf-8')
    headers = {
        "User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)"
    }
    request = urllib.request.Request(url=url, data=data, headers=headers)

    return request

# 获取页数
def get_page_count():
    request = get_request(1)
    response = urllib.request.urlopen(request)
    data_dict = response.read().decode('utf-8')
    data_dict = json.loads(data_dict)
    page_count = data_dict['returnValue']['totalPage']
    return page_count

# 根据页数获取request列表
def get_request_list():
    request_list = []
    pages = get_page_count()
    for page in range(pages):
        request_list.append(get_request(page))

    return request_list

# 根据request列表发起请求获取json数据
def get_json_list():
    json_list = []
    request_list = get_request_list()
    for request in request_list:
        response = urllib.request.urlopen(request)
        json_list.append(response.read().decode('utf-8'))
    return json_list


if __name__ == '__main__':
    data_list = []
    json_list = get_json_list()
    for json_data in json_list:
        json_data = json.loads(json_data)
        str = json_data['returnValue']['datas'][0]['requirement']
        str = str.replace('<br/>','')
        print(str)