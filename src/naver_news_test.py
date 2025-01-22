import requests # requests 라이브러리 불러오기
from bs4 import BeautifulSoup
import pandas as pd
import openpyxl

url = "https://news.naver.com/section/105"
response = requests.get(url) # url에 get 요청을 보냄
# print(response) # 200은 요청 성공을 의미
# print(response.text) # HTML 소스 출력

html = response.text

# BeautifulSoup 객체 생성
soup = BeautifulSoup(html, 'html.parser')

# section_article, as_headline 클래스 이름을 동시에 가진 대상을 선택
# print(soup.select('.section_article.as_headline'))

# 후손이면서 클래스 이름이 sa_text_strong 검색(헤드라인 뉴스 기사 가져오기)
print(soup.select('.section_article.as_headline .sa_text_strong'))

# 헤드라인 뉴스 기사 담을 리스트 객체 생성
headline_news_title = []

# 헤드라인 뉴스 기사 html 검색
headline_news_el = soup.select('.section_article.as_headline .sa_text_strong')

# 반복문을 이용하여 헤드라인 뉴스기사 타이틀을 뽑아냄
# 타이틀의 text만 추출하여 headline_news_title 리스트에 저장
for title in headline_news_el:
  title_text = title.get_text()
  headline_news_title.append(title_text)

# 헤드라인 뉴스 기사 제목 모음 출력
print(headline_news_title)

# 뉴스 제목을 반복문을 이용하여 순회
for idx, title in enumerate(headline_news_title):
  print(f"{idx + 1} : {title}")
  
data = {
  "네이버 헤드라인 뉴스 제목":headline_news_title
}

# print(data)
 
# 헤드라인 뉴스 제목을 엑셀에 저장
df = pd.DataFrame(data)
save_path = 'C:\work\python_projects\뉴스_기사.xlsx'

# 엑셀 파일로 저장
df.to_excel(save_path, index=False, engine='openpyxl')
print(f"{save_path} 로 엑셀 파일이 저장되었습니다.")  

'''
print("== 특정 키워드를 이용하여 원하는 뉴스 기사 추출하기 ==")
keyword = '넷플릭스'

find_keyword_new_title = []

# title.find(keyword)
# - 키워드에 내용안에 존재하면 0을 반환
# - 키워드가 존재하지 않으면 -1을 반환

for idx, title in enumerate(headline_news_title):  
  if title.find(keyword) != -1:
    find_keyword_new_title.append(title)

# 특정 키워드가 담긴 리스트 출력    
print(find_keyword_new_title)    
'''