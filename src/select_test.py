import requests # requests 라이브러리 불러오기
from bs4 import BeautifulSoup

url = "https://www.naver.com/"
response = requests.get(url) # url에 get 요청을 보냄
# print(response) # 200은 요청 성공을 의미
print(response.text) # HTML 소스 출력

# 테스트용 html
html = """
<nav class="menu-box-1" id="menu-box">
  <ul>
    <li>
      <a class="naver a b c d" href="https://www.naver.com">네이버로 이동</a>      
    </li>
    <li>
      <a class="google" href="https://www.google.com">구글로 이동</a>
    </li>
    <li>
      <a class="daum" href="https://www.daum.net">다음으로 이동</a>
    </li>
  </ul>
</nav>
<nav class="menu-box-1">테스트 nav</nav>
"""   

# BeautifulSoup 객체 생성
soup = BeautifulSoup(html, 'html.parser')

# ! select_one() 테스트
# class 이름이 menu-box-1 인 엘리먼트를 검색
print("== select_one 테스트, class 검색 ==")
print(soup.select_one('.menu-box-1'))

# id 이름이 menu-box-1 인 엘리먼트를 검색
print("== select_one 테스트, id 검색 ==")
print(soup.select_one('#menu-box'))

# nav > ul > li : nav의 자식의 ul, ul의 자식인 li를 검색
print("== select_one 테스트, 선택자 검색 ==")
print(soup.select_one('nav > ul > li'))

# ! select() 테스트
# 1. select() 로 검색한 결과는 리스트 객체로 변환
# 2. 데이터가 하나이더라고 리스트 객체로 변환

# class 이름이 menu-box-1 인 엘리먼트를 검색
print("== select 테스트, class 검색 ==")
print(soup.select('.menu-box-1'))

print("== select 테스트, 선택자 검색 ==")
# >(자식 선택자) : 자식 선택자를 이용한 검색
print(soup.select('.menu-box-1 > ul > li > a'))

# 띄어쓰기(후손 선택자) : 후손 선택자를 이용한 검색
print(soup.select('.menu-box-1 a'))

# 반복문을 이용하여 데이터 순회
select_a = soup.select('.menu-box-1 a')

# v1 : 엘리먼트 속성값 가져오기
print("== 엘리먼트 속성값 가져오기 ==")
for idx, a in enumerate(select_a):
  print(a.attrs) # attrs : 엘리먼트의 속성을 딕셔너리 객체로 변환    

# v2 : 엘리먼트 href 속성값 가져오기
print("== 엘리먼트 href 속성값 가져오기 ==")
for idx, a in enumerate(select_a):
  print(a.attrs['href']) # href 키로 접근하여 속성값 가져오기

# v3 : 엘리먼트 class 속성값 가져오기
print("== 엘리먼트 class 속성값 가져오기 ==")
for idx, a in enumerate(select_a):
  print(a.attrs['class']) # class 키로 접근하여 속성값 가져오기

# v4 : 엘리먼트의 text 값 가져오기
print("== 엘리먼트의 text 값 가져오기 ==")  
for idx, a in enumerate(select_a):
  print(f"{idx} : {a.get_text()}")  