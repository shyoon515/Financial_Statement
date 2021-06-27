def prevent_error(txt):
    try:
        txt = txt
        return txt
    except UnicodeDecodeError:
        print("유니코드 에러가 발생하였습니다. 이 메시지가 연속적으로 반복된다면 개발자에게 보고 바랍니다. \n")
        txt = prevent_error(txt)
        return txt
