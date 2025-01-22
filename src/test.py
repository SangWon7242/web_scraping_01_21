import requests # requests 라이브러리 불러오기

url = "https://www.naver.com/"
response = requests.get(url) # url에 get 요청을 보냄
print(response) # 200은 요청 성공을 의미
print(response.text) # HTML 소스 출력