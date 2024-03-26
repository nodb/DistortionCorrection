import numpy as np
import cv2 as cv

def select_img_from_video(video_file, board_pattern, select_all=False, wait_msec=10, wnd_name='Camera Calibration'):
    # 비디오 열기
    video = cv.VideoCapture(video_file)
    assert video.isOpened()

    # 이미지 선택
    img_select = []
    while True:
        # 비디오에서 이미지 가져오기
        valid, img = video.read()
        if not valid:
            break

        if select_all:
            img_select.append(img)
        else:
            # 이미지 보여주기
            display = img.copy()
            cv.putText(display, f'NSelect: {len(img_select)}', (10, 25), cv.FONT_HERSHEY_DUPLEX, 0.6, (0, 255, 0))
            cv.imshow(wnd_name, display)

            # 키 이벤트 처리
            key = cv.waitKey(wait_msec)
            if key == ord(' '):            # Space: 이미지 일시 중지, 코너 표시
                complete, pts = cv.findChessboardCorners(img, board_pattern)
                cv.drawChessboardCorners(display, board_pattern, pts, complete)
                cv.imshow(wnd_name, display)
                key = cv.waitKey()
                if key == ord('\r'):       # Enter: 이미지 선택
                    img_select.append(img)
            if key == 27:                  # ESC: 이미지 선택 종료
                break

    cv.destroyAllWindows()
    return img_select

def calib_camera_from_chessboard(images, board_pattern, board_cellsize, K=None, dist_coeff=None, calib_flags=None):
    # 주어진 이미지에서 2D 코너 포인트 찾기
    img_points = []
    for img in images:
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        complete, pts = cv.findChessboardCorners(gray, board_pattern)
        if complete:
            img_points.append(pts)
    assert len(img_points) > 0

    # 체스 보드의 3D 포인트 준비
    obj_pts = [[c, r, 0] for r in range(board_pattern[1]) for c in range(board_pattern[0])]
    obj_points = [np.array(obj_pts, dtype=np.float32) * board_cellsize] * len(img_points) # Must be `np.float32`

    # 카메라 보정
    return cv.calibrateCamera(obj_points, img_points, gray.shape[::-1], K, dist_coeff, flags=calib_flags)

if __name__ == '__main__':
    video_file = 'chessboard.avi'
    board_pattern = (10, 7)
    board_cellsize = 0.025

    img_select = select_img_from_video(video_file, board_pattern)
    assert len(img_select) > 0, '이미지를 선택하지 않았습니다.'
    rms, K, dist_coeff, rvecs, tvecs = calib_camera_from_chessboard(img_select, board_pattern, board_cellsize)

    # 카메라 보정 결과 출력
    print('카메라 보정 결과')
    print(f'선택된 이미지 수 : {len(img_select)}')
    print(f'RMS 오차 : {rms}')
    print(f'카메라 행렬 (K) = \n{K}')
    print(f'왜곡 계수 (k1, k2, p1, p2, k3, ...) = {dist_coeff.flatten()}')

    # 주어진 비디오와 보정 데이터
    video = cv.VideoCapture(video_file)
    assert video.isOpened(), '주어진 입력을 읽을 수 없습니다: ' + video_file

    # 왜곡 보정 실행
    show_rectify = False
    map1, map2 = None, None
    while True:
        # 비디오에서 이미지 읽기
        valid, img = video.read()
        if not valid:
            break

        # 기하학적 왜곡 보정 (대안: `cv.undistort()`)
        info = "Original"
        if show_rectify:
            if map1 is None or map2 is None:
                map1, map2 = cv.initUndistortRectifyMap(K, dist_coeff, None, None, (img.shape[1], img.shape[0]), cv.CV_32FC1)
            img = cv.remap(img, map1, map2, interpolation=cv.INTER_LINEAR)
            info = "Distortion Correction"
        cv.putText(img, info, (10, 25), cv.FONT_HERSHEY_DUPLEX, 0.6, (0, 255, 0))

        # 이미지 보여주고 키 이벤트 처리
        cv.imshow("Geometric Distortion Correction", img)
        key = cv.waitKey(10)
        if key == ord(' '):     # Space: 일시 중지
            key = cv.waitKey()
        if key == 27:           # ESC: 종료
            break
        elif key == ord('\t'):  # Tab: 보정 모드 전환
            show_rectify = not show_rectify

    video.release()
    cv.destroyAllWindows()
