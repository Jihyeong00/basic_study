"""
영어 단어와 한글 단어를 
"""

initial_dic = {"kr_dic": {"사과": "apple", "포도": "grape"}, "en_dic": {"apple": "사과", "grape": "포도"}}

message = "1. 영어/한글 단어 뜻 검색, 2. 단어 등록, 3. 단어 삭제, 4.종료 \n"


def is_object_value(value, obj):
    return value in obj


def search_en(dic):
    while True:
        search_keyword = input("검색할 영어 명을 입력 해 주세요, 생각이 안 난다면 q를 입력 해 주세요 :\n")
        if search_keyword == 'q':
            break
        if not is_object_value(search_keyword, dic['en_dic']):
            print("없는 영어명 입니다. 다시 입력 해 주세요.")
            continue

        print(search_keyword + "의 한글 명은 \"" + dic['en_dic'][search_keyword] + "\" 입니다.")
        break


def search_kr(dic):
    while True:
        search_keyword = input("검색할 한글 명을 입력 해 주세요, 생각이 안 난다면 q를 입력 해 주세요 :\n")
        if search_keyword == 'q':
            break
        if not is_object_value(search_keyword, dic['kr_dic']):
            print("없는 한글명 입니다. 다시 입력 해 주세요.")
            continue

        print(search_keyword + "의 영어 명은 \"" + dic['kr_dic'][search_keyword] + "\" 입니다.")
        break


def search(dic):
    while True:
        search_type = input("검색할 단어의 타입을 알려주세요 (ex: 한글, 영어, q), 검색하기 싫다면 q를 눌러주세요\n")
        if search_type == "한글":
            search_kr(dic)
        elif search_type == "영어":
            search_en(dic)
        elif search_type == "q":
            print("검색을 종료합니다.")
            break
        else:
            print("잘못 입력 하였습니다.")


def register(dic):
    while True:
        new_dic = dic
        register_en_keyword = input("등록할 사전의 영여 명을 입력 해 주세요, 생각이 안 난다면 q를 입력 해 주세요 :\n")
        if register_en_keyword == 'q':
            return new_dic
        if is_object_value(register_en_keyword, dic['en_dic']):
            print("있는 영어명 입니다. 다시 입력 해 주세요.")
            continue

        register_kr_keyword = input("등록할 한글 명을 입력 해 주세요. \n")
        new_dic['en_dic'][register_en_keyword] = register_kr_keyword
        new_dic['kr_dic'][register_kr_keyword] = register_en_keyword
        print(f"{register_en_keyword} 해당 단어가 {register_kr_keyword} 뜻으로 등록 되었습니다.")
        break
    return new_dic


def delete_keyword(dic):
    new_dic = dic
    while True:
        delete_en_keyword = input("삭제할 사전의 영여 명을 입력 해 주세요, 생각이 안 난다면 q를 입력 해 주세요 :\n")
        if delete_en_keyword == 'q':
            return new_dic
        if not is_object_value(delete_en_keyword, dic['en_dic']):
            print("없는 영어명 입니다. 다시 입력 해 주세요.")
            continue
        delete_kr_keyword = new_dic['en_dic'][delete_en_keyword]
        del new_dic['kr_dic'][delete_kr_keyword]
        del new_dic['en_dic'][delete_en_keyword]
        break

    return new_dic


def dic_play():
    dic = initial_dic
    while True:
        select = input(message)
        if select == "1":
            search(dic)
        elif select == "2":
            dic = register(dic)
        elif select == "3":
            dic = delete_keyword(dic)
        elif select == "4":
            print("프로그램을 종료 합니다. \n")
            break
        else:
            print("잘못된 입력 입니다. 다시 입력 해 주세요")


if __name__ == "__main__":
    dic_play()
