# AI/CV 미니 프로젝트 포트폴리오 (5개)

인공지능공학과 GitHub 포트폴리오용으로 만든 쉬운 난이도의 AI/CV 미니 프로젝트
5개입니다. 모두 Google Colab에서 별도 환경설정 없이 바로 실행 가능합니다.

## 프로젝트 목록

| # | 프로젝트 | 핵심 기술 |
|---|---|---|
| 01 | [MNIST 손글씨 숫자 분류](./01_mnist_cnn) | CNN, Keras |
| 02 | [YOLOv8 객체 탐지](./02_yolo_detection) | Ultralytics YOLOv8 |
| 03 | [전이학습 이미지 분류 (고양이 vs 개)](./03_transfer_learning) | MobileNetV2, Transfer Learning |
| 04 | [OpenCV 얼굴 검출](./04_face_detection) | Haar Cascade, OpenCV |
| 05 | [타이타닉 생존자 예측](./05_titanic_ml) | RandomForest, scikit-learn |

## 사용 방법
각 폴더의 `.py` 파일을 열어 내용을 통째로 Google Colab 새 노트북에 붙여넣은 뒤,
`# %%` 표시를 기준으로 셀을 나누어 위에서부터 순서대로 실행하면 됩니다.
(VS Code의 Python 확장이나 Jupyter에서도 `# %%`는 셀 구분으로 인식됩니다.)

## GitHub 업로드 팁
- 폴더 구조를 그대로 레포지토리에 올리면 됩니다 (`01_mnist_cnn/`, `02_yolo_detection/` ...)
- 각 폴더 안의 `README.md`가 해당 프로젝트 설명이고, 이 최상위 `README.md`는
  전체 레포 소개(메인 페이지)로 사용하면 됩니다.
- 실행 결과 스크린샷을 직접 캡처해서 각 폴더에 추가하면 포트폴리오 완성도가 더 높아집니다.
