import cv2
import numpy as np

def detect_blue_ball(image):
    # 将图像从BGR转换为HSV
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # 定义蓝色的颜色范围
    lower_blue = np.array([100, 150, 50])
    upper_blue = np.array([140, 255, 255])

    # 创建一个掩模，保留颜色范围内的区域
    mask = cv2.inRange(hsv_image, lower_blue, upper_blue)

    # 使用形态学操作去除噪声
    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

    # 识别图像中的圆
    circles = cv2.HoughCircles(mask, cv2.HOUGH_GRADIENT, dp=1.2, minDist=30,
                               param1=50, param2=30, minRadius=10, maxRadius=100)

    # 如果检测到圆形，绘制出来
    if circles is not None:
        print("found")
        circles = np.round(circles[0, :]).astype("int")
        for (x, y, r) in circles:
            cv2.circle(image, (x, y), r, (0, 255, 0), 4)
            cv2.putText(image, "Blue Ball Detected", (x - r, y - r - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (36, 255, 12), 2)
    else:
        print("not found")

    return image