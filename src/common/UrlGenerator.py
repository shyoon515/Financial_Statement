#-*- coding: utf-8 -*-

import dart_fss as dart

import SearchCorp
import RequestFactors as rf

import sys
sys.path.append("/workspace/Financial_Statement/src")


# 일반화 작업



def get_url_info(list_of_essential_cds=[], list_of_selective_cds=[]):    # list 안에는 RF객체들이 들어있다.
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
            essential_cds[condition.name] = SearchCorp.get_corp_code_by_name(corp_list)    # corp_list 전달이 필요.
        else:
            value = input(condition.kor_name, "의 검색 값을 입력하세요.\n", condition.explanation)
            essential_cds[condition.name] = value

    #선택 인자 셋팅
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

        resp = input(instructions)

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
    
    condition_info = essential_cds.copy()
    condition_info.update(selective_cds)  
    return condition_info


def get_url(request_url, condition_info):    #request_url: 요청 url json 형태, condition_info: get_url_info의 반환값
    from ProgramMain import api_key
    url = request_url+"?crtfc_key="+api_key
    for condition in condition_info:
        if condition_info[condition] != '':
            condition_info[condition] = "&"+condition+"="+condition_info[condition]
    for condition in condition_info:
        url += condition_info[condition]
    return url
