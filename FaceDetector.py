import cv2
import shutil
import  os
face_cascade = cv2.CascadeClassifier("C:\\Users\\anupa\Downloads\\tefoLOGIC\\pythonProject\\haarcascade_frontalface_default.xml")
vid= cv2.VideoCapture(0)
#vid=cv2.VideoCapture("C:\\Users\\anupa\\Downloads\\tefoLOGIC\\pythonProject\\power_star")
width=vid.get(cv2.CAP_PROP_FRAME_WIDTH)
height=vid.get(cv2.CAP_PROP_FRAME_HEIGHT)
fps=vid.get(cv2.CAP_PROP_FPS)
print('width %d,height %d' % (width,height))
print('fps %f ' %(fps))
grabbed,frame= vid.read()
if os.path.exists("./output"):
    shutil.rmtree("./output")
os.mkdir('./output')
i=0
grabbed,frame=vid.read()
while grabbed:
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,1.3,5)
    i=i+1
    print("frame= ",i)
    j=1
    for (x,y,w,h) in faces:

             img=cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
             roi_gray=gray[y:y+h,x:x+w]
             roi_color=img[y:y+h,x:x+w]
             #cv2.imwrite("./output/frame_%dface.png" %(len(os.listdir("./output"))),roi_color)
             cv2.imshow('frame',frame)
             cv2.waitKey(100)
             cv2.imwrite("./output/%dframe_%dface.jpg" %(i,j),roi_color)
             j=j+1
             grabbed,frame =vid.read()

vid.release()