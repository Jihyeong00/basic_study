import webbrowser

s = input("번역할 영어 문장을 입력하시오 : ")
url = "https://translate.google.co.kr/#en/kr/" + s
webbrowser.open(url)