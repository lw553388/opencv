import cv2 as cv  

img = cv.imread("./img_data/starry_night.jpg")
img_convert = None

while True:
    
    # 이미지 표시
    cv.imshow("Display window", img)

    # 사용자의 키 입력 대기
    k = cv.waitKey(0)

    # 이미지 변환 (grayscale, hsv)
    if k == ord("g"):
        # 원본 이미지를 그레이스케일로 변환
        img_convert = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        cv.imshow("Convert window",img_convert)
       
    elif k == ord("h"):
        # 원본 이미지를 HSV로 변환
        img_convert = cv.cvtColor(img, cv.COLOR_BGR2HSV)
        cv.imshow("Convert window",img_convert) 
   
    # 이미지 저장
    elif k == ord("s"):
        if img_convert is not None:
            # 변환된 이미지가 있을 때만 저장
            cv.imwrite('./img_data/result.jpg', img_convert)
            
    # 종료
    if k == ord("q"):
        break

cv.destroyAllWindows()  
