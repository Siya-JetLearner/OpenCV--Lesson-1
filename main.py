import cv2

image = cv2.imread("pika.png")

if image is None:
    print("Error image is not found!!")
    exit()

cv2.imshow("original img", image)
cv2.imwrite("saved_img.png", image)


grayimage = cv2.cvtColor(image, cv2)


cv2.waitKey(0)
cv2.destroyAllWindows()