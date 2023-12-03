import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup
import time

# CSV 파일 읽기
data = pd.read_csv("MelonChart_Full_Foreign.csv")

# 크롬드라이버 열기
driver = webdriver.Chrome()
driver.maximize_window()

# 장르 정보를 담을 리스트
genres = []

# 노래마다 반복하여 크롤링
for number in data['number']:
    # 노래 고유 번호를 이용해 해당 페이지에 접근
    url = f"https://www.melon.com/song/detail.htm?songId={number}"
    driver.get(url)
    time.sleep(2)

    # 페이지 소스 가져오기
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    # 장르 정보 가져오기
    genre_section = soup.find('dt', text='장르')
    if genre_section:
        genre = genre_section.find_next('dd').get_text()
    else:
        genre = "N/A"
    
    genres.append(genre)

# 장르 정보를 데이터프레임에 추가
data['genre'] = genres

# 1990년부터 2022년까지 10년 단위로 분할하여 CSV 파일로 저장
for decade in range(1990, 2023, 10):
    start_year = decade
    end_year = decade + 9 if decade + 9 <= 2022 else 2022
    
    # 해당 연도 범위의 데이터 추출
    decade_data = data[data['year'].between(start_year, end_year)]
    
    # 파일명 지정
    filename = f"MelonChart_{start_year}_{end_year}.csv"
    
    # CSV 파일로 저장
    decade_data.to_csv(filename, encoding='utf-8-sig', index=False)

# CSV 파일로 저장
data.to_csv("MelonChart_Full_with_Genres.csv", encoding='utf-8-sig', index=False)

# 웹드라이버 닫기
driver.quit()
