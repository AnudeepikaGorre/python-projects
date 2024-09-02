import cv2
#face=cv2.cascadeClassifier('./haarcascades/casacde.xml')
#face=cv2.CascadeClassifier('cascade.xml')
face=cv2.CascadeClassifier("C:\\Users\\anupa\\OneDrive\\Desktop\\New folder\\cascade.xml")

#image=cv2.imread('wattakay.jpg') #the file to check test2.jpg
image=cv2.imread("C:\\Users\\anupa\\Downloads\\tefoLOGIC\\pythonProject\\wattakay.jpg")
grey=cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
faces=face.detectMultiScale(grey,1.1,4)

for (x,y,w,h) in faces:
    cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),3)
    cv2.imshow('image',image)
    cv2.imwrite("mine.jpg",image)
cv2.waitKey(8000)
