from tabulate import tabulate
import sys
sys.path.append("/workspace/Financial_Statement/src/common")

import UrlGenerator
import RequestFactors as rf
import UrlToInfo
import DcInfoBrowse


# 유저입력 012221
def check_recapitalization():
    list_of_essential_cds = [rf.corp_code, rf.bsns_year, rf.reprt_code]
    condition_info = UrlGenerator.get_url_info(list_of_essential_cds=list_of_essential_cds)
    request_url = "https://opendart.fss.or.kr/api/irdsSttus.json"
    url = UrlGenerator.get_url(request_url, condition_info)

    response = UrlToInfo.get_info_from_url(url)
    return response

def check_capital():
    # rcept_no를 받아내는 과정.
    print("\n공시 정보를 검색합니다.\n")
    response = DcInfoBrowse.browse_dc_info()
    print(response)
    dc_choice = input("\n검색된 위의 공시 정보들 중, 열람을 원하는 공시 목록의 맨 왼쪽 번호(index)들을 쉼표(,)로 구분하여 입력해주세요.\n")
    choice_list = dc_choice.split(',')
    for choice in choice_list:
        choice = int(choice.strip())
    
    print(response[choice_list, :])
    
    
    
    
    list_of_essential_cds = [rf.reprt_code]
    condition_info = UrlGenerator.get_url_info(list_of_essential_cds=list_of_essential_cds)
    request_url = "https://opendart.fss.or.kr/api/fnlttXbrl.xml"
    url = UrlGenerator.get_url(request_url, condition_info)

    response = UrlToInfo.get_info_from_url(url)
