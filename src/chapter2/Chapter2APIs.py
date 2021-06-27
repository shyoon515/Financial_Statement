import sys
sys.path.append("/workspace/Financial_Statement/src/common")

import UrlGenerator
import RequestFactors as rf
import UrlToInfo
from tabulate import tabulate

def check_recapitalization():
    list_of_essential_cds=[rf.corp_code, rf.bsns_year, rf.reprt_code]
    condition_info = UrlGenerator.get_url_info(list_of_essential_cds=list_of_essential_cds)
    request_url = "https://opendart.fss.or.kr/api/irdsSttus.json"
    url = UrlGenerator.get_url(request_url, condition_info)
    
    response = UrlToInfo.get_info_from_url(url=url)
    
    print(tabulate(response, headers='keys', tablefmt='psql'))
    