import requests


def get_ip_addr():
    ip = '223.73.0.88'
    url = 'https://api.ip2country.info/ip?'
    response = requests.get(url + ip)

    print(response.text)
    print(type(response.json()))   # class: dict
    print(response.json().get('countryName'))


if __name__ == '__main__':
    get_ip_addr()