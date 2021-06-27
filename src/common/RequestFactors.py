class RequestFactors:
    def __init__(self, name, kor_name):
        self.name = name
        self.kor_name = kor_name
        self.explanation = ""

    def explain(self, explanation):
        self.explanation = explanation


corp_code = RequestFactors('corp_code', '기업선택')

bgn_de = RequestFactors('bgn_de', '시작일')
bgn_de.explain("검색시작 접수일자를 입력합니다. 'YYYYMMDD'의 8자리 숫자 형태로 입력합니다. 설정하지 않으면 종료일과 동일하게 설정됩니다.")

end_de = RequestFactors('end_de', '종료일')
end_de.explain("검색종료 접수일자를 입력합니다. 'YYYYMMDD'의 8자리 숫자 형태로 입력합니다. 설정하지 않으면 오늘 날짜로 설정됩니다.")

last_reprt_at = RequestFactors('last_reprt_at', '최종보고서 검색여부')
last_reprt_at.explain("최종보고서만 검색하려면 'Y', 아니면 'N'을 입력합니다.")

pblntf_ty = RequestFactors('pblntf_ty', '공시유형')
pblntf_ty.explain("""
공시유형을 설정합니다.

A : 정기공시
B : 주요사항보고
C : 발행공시
D : 지분공시
E : 기타공시
F : 외부감사관련
G : 펀드공시
H : 자산유동화
I : 거래소공시
j : 공정위공시
""")

pblntf_detail_ty = RequestFactors('pblntf_detail_ty', '공시상세유형')
pblntf_detail_ty.explain("상세유형을 입력합니다. 사이트 참조.")

corp_cls = RequestFactors('corp_cls', '법인구분')
corp_cls.explain("""
법인의 종류를 설정합니다. 없으면 전체가 조회되며, 복수조건은 불가합니다.

Y: 유가
K: 코스닥
N: 코넥스
E: 기타
""")

sort = RequestFactors('sort', '정렬')
sort.explain("""
기본적으로는 접수일자(date)를 기준으로 정렬됩니다.

date: 접수일자
crp: 회사명
rpt: 보고서명
""")

sort_mth = RequestFactors('sort_mth', '정렬방법')
sort_mth.explain("""
기본적으로는 내림차순(desc)으로 정렬됩니다.

asc: 오름차순
desc: 내림차순
""")

page_no = RequestFactors('page_no', '페이지')
page_no.explain("열람할 페이지 쪽수를 정수로 입력합니다. 기본값은 1페이지 입니다.")

page_count = RequestFactors('page_count', '검색갯수')
page_count.explain("한 번에 로드할 공시정보의 개수를 정수로 입력합니다. 기본값은 10이며, 1~100 사이의 정수로 설정 가능합니다.")

bsns_year = RequestFactors('bsns_year', '사업연도')
bsns_year.explain("사업연도 4자리 숫자를 입력하세요. 2015년 이후만 제공 가능합니다.")

reprt_code = RequestFactors('reprt_code', '보고서코드')
reprt_code.explain("""
보고서의 종류를 선택합니다.

11013: 1분기 보고서
11012: 반기보고서
11014: 3분기보고서
11011: 사업보고서
""")
