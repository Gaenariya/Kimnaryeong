# 타이타닉 생존자 예측 (RandomForest)

타이타닉 승객 데이터를 이용해 생존 여부를 예측하는 머신러닝 입문용
대표 프로젝트입니다.

## 사용 기술
- scikit-learn (RandomForestClassifier)
- Pandas, Seaborn, Matplotlib

## 실행 방법 (Google Colab)
1. `titanic_ml.py` 내용을 Colab 새 노트북에 복사
2. `# %%` 단위로 셀을 나누어 순서대로 실행
3. 별도 데이터 다운로드 불필요 (seaborn 내장 데이터셋 사용)

## 결과
- 약 80% 내외의 생존 예측 정확도
- 혼동 행렬(Confusion Matrix), 특징 중요도(Feature Importance) 시각화 포함
