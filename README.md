# DistortionCorrection 📷

## ✍ 소개
- 카메라 캘리브레이션 및 렌즈 왜곡 보정 프로그램입니다.

## 🗂️ 사용 기술
- Python
- OpenCV

## 💻 기능
- 작동 순서 : 캘리브레이션 모드 진입 → 캘리브레이션 측정 완료(콘솔 출력) → 왜곡 보정 모드 진입 → 왜곡 보정 여부 지정

### 1. 캘리브레이션 모드
클리브레이션 측정 방법
1. 원하는 화면에서 Space bar를 클릭 후 Enter 클릭(이미지 선택)
2. 1번을 최소 3번 반복
3. Esc를 클릭하여 캘리브레이션 측정(이미지 선택) 종료

화면 기능
- Nselect : 캘리브레이션(정밀도 측정)을 위해 캡쳐한 이미지 개수

### 2. 콘솔 출력
카메라 보정 결과
- 선택된 이미지 수
- RMS 오차
- 카메라 행렬 (K)
- 왜곡 계수 (k1, k2, p1, p2, k3, ...)

### 3. 왜곡 보정 모드
왜곡 보정 방법
1. Tab을 클릭하여 왜곡 보정 적용/미적용(토글)
2. ESC를 클릭하여 프로그램 종료

화면 기능
- Original : 보정 미적용
- Distortion Correction : 보정 적용


## 📸 렌즈 왜곡 보정 결과 데모
- 카메라 : 갤럭시S22U 0.6배율
  
![image](https://github.com/nodb/DistortionCorrection/assets/71473708/6f5bce4d-bb1d-4ea3-848e-b0708c2627c6)



## 시연
- [동영상 시연 1](https://youtu.be/1BX8ZkZdgUM)
- 원본 ![원본](https://github.com/nodb/DistortionCorrection/assets/71473708/4babf917-f81c-4fc2-8716-bc41799386d1)
- 왜곡 보정 ![왜곡 보정](https://github.com/nodb/DistortionCorrection/assets/71473708/eecd430d-c276-41dc-ba08-d030370e4615)
- [동영상 시연 2](https://youtu.be/IO10TNj8Lrc)
- 원본 ![원본](https://github.com/nodb/DistortionCorrection/assets/71473708/64b1ffeb-56fe-4d64-a751-be104160910d)
- 왜곡 보정 ![왜곡 보정](https://github.com/nodb/DistortionCorrection/assets/71473708/8f76a7c9-c69c-47fe-8154-04aec58be9ca)


