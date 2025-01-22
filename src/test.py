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
      <a class="naver" href="https://www.naver.com">네이버로 이동</a>      
    </li>
    <li>
      <a class="google" href="https://www.google.com">구글로 이동</a>
    </li>
    <li>
      <a class="daum" href="https://www.daum.net">다음으로 이동</a>
    </li>
  </ul>
</nav>
"""   

# BeautifulSoup 객체 생성
soup = BeautifulSoup(html, 'html.parser')

# ! find 사용법
# html 상에 있는 첫 번째 li를 가져온다.
print(soup.find('li')) 

# html 상에 있는 첫 번째 a를 가져온다.
print(soup.find('a'))

# html 상에 있는 첫 번째 a를 가져온다. / class 이름이 naver2 인 녀석을 가져옴
print(soup.find('a', class_="naver2"))

# ! find_all 사용법
# html 상에 있는 모든 li를 검색해서 모두 가져온다.
# 가져온 데이터는 리스틑 객체로 변환된다.
print(soup.find_all('li'))

# 위 코드를 반복문을 이용한 순회
find_li = soup.find_all('li');

for idx, li in enumerate(find_li):
  print(f"{idx} : {li}")
  
# html 상에 있는 모든 a를 검색해서 모두 가져온다.
print(soup.find_all('a'))  

find_a = soup.find_all('a')

for idx, a in enumerate(find_li):
  a_text = a.get_text().strip()  
  print(f"{idx} : {a_text}")