# 기업 이름으로 검색 후, 고유번호 8자리를 반환
def get_corp_code_by_name(corp_list):
    corp_list = corp_list
    corp_name = input("검색할 기업 이름을 입력하세요.\n")
    try:
        corp_code = corp_list.find_by_corp_name(corp_name=corp_name)[0]
        corp_code = corp_code._info['corp_code']
        return corp_code
    except TypeError:
        print("검색한 기업이 존재하지 않습니다. 다시 입력하세요.")
        SearchCorp()