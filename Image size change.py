import cv2
vid =cv2.VideoCapture(0)
width=vid.get(cv2.CAP_PROP_FRAME_WIDTH) #getting width of the image
height=vid.get(cv2.CAP_PROP_FRAME_HEIGHT)#getting height of the image
fps=vid.get(cv2.CAP_PROP_FPS) #Frame/seconds
print("width %d,height height%d" %(width,height))
print("fps %f" %(fps))
grabbed,frame=vid.read()


fourcc=cv2.VideoWriter.fourcc(*"XVID")

videowriter=cv2.VideoWriter(".Anu.avi",fourcc,15,(int(width),int(height)))
i=1

while grabbed:
    print(i,"\n")

    i=i+1
    videowriter.write(frame)
    grabbed,frame=vid.read()
vid.release()
videowriter.release()
