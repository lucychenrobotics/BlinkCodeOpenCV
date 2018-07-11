import cv2
import numpy
from scipy import stats
import time
import os
import csv
numpy.set_printoptions(threshold=numpy.nan)



cap = cv2.VideoCapture('/Users/lucychen/Downloads/testEye2.wmv')
i = 0
fps = cap.get(cv2.CAP_PROP_FPS)
length = cap.get(cv2.CAP_PROP_FRAME_COUNT)
print(length)
print("this is length")
a = numpy.empty((3,int(length),))
a[:] = numpy.nan
#print(a)
print(length)

cap.set(1, int(75*fps))
ret, frame = cap.read()
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
print(gray.shape)

numTimes = 0

#average the numbers less than 50 to get the average of the black colors
sumBlack = 0
numBlack = 0
for i in range(gray.shape[0]):
    for j in range(gray.shape[1]):
        if(gray[i,j] < 50):
            sumBlack += gray[i,j]
            numBlack += 1
minThres = (sumBlack/numBlack)*gray.shape[0]*gray.shape[1]+150000
print(minThres)

while(i < length):
    # Capture frame-by-frame
    #cap.set(1, 100)
    ret, frame = cap.read()
    #print(frame)
    #print(frame.shape)
    if ret == False:
        break
    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #print(gray)
    a[1, i] = cv2.sumElems(gray)[0]
    #print(cv2.sumElems(gray))
    #print("hi?")
    #print(a[1,i])
    #print(i)

    if(a[1,i] < minThres): numTimes += 1
    else: numTimes = 0
    
    font                   = cv2.FONT_HERSHEY_SIMPLEX
    bottomLeftCornerOfText = (10,100)
    fontScale              = 2
    fontColor              = (255,255,255)
    lineType               = 2

    cv2.putText(gray, str(cv2.sumElems(gray)[0]), 
        bottomLeftCornerOfText, 
        font, 
        fontScale,
        fontColor,
        lineType)

    cv2.putText(gray, str(i), 
        (10,150), 
        font, 
        fontScale,
        fontColor,
        lineType)

    cv2.putText(gray, str(numTimes),  
        (10,200), 
        font, 
        fontScale,
        fontColor,
        lineType)




    # Display the resulting frame
    cv2.imshow('frame',gray)
    
    # Write some Text
    time.sleep(.20) 


    if cv2.waitKey(1) & 0xFF == ord('q'):
        time.sleep(3) 

    i+=1
# When everything done, release the capture
print("yo done loading i guess")
#for arr in a: #do not need the loop at this point, but looks prettier
#    print(stats.describe(arr))

print("Finished thing here")
print(i)
#numpy.save("testCV2", a)
#numpy.savetxt("testCV", a)



