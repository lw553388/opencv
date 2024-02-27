import cv2

# 비디오 캡처 객체 생성
cap = cv2.VideoCapture(0)  # 0은 웹캠을 의미합니다. 파일명을 사용하여 저장된 비디오를 읽을 수도 있습니다.

# 이전 프레임(카메라가 켜졌을때 프레임 저장)
_,src = cap.read()
previous = cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)
# 가우시안 블러링으로 흰색 튀는값을 잡아줌
previous_frame=cv2.GaussianBlur(previous,(0,0),1)           

while True:
    # 현재 프레임 캡처
    _, current = cap.read()
    
    # 그레이 스케일로 변환
    current_gray = cv2.cvtColor(current, cv2.COLOR_BGR2GRAY)
    # 가우시안 블러링으로 흰색 튀는값을 잡아준다
    current_frame_gray=cv2.GaussianBlur(current_gray,(0,0),1)           
    
    # 이전 프레임과 현재 프레임의 절대 차이 계산
    frame_diff = cv2.absdiff(previous_frame, current_frame_gray)
    
    # 임계값 적용 (이진화)
    # 차이값이 30 이상이면 255로 만들고, 30보다 작으면 0으로 만든다
    _, thresholded_diff = cv2.threshold(frame_diff, 30, 255, cv2.THRESH_BINARY)
    
    # 모션 감지 결과 표시
    cv2.imshow('Motion Detection', thresholded_diff)
    
    # 'q' 키를 누르면 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 종료 시 비디오 캡처 객체 및 윈도우 해제
cap.release()
cv2.destroyAllWindows()
