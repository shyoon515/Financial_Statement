import dart_fss as dart


# API 키를 할당하고 인증 받는 절차
def api_key(api_key='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'):
    dart.set_api_key(api_key=api_key)
    return api_key