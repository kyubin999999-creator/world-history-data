import os
import pandas as pd

# 1. 새 GitHub 저장소(world-history-data) clone 및 최신화
repo_name = "world-history-data"
repo_url = f"https://github.com/kyubin999999-creator/{repo_name}.git"

if not os.path.exists(repo_name):
    !git clone {repo_url}
else:
    %cd {repo_name}
    !git pull
    %cd ..

# 2. 저장소 내 CSV 파일 불러오기
file_path = f"{repo_name}/world_population.csv"

try:
    df = pd.read_csv(file_path)
    
    print("=== 데이터 로드 성공 ===")
    print(f"전체 데이터 행/열 크기: {df.shape}")
    print("\n=== 컬럼 목록 ===")
    print(df.columns.tolist())
    
    print("\n=== 상위 5개 데이터 ===")
    print(df.head())

except Exception as e:
    print(f"파일을 불러오는 중 오류가 발생했습니다: {e}")
