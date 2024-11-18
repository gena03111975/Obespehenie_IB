import json
import requests
from pathlib import Path

"""проверка файла / ip-адреса / url-адреса  с использованием открытого API VirusTotal без необходимости использования интерфейса веб-сайта www.virustotal.com"""


APIKEY = 'e7eb2495811c71d985f4394bcea7749bb851382aac53ed9e92e904bfd4b807e8'
API_BASE = 'https://www.virustotal.com/vtapi/v2/'


def file_scan_request(filePath):
    """отправка файла на сканирование"""

    api_url = API_BASE + 'file/scan'
    params = dict(apikey=APIKEY)
    with open(filePath, 'rb') as file:
        files = dict(file=(filePath, file))
        response = requests.post(api_url, files=files, params=params)
    if response.status_code == 200:
        result=response.json()
        print(json.dumps(result, sort_keys=False, indent=4), '\n', '-'*100)
    return result['resource']


def scan_file(post_answer):
    """отчет о последнем сканировании файла"""

    api_url = API_BASE + 'file/report'
    params = dict(apikey=APIKEY, resource=post_answer)
    response = requests.get(api_url, params=params)
    if response.status_code == 200:
        result=response.json()
        print(json.dumps(result, sort_keys=False, indent=4), '\n', '-'*100)


def scan_ip(ip):
    """отправка IP-адреса на сканирование"""

    api_url = API_BASE + 'ip-address/report'
    params = dict(apikey=APIKEY, ip=ip)
    response = requests.get(api_url, params=params)
    if response.status_code == 200:
        result=response.json()
        print(json.dumps(result, sort_keys=False, indent=4))  


def scan_url(url):
    """проверка url-адреса"""

    api_url = API_BASE + 'url/report'
    params = dict(apikey=APIKEY, resource=url, scan=0)
    response = requests.get(api_url, params=params)
    if response.status_code == 200:
        result=response.json()
        print(json.dumps(result, sort_keys=False, indent=4))  


# filePath = Path('./uplift_test.csv').absolute()
# print(filePath)
# post_answer = file_scan_request('E:/learning/lesson28_IS/HW\hw3/for_scan/uplift_test.csv')



post_answer = file_scan_request('./hw3/for_scan/uplift_test.csv')
# scan_file(post_answer)
# scan_ip('94.156.189.28')
# scan_url('cheapdealnow.top')