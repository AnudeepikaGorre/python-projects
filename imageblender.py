import cv2
img1=cv2.imread("DSCN0645.jpg")
img2=cv2.imread("DSCN0643.jpg")

img1 = cv2.resize(img1,(512,512))
img2 = cv2.resize(img2,(512,512))

dst = cv2.addWeighted(img1,0.5,img2,0.3,0)

cv2.imwrite("./added.png",dst)
cv2.imshow('dst',dst)
cv2.waitKey()
cv2.destroyAllWindows()