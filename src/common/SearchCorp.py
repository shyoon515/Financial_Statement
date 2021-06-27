import SolutionForUnicodeError as ue
import pandas as pd
import numpy as np


# 기업 이름으로 검색 후, 고유번호 8자리를 반환. input은 ProgramMain.py에 있는 전역변수 corp_list를 넣어야 한다. 약간만 조작하면 stock_code값과 modify_date도 가져올 수 있는 함수.
def get_corp_code_by_name(corp_list):
    corp_name = ue.usr_reply("검색할 기업 이름을 입력하세요.\n")

    try:
        condition = (corp_list['corp_name'] == corp_name)
        result = corp_list[condition]
        result_np = result.values

        return result_np[0,1]
    except IndexError:
        print("검색한 기업이 존재하지 않습니다. 다시 입력하세요.\n")
        return get_corp_code_by_name(corp_list)
