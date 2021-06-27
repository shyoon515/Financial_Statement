def usr_reply(instruction_msg):
    try:
        txt = input(instruction_msg)
        return txt
    except UnicodeDecodeError:
        print("유니코드 에러가 발생하였습니다. 인코딩 불안정이 원인이므로, 한 번 더 입력해주세요. \n")
        return usr_reply(instruction_msg)
