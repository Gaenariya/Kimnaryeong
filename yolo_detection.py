# YOLOv8을 이용한 객체 탐지

Ultralytics YOLOv8 사전학습 모델로 이미지 속 객체(사람, 차, 동물 등)를 탐지하는 프로젝트입니다.

## 사용 기술
- Ultralytics YOLOv8 (yolov8n, nano 모델)
- OpenCV, Matplotlib

## 실행 방법 (Google Colab)
1. `yolo_detection.py` 내용을 Colab 새 노트북에 복사
2. `# %%` 단위로 셀을 나누어 순서대로 실행
3. 마지막 셀에서 본인이 가진 이미지를 직접 업로드해서 테스트 가능

## 결과
- 샘플 이미지(bus.jpg)에서 사람, 버스 등 객체를 바운딩 박스와 confidence score로 표시
- 클래스명, 신뢰도(confidence) 출력
