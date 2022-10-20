from urllib.parse import urlencode, unquote, quote_plus
import requests
from bs4 import BeautifulSoup
from xml.etree.ElementTree import parse
import xmltodict

# 문화포털 공연전시정보 조회서비스 오픈API 서비스 키
service_key = "n1Jh450%2FmskemPK5lqiA2uBPBeE3ypioAAuWbZ6nNHIsTCnAi6Q7R%2F3IDXnvrx3lGcEyzkHXRM5CqpUyxLMNhA%3D%3D"
serviceKeyDecoded = unquote(service_key, 'UTF-8')

def performance_api():
    url = "http://www.culture.go.kr/openapi/rest/publicperformancedisplays/period"
    params = {'from': '20220101',
              'to': '20231231',
              'cPage': '1',
              'rows': '10',
              'serviceKey': service_key
              }



