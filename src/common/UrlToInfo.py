"""
<참고 url들>
고유번호 가져오기 https://electromastersesi.tistory.com/147
url 생성 방법 https://kwonkyo.tistory.com/95
"""

import dart_fss as dart
import urllib.request as ul
from zipfile import ZipFile
from io import BytesIO
import xml.etree.ElementTree as elemTree
import json
import pandas as pd
from bs4 import BeautifulSoup


# url을 입력하면 xml 형태로, 맨 첫 기업 정보 로드에 필요한 정보를 pandans DataFrame 객체로 반환해주게 된다.
def load_company_lists(url):
    request = ul.Request(url)
    response = ul.urlopen(request)

    with ZipFile(BytesIO(response.read())) as zf:
        file_list = zf.namelist()
        while len(file_list) > 0:
            file_name = file_list.pop()
            corpCode = zf.open(file_name).read().decode()

    tree = elemTree.fromstring(corpCode)

    XML_stocklist = tree.findall("list")
    corp_name = [x.findtext("corp_name") for x in XML_stocklist]
    corp_code = [x.findtext("corp_code") for x in XML_stocklist]
    stock_code = [x.findtext("stock_code") for x in XML_stocklist]

    dicts_of_dc_info = []

    for i in range(len(corp_code)):
        dicts_of_dc_info.append({
            'corp_name':corp_name[i],
            'corp_code':corp_code[i],
            'stock_code':stock_code[i],
        })

    col_name = []
    rows = []

    for info in dicts_of_dc_info[0]:
        col_name.append(info)

    for infos in dicts_of_dc_info:
        row = []
        for info in infos:
            row.append(infos[info])
        rows.append(row)

    response = pd.DataFrame(rows, columns=col_name)
    return response


# url을 입력하면 json형태로 온 "list" 응답결과를 dict로 반환해주는 코드. 정보를 dict로 추출해온 후, pandas DataFrame 객체로 반환한다.
def get_info_from_url(url):
    request = ul.Request(url)
    response = ul.urlopen(request)
    responseData = response.read()
    data = json.loads(responseData)

    resp_result = data["list"]

    col_name = []
    rows = []

    for info in resp_result[0]:
        col_name.append(info)

    for infos in resp_result:
        row = []
        for info in infos:
            row.append(infos[info])
        rows.append(row)

    response = pd.DataFrame(rows, columns=col_name)
    return response

def get_xbrl_file(url):
    request = ul.Request(url)
    response = ul.urlopen(request)

    with ZipFile(BytesIO(response.read())) as zf:
        file_list = zf.namelist()
        while len(file_list) > 0:
            file_name = file_list.pop()
            corpCode = zf.open(file_name).read().decode()
            
    soup = BeautifulSoup(corpCode, 'lxml')
    print(soup.prettify())

