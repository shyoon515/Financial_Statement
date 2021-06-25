"""
<참고 url들>
고유번호 가져오기 https://electromastersesi.tistory.com/147
url 생성 방법 https://kwonkyo.tistory.com/95
"""

import dart_fss as dart
import urllib.request as ul
from zipfile import ZipFile
from io import BytesIO
import json


# url을 입력하면 json형태로 온 "list" 응답결과를 dict로 반환해주는 코드. 정보를 추출해와서 dict로 반환한다.
def get_info_from_url(url):
    url=url
    request = ul.Request(url)
    response = ul.urlopen(request)
    responseData = response.read()

    data = json.loads(responseData)
    return data["list"]
