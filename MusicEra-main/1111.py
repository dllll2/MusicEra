import pandas as pd

# CSV 파일 읽기
data = pd.read_csv("src/MelonChart_Separated_Genres.csv")

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

# CSV 파일 읽기
data2 = pd.read_csv("src/MelonChart_Full_with_Genres_Foreign.csv")

# 1990년부터 2022년까지 10년 단위로 분할하여 CSV 파일로 저장
for decade in range(1990, 2023, 10):
    start_year = decade
    end_year = decade + 9 if decade + 9 <= 2022 else 2022

    # 해당 연도 범위의 데이터 추출
    decade_data = data2[data2['year'].between(start_year, end_year)]
    
    # 파일명 지정
    filename = f"src/MelonChart_foreign_{start_year}_{end_year}_1.csv"
    
    # CSV 파일로 저장
    decade_data.to_csv(filename, encoding='utf-8-sig', index=False)

