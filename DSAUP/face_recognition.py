import cv2

faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


OUTPUT_SIZE_WIDTH = 700
OUTPUT_SIZE_HEIGHT = 600

capture = cv2.VideoCapture(2)

cv2.namedWindow("base-image", cv2.WINDOW_AUTOSIZE)
cv2.namedWindow("result-image", cv2.WINDOW_AUTOSIZE)

cv2.moveWindow("base-image", 20, 200)
cv2.moveWindow("result-image", 640, 200)

cv2.startWindowThread()

rectangleColor = (0, 100, 255)

while(True):
    rc, fullSizeBaseImage = capture.read()

    baseImage = cv2.resize(fullSizeBaseImage, (520, 420))

    pressedKey = cv2.waitKey(2)
    if (pressedKey == ord('Q')) | (pressedKey == ord('q')):
        cv2.destroyAllWindows()
        exit(0)

    resultImage = baseImage.copy()

    gray_image = cv2.cvtColor(baseImage, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray_image, 1.3, 5)

    maxArea = 0
    x = 0
    y = 0
    w = 0
    h = 0

    for (_x, _y, _w, _h) in faces:
        if _w * _h > maxArea:
            x = _x
            y = _y
            w = _w
            h = _h
        maxArea = w * h
        if maxArea > 0:
            cv2.rectangle(resultImage, (x - 10, y - 20), (x + w + 10, y + h + 20), rectangleColor, 2)

    largeResult = cv2.resize(resultImage, (OUTPUT_SIZE_WIDTH, OUTPUT_SIZE_HEIGHT))

    cv2.imshow("base-image", baseImage)
    cv2.imshow("result-image", largeResult)
