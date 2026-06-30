# 전이학습을 이용한 고양이 vs 개 이미지 분류

ImageNet으로 사전학습된 MobileNetV2를 베이스로 사용해 적은 학습만으로
고양이/개 이미지를 분류하는 전이학습(Transfer Learning) 프로젝트입니다.

## 사용 기술
- TensorFlow / Keras
- MobileNetV2 (사전학습 모델, 전이학습)
- TensorFlow Datasets (cats_vs_dogs)

## 실행 방법 (Google Colab)
1. `transfer_learning.py` 내용을 Colab 새 노트북에 복사
2. `# %%` 단위로 셀을 나누어 순서대로 실행
3. 런타임 > GPU 권장

## 결과
- 3 epoch만으로도 90% 내외의 검증 정확도 달성 (전이학습의 장점)
- 학습 곡선 및 예측 결과 시각화 포함
