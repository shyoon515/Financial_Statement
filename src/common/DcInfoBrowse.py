from tabulate import tabulate

import RequestFactors as rf
import UrlGenerator
import UrlToInfo


# 공시 정보를 검색하여, pandas DataFrame 객체로 응답정보를 반환해준다.
def browse_dc_info():
    list_of_selective_cds=[
        rf.corp_code, rf.bgn_de, rf.end_de, rf.last_reprt_at, rf.pblntf_ty, rf.pblntf_detail_ty, rf.corp_cls, rf.sort, rf.sort_mth, rf.page_no, rf.page_count
    ]
    condition_info = UrlGenerator.get_url_info(list_of_selective_cds=list_of_selective_cds)

    request_url = "https://opendart.fss.or.kr/api/list.json"
    url = UrlGenerator.get_url(request_url=request_url, condition_info=condition_info)    # '공시정보' API에 접속할 url을 저장. url은 이 메쏘드에서 사용자로부터 정보를 받아 형성된다.
    response = UrlToInfo.get_info_from_url(url)    # 만들어진 url로 '공시정보'에서 모든 인자들을 pandans DataFrame 객체로 반환해준다.
    return response