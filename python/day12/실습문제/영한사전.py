message = "1. 영어/한글 단어 뜻 검색, 2. 단어 등록, 3. 단어 삭제, 4.종료"


def dic():
    dic = {"kr_dic": {}, "en_dic": {}}
    while True:
        select = input(message)
        if select == 1:
            return dic =  search()
        elif select == 2:
            return dic = register()
        elif select == 3:
            return dic =  deleteKeyword()
        else:
            break


if __name__ == "__main__":
    dic()
