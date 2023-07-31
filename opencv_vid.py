import cv2 as cv
import time
scr = 0
fps = 5
start = time.time()
cam = cv.VideoCapture(scr)
#cc = cv.VideoWriter_fourcc(*'XVID')
#file = cv.VideoWriter('output.avi', cc, 15.0, (640, 480))

if not cam.isOpened():
   print("error opening camera")
   exit()
while True:
   # Capture frame-by-frame
   temppasse = time.time() - start
   ret, frame = cam.read()
   # if frame is read correctly ret is True
   if not ret:
      print("error in retrieving frame")
      break

   if temppasse > 1./fps:
      #img = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
      start = time.time()
      cv.imshow('frame', frame)
      #file.write(img)

   
   if cv.waitKey(1) == ord('q'):
      break

cam.release()
#file.release()
cv.destroyAllWindows()