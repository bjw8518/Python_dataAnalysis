import pandas as pd
from sqlalchemy import create_engine, types
import os

# Oracle 데이터베이스 연결 설정

id = 'kopo'
pw = 'kopo'
ip = '192.168.110.112'
port = '1521'
dbName = 'orcl'

engine = create_engine(f'oracle://{id}:{pw}@{ip}:{port}/{dbName}', echo=True)

#https://www.entity.co.kr/entry/62-%ED%8C%8C%EC%9D%BC-%EC%A1%B4%EC%9E%AC%EC%97%AC%EB%B6%80-%ED%99%95%EC%9D%B8-%EB%94%94%EB%A0%89%ED%86%A0%EB%A6%AC-%EC%A1%B4%EC%9E%AC%EC%97%AC%EB%B6%80%EB%8A%94-%EC%96%B4%EB%96%BB%EA%B2%8C-%ED%99%95%EC%9D%B8%ED%95%98%EB%82%98%EC%9A%94
path = '../'
for root, dirs, files in os.walk(path):
    for file in files:
        if file.endswith('.csv') or file.endswith('.xlsx'):
            file_path = os.path.join(root, file)

            #파일읽기
            if file.endswith('.csv'):
                data = pd.read_csv(file_path)
            else:
                data = pd.read_excel(file_path)

            #nan제거
            data = data.dropna()

            #테이블이름파일명으로
            tableName = file.split('.')[0]
            tableName = tableName.lower()

            #object로
            objectColumns = list(data.columns[data.dtypes == 'object'])
            typeDict={}
            maxLen = 100

            for i in range(0, len(objectColumns)):
                typeDict[objectColumns[i]] = types.VARCHAR(maxLen)
                
            data.to_sql(name=tableName, if_exists="replace", con=engine, dtype=typeDict, index=False)