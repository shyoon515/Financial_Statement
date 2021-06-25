import sys
sys.path.append("/workspace/Financial_Statement/src/chapter2")
sys.path.append("/workspace/Financial_Statement/src/common")

import dart_fss as dart
import urllib.request as ul
from zipfile import ZipFile
from io import BytesIO
import xml.etree.ElementTree as elemTree


# 프로그램 상태 0
def ProgramStart():
    print("""
기업정보 분석 프로그램 with dart를 시작합니다.
    """)
    user_reply = int(input("""
기능을 선택해주세요(정수 입력).
1. 박 회계사의 재무제표 분석법(공시정보 가져오기)    0. 프로그램 종료하기
"""))

    if user_reply == 1:
        api_key = get_API()
        corp_list = update_corp_list()    # 여기까지는 첫 접속 때만 로딩할 수 있도록 코드를 짜자.
        
        import UrlGenerator
        url = UrlGenerator.GetBrowseUrl(api_key, corp_list)    # '공시정보' API에 접속할 url을 저장
        
        import dc_info
        dicts_of_dc_info = dc_info.get_dc_info(url)    # 만들어진 url로 '공시정보'에서 모든 인자들을 list of dict의 형태로 반환해준다.
        for i, val in enumerate(dicts_of_dc_info):
            print(str(i+1),"    ",val,'\n')
        ParkFS()
    elif user_reply == 0:
        End()
    else:
        End()


# 프로그램 상태 01
def get_API():
    import AllocateAPI
    api_key = AllocateAPI.api_key(api_key=input('DART 사이트에서 할당받은 API를 입력하세요.'))    #해당 API로 할당과 인증이 완료.
    return api_key

def update_corp_list():
    # 모든 상장된 기업 리스트 불러오기
    corp_list = dart.get_corp_list()
    print("\ncorp_list 타입: ", type(corp_list))
    print("\ncorp_list 프린트: ", corp_list)
    return corp_list

def get_dc_info(url):
    pass    #temp2 파일 참조하여 완성.
    

def ParkFS():
    print("_"*70+"""
초기화면/박 회계사의 재무제표 분석법
""")
    user_reply = int(input("""
2. 재무상태표로 기업의 재무 상태 파악하기
3. 손익계산서로 경영 성과 엿보기
4. 지배기업과 종속기업 그리고 재무제표
5. 기업의 현금흐름 파악하기
6. 주석사항에서 알짝 정보 얻기
7. 재무제표 분석과 주요 재무비율
0. 이전으로
"""))

    if user_reply == 2:
        chapter2()
    elif user_reply == 0:
        ProgramStart()


def chapter2():
    import chapter2
    chapter2.start()


def End():
    print("프로그램을 종료합니다.")
