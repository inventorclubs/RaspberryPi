import cv2
from datetime import datetime
import subprocess
import signal
import os
import time

def send():
    subprocess.Popen("python3 send.py", stdout=subprocess.PIPE, shell=True, preexec_fn=os.setsid)

cap = cv2.VideoCapture(0)  # Sets camera feed number
fourcc = cv2.VideoWriter_fourcc(*'XVID')  # Sets codec ('M', 'J', 'P', 'G') or (*'DIVX')
out = cv2.VideoWriter("output.avi", fourcc, 20, (640, 480))

capture_duration = 3
start_time = time.time()
while( int(time.time() - start_time) < capture_duration ):
    ret, frame = cap.read()
    if ret==True:
        frame = cv2.flip(frame,0)
        # write the flipped frame
        out.write(frame)
        cv2.imshow('frame',frame)
    else:
        break


cap.release()
out.release()
send()
cv2.destroyAllWindows()
