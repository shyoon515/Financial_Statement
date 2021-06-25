import sys
sys.path.append("/workspace/Financial_Statement/src")

def start():
    print("_"*70+"""
초기화면/박 회계사의 재무제표 분석법/재무상태표로 기업의 재무 상태 파악하기
""")
    user_reply = int(input("""
1. 재무상태표
2. 자산
3. 부채
4. 자본과 자본변동표
0. 이전으로
"""))
    if user_reply == 1:
        import chapter2_1
        chapter2_1.start()
    elif user_reply == 2:
        import chapter2_2
        chapter2_2.start()
    elif user_reply == 0:
        import ProgramMain
        ProgramMain.ParkFS()


