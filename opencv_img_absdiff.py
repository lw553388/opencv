import cv2

# # 비디오 캡처 객체 생성
# cap = cv2.VideoCapture(0)  # 0은 웹캠을 의미합니다. 파일명을 사용하여 저장된 비디오를 읽을 수도 있습니다.

while True:
    # 현재 프레임 캡처
    ret = cv2.imread('./img_data/background.png')
    current_frame = cv2.imread('./img_data/current.png')

    # # 이미지 사이즈 맞춤
    # ret = cv2.resize(src,(500,500))
    # current_frame = cv2.resize(current,(500,500))

    # 그레이 스케일로 변환
    previous_frame = cv2.cvtColor(ret, cv2.COLOR_BGR2GRAY)
    current_frame_gray = cv2.cvtColor(current_frame, cv2.COLOR_BGR2GRAY)

    # 이전 프레임과 현재 프레임의 절대 차이 계산
    frame_diff = cv2.absdiff(previous_frame, current_frame_gray)
        
    # 임계값 적용 (이진화)
    _, thresholded_diff = cv2.threshold(frame_diff, 30, 255, cv2.THRESH_BINARY)
        
    # 모션 감지 결과 표시
    cv2.imshow('Motion Detection', thresholded_diff)
        
    # 'q' 키를 누르면 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 종료 시 비디오 캡처 객체 및 윈도우 해제
# cap.release()
cv2.destroyAllWindows()
