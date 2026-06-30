# MNIST 손글씨 숫자 분류 (CNN)

간단한 CNN으로 0~9 손글씨 숫자를 분류하는 프로젝트입니다.

## 사용 기술
- TensorFlow / Keras
- CNN (Convolutional Neural Network)

## 실행 방법 (Google Colab)
1. `mnist_cnn.py` 내용을 Colab 새 노트북에 복사
2. `# %%` 단위로 셀을 나누어 순서대로 실행
3. 런타임 > 런타임 유형 변경 > GPU 권장 (없어도 5 epoch 정도는 빠르게 돌아갑니다)

## 결과
- 약 5 epoch 학습 후 테스트 정확도 98~99% 수준 달성
- 학습 곡선(accuracy/val_accuracy) 시각화 포함
