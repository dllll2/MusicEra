# MusicEra

멜론 시대별 차트에서 1990년부터 2022년까지의 노래정보를 크롤링을 통해

데이터를 수집, 가공 하여 원하는 새로운 데이터를 추출하는 프로젝트

## 파일 구성

- 차트 크롤링
  - melon_crawling.py (국내 차트를 크롤링하는 코드)
  - melon_crawling_foreign.py (해외 차트를 크롤링하는 코드)
  

- 장르 크롤링 (장르에 대한 정보는 차트에 없고 곡 상세페이지에 존재하기 때문에 다른 페이지에서 따로해줘야함)
  - genre.py (국내 곡 장르 크롤링)
  - foreign_genre.py (해외 곡 장르 크롤링)
    

- 1111.py
  - 크롤링해온 데이터를 10년단위로 쪼개서 따로 저장하는 코드인데 오히려 자료를 쪼개는게

    더 불편한 상황이 있어서 쓰진 않음
  

## 데이터 정제 및 시각화

- 크롤링해온 데이터를 가공하고 여러가지 시각화를 진행
    - Korea_Music_era.ipynb (국내)
    - Foreign_Music_era.ipynb (해외)



![top10 장르별 노래수(국내)](https://github.com/dllll2/MusicEra/assets/105922173/b6bc74e6-2ad2-42e2-a19b-3f5b7a1eb69d)


1990년 부터 2022년까지의 장르별 노래수를 시각화한 그래프


![연도별 상위 5개 장르의 변화(국내)](https://github.com/dllll2/MusicEra/assets/105922173/06be894b-aa1d-4e9b-af55-9128e9ad8b47)

1990년 부터 2022년 까지의 장르별 노래수의 변화를 시각화한 그래프



![2023년에 유행할 음악 장르(국내)](https://github.com/dllll2/MusicEra/assets/105922173/99b25dab-edaa-4c13-a65e-0ed76cc25c2d)


2023년에 유행할 음악 장르에 대한 예측을 시각화한 그래프


![연대별 유행한 음악장르 top3(국내)](https://github.com/dllll2/MusicEra/assets/105922173/2d7d77fc-3173-4889-97e1-442b989cea6d)


연대별로 유행했던 음악장르를 시각화한 그래프
