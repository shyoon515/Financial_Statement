import pandas as pd

import SearchCorp
import RequestFactors as rf
import SolutionForUnicodeError as ue

import sys
sys.path.append("/workspace/Financial_Statement/src")


# list 안에는 rf객체들이 들어있어야 한다. 원하는 조건을 dict 형태로 반환한다.
def get_url_info(list_of_essential_cds=[], list_of_selective_cds=[]):
    from ProgramMain import corp_list
    essential_cds = {}
    selective_cds = {}
    for condition in list_of_essential_cds:
        essential_cds[condition.name] = ""
    for condition in list_of_selective_cds:
        selective_cds[condition.name] = ""

    # 필수 인자 셋팅
    for condition in list_of_essential_cds:
        if condition.name == 'corp_code':
            essential_cds[condition.name] = SearchCorp.get_corp_code_by_name(corp_list)
        else:
            value = input(condition.kor_name+"의 검색 값을 입력하세요.\n"+condition.explanation)
            essential_cds[condition.name] = value

    #선택 인자 셋팅
    if list_of_selective_cds != []:
        resp = 1
        while resp != 0:
            selective_cds_kor_names = []
            for condition in list_of_selective_cds:
                selective_cds_kor_names.append(condition.kor_name)

            cds = ', '.join(selective_cds_kor_names)
            new_string = []
            new_string.append(cds)
            new_string.append(" 중 추가할 검색 요소를 입력하세요. 없으면 0을 입력하세요.\n")
            instructions = ''.join(new_string)

            resp = ue.usr_reply(instructions)

            if resp == "0":
                resp = 0
                break

            if (rf.corp_code in list_of_selective_cds) & (resp == rf.corp_code.kor_name):
                selective_cds[rf.corp_code.name] = SearchCorp.get_corp_code_by_name(corp_list)
            else:
                try:
                    index = selective_cds_kor_names.index(resp)
                    value = input(list_of_selective_cds[index].kor_name+"값 입력을 선택하셨습니다.\n"+list_of_selective_cds[index].explanation)
                    selective_cds[list_of_selective_cds[index].name] = value
                except ValueError:
                    print("key 요소 입력 오류, 다시 입력하세요.")
        else:
            pass

    condition_info = essential_cds.copy()
    condition_info.update(selective_cds)
    return condition_info

# request_url: 요청 url 형태, condition_info: get_url_info의 반환값. 조건에 맞는 url을 string으로 반환한다.
def get_url(request_url, condition_info={}):
    from ProgramMain import api_key
    url = request_url+"?crtfc_key="+api_key
    for condition in condition_info:
        if condition_info[condition] != '':
            condition_info[condition] = "&"+condition+"="+condition_info[condition]
    for condition in condition_info:
        url += condition_info[condition]
    return url
