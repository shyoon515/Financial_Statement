url = "https://opendart.fss.or.kr/api/corpCode.xml?crtfc_key="+api_key
resp = ul.urlopen(url)

# 수신된 resp의 bytes를 Buffer에 쌓고 zip file을 로드한다.
with ZipFile(BytesIO(resp.read())) as zf:
    file_list = zf.namelist()
    while len(file_list) > 0:
        file_name = file_list.pop()
        corpCode = zf.open(file_name).read().decode()

        
tree = elemTree.fromstring(corpCode)

XML_stocklist = tree.findall("list")
corp_code = [x.findtext("corp_code") for x in XML_stocklist]
corp_name = [x.findtext("corp_name") for x in XML_stocklist]
stock_code = [x.findtext("stock_code") for x in XML_stocklist]
modify_date = [x.findtext("modify_date") for x in XML_stocklist]

stocklist = {}
for i in range(len(corp_code)):
    stocklist[corp_code[i]] = (corp_name[i], stock_code[i], modify_date[i])

for i in corp_code:
    print(stocklist[i])