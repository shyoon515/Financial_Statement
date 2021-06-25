import chapter2

def start():
    print("_"*70+"""
초기화면/박 회계사의 재무제표 분석법/재무상태표로 기업의 재무 상태 파악하기/자산
""")
    user_reply = int(input("""
1. 현금 및 현금성자산
2. 단기금융상품(금융기관예치금)
3. 매출채권
4. 재고자산
5. 기타 유동자산
6. 금융자산
7. 유형자산과 투자부동산
8. 무형자산
9.이연법인세자산(부채)
0.이전으로
"""))
    if user_reply == 1:
        cash()
    elif user_reply == 0:
        chapter2.start()


# 1. 현금 및 현금성자산
def cash():
    print("_"*70+"""
초기화면/박 회계사의 재무제표 분석법/재무상태표로 기업의 재무 상태 파악하기/재무상태표/현금 및 현금성자산
""")
    print("""
- 기업이 가지고 있는 현금과 수표 실물을 포함해 보통예금, 당좌예금, 양도성 예금증서(CD), CMA, MMF 등이 포함.
- 양도성 예금증서에서 분식회계나 횡령사고가 많이 발생했었음.
- 주석에 어떤 현금성자산을 보유 중인지 보여주는 경우도 가끔 있긴 하지만 뭉뚱그려 표시하는 편.
- 기업의 투명성, 경영자의 철학 또는 평판 등을 반드시 고려해야 한다.
""")
    input("이전으로 돌아가려면 아무 키나 입력하세요.")
    start()

# 2. 단기금융상품(금융기관예치금)
def cash():
    print("_"*70+"""
초기화면/박 회계사의 재무제표 분석법/재무상태표로 기업의 재무 상태 파악하기/재무상태표/단기금융상품(금융기관예치금)
""")
    print("""
- 기업이 보유한 정기예금이나 정기적금 등에서 만기가 1년 이내에 도래하면 단기금융상품으로 분류. (1년 넘게 남으면 비유동자산인 장기금융상품으로 분류.)
- 차입금이 많은 기업들은 장단기금융상품이 인출 제한된 경우들이 많다. 실질적 인출을 못하므로, 주석사항에서 인출 제한 여부를 살펴봐야 한다.
- 기업의 현금흐름이 영업, 투자, 재무에서 계속 (-)여서 자금이 마르면 기업의 보유 현금을 분석하자. 또 지난 5~10년 재무상태표의 자본금을 확인하여 그 기업이 유상증자를 빈번하게 했는가 확인하자.
""")
    input("이전으로 돌아가려면 아무 키나 입력하세요.")
    start()