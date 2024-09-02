import cv2
img=cv2.imread("DSCN0753.jpg")
e1=cv2.getTickCount()
print(e1)
for i in range(5,10,2):
    img=cv2.medianBlur(img,i)
e2=cv2.getTickCount()
print(e2)
T=(e2-e1)/cv2.getTickFrequency()
print(T)
cv2.imwrite("Anudeepika.jpg",img)
img1=cv2.resize(img,(512,512))
cv2.imshow("Anudeepika.jpg",img)
cv2.waitKey()
