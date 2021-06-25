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


# url을 입력하여 "공시정보"의 모든 list 응답결과를 dict로 반환해주는 코드.
def get_dc_info(url):
    url=url
    request = ul.Request(url)
    response = ul.urlopen(request)
    responseData = response.read()

    tree = elemTree.fromstring(responseData)

    XML_stocklist = tree.findall("list")
    corp_cls = [x.findtext("corp_cls") for x in XML_stocklist]
    corp_name = [x.findtext("corp_name") for x in XML_stocklist]
    corp_code = [x.findtext("corp_code") for x in XML_stocklist]
    stock_code = [x.findtext("stock_code") for x in XML_stocklist]
    report_nm = [x.findtext("report_nm") for x in XML_stocklist]
    rcept_no = [x.findtext("rcept_no") for x in XML_stocklist]
    flr_nm = [x.findtext("flr_nm") for x in XML_stocklist]
    rcept_dt = [x.findtext("rcept_dt") for x in XML_stocklist]
    rm = [x.findtext("rm") for x in XML_stocklist]

    dicts_of_dc_info = []

    for i in range(len(corp_code)):
        dicts_of_dc_info.append({
            'corp_cls':corp_cls[i],
            'corp_name':corp_name[i],
            'corp_code':corp_code[i],
            'stock_code':stock_code[i],
            'report_nm':report_nm[i],
            'rcept_no':rcept_no[i],
            'flr_nm':flr_nm[i],
            'rcept_dt':rcept_dt[i],
            'rm':rm[i]
        })
    
    return dicts_of_dc_info

