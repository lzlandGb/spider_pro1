import requests
import requests.auth


def login_like_js():
    auth = requests.auth.HTTPBasicAuth('sadf', '456')
    response = requests.post('http://pythonscraping.com/pages/auth/login.php', auth=auth)
    print(response.text)

    pass

if __name__ == '__main__':
    login_like_js()