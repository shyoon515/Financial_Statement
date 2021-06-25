import dart_fss as dart




# 검색 설정을 유저에게 받아서 dict로 반환
def GetBrowseInfo(corp_list):
    import SearchCorp
    
    corp_list=corp_list
    browse_info = {'corp_code':"", 'bgn_de':"", 'end_de':"", 'last_reprt_at':"", 'pblntf_ty':"", 'pblntf_detail_ty':"", 'corp_cls':"", 'sort':"", 'sort_mth':"", 'page_no':"", 'page_count':""}
    resp = 1    
    while resp!=0:
        resp = input("\n\ncorp_code, bgn_de, end_de, last_reprt_at, pblntf_ty, pblntf_detail_ty, corp_cls, sort, sort_mth, page_no, page_count 중 추가할 검색 요소를 입력하세요. 없으면 0을 입력하세요.\n")
        if resp == "0":
            resp=0
            break
        
        if resp == "corp_code":
            browse_info["corp_code"] = SearchCorp.get_corp_code_by_name(corp_list)
        elif resp in browse_info:
            value = input(resp+"의 값을 입력하세요.")
            browse_info[resp] = value
        else:
            print("key 요소 입력 오류, 다시 입력하세요.")
    return browse_info

# 공시 정보 api의 url을 반환
def GetBrowseUrl(api_key, corp_list):
    api_key = api_key
    corp_list = corp_list
    browse_info = GetBrowseInfo(corp_list)
    url = "https://opendart.fss.or.kr/api/list.xml?crtfc_key="+api_key
    for value in browse_info:
        if browse_info[value] != "":
            browse_info[value] = "&"+value+"="+browse_info[value]
    for value in browse_info:
        url += browse_info[value]
    print(url)
    return url