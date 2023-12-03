import selenium
from selenium import webdriver
import time
from bs4 import BeautifulSoup
import pandas as pd


#
# 멜론 국내차트
#


# 크롬드라이버 열기
driver = webdriver.Chrome()
driver.maximize_window()  # 크롬창 크기 최대

all_data = []  # 모든 년도 데이터를 담을 리스트

# 1990년부터 2022년까지의 시대별 차트 분석
for year in range(1990, 2023):  # 1990년부터 2022년까지의 데이터를 가져옵니다.
    # 해당 년도의 멜론차트 URL 생성
    url = f'https://www.melon.com/chart/age/index.htm?chartType=YE&chartGenre=KPOP&chartDate={year}'
    
    # 해당 url 접속
    driver.get(url)
    time.sleep(2)

    # 드라이버의 현재 페이지의 html 정보 가져오기
    html = driver.page_source  
    soup = BeautifulSoup(html, 'lxml')

    # 해당 년도의 곡 정보를 저장할 리스트
    song_titles = []
    song_artists = []
    song_numbers = []

    # 멜론 차트에서 곡 제목과 가수 이름을 가져오기 (50개만)
    for entry in soup.find_all('tr', attrs={'class': 'lst50'}):
        title_elem = entry.find('div', class_='ellipsis rank01')
        artist_elem = entry.find('div', class_='ellipsis rank02')
        song_num = entry.find('div', class_='data-song-no')

        # None 체크를 통해 요소가 있는지 확인
        number = entry.find('button', class_='btn_icon like')['data-song-no'] if entry.find('button', class_='btn_icon like') else "N/A"
        title = title_elem.find('a').get_text() if title_elem and title_elem.find('a') else "N/A"
        artist = artist_elem.find('a').get_text() if artist_elem and artist_elem.find('a') else "N/A"

        song_titles.append(title)
        song_artists.append(artist)
        song_numbers.append(number)

    # DataFrame으로 변환
    data = {"year": [year] * len(song_titles), "title": song_titles, "artist": song_artists, 'number': song_numbers}
    df = pd.DataFrame(data)

    # 리스트에 DataFrame 추가
    all_data.append(df)

# 모든 년도 데이터를 하나의 DataFrame으로 결합
full_df = pd.concat(all_data, ignore_index=True)

# 웹드라이버 닫기
driver.quit()

# CSV 파일로 저장 (각 년도별로 파일을 생성합니다.)
for year in range(1990, 2023):
    filename = f"MelonChart_{year}.csv"
    df.to_csv(filename, encoding="utf-8-sig", index=False)

# 전체 데이터를 CSV 파일로 저장 한다
full_df.to_csv("MelonChart_Full.csv", encoding="utf-8-sig", index=False)
