import cv2 
import math
import numpy as np
# capture frames from a camera
cap = cv2.VideoCapture(0)
 
# loop runs if capturing has been initialized.
while 1: 
 
    # reads frames from a camera
    ret, g11 = cap.read() 
    # convert to gray scale of each frames
    img = cv2.cvtColor(g11, cv2.COLOR_BGR2GRAY)
    size = img.shape
    r,c=size
    y2 = np.zeros(size, dtype=np.uint8)
    for y in range(0,r):
        for x in range(0,c):
            x1 = x-int(c/2)
            y1 = y-int(r/2)
            if(y1==0):
                y1=y1+1
            q = math.atan(x1/y1)
            if abs(x1)>abs(y1):
                jt = img[y,x]
                l=int(c/2)+x1-(x1/5)*(math.cos(2*q))
                if(l>=c or l<0):
                    continue
                y2.itemset((int(y),int(l)),jt)
            else:
                jt = img[y,x]
                l=int(r/2)+y1+(y1/5)*(math.cos(2*q))
                if(l>=r or l<0):
                    continue
                y2.itemset((int(l),int(x)),jt)

    for y in range(0,r-1):
        x =0
        while x <c:
            x1 = x
            while y2.item(y,x) == 0 and x<(c-1) :
                y2.itemset((y,x), y2.item(y,x-1))
                x = x+1
            if x> x1:
                x = x-1  # the extra increment in x inside while loop is removed
            x = x+1

#    for x in range(0,c-1):
#        y =0
#        while y <r:
#            y1 = y
#            while y2.item(y,x) == 0 and y<(r-1) :
#                y2.itemset((y,x), y2.item(y-1,x))
#                y = y+1
#            if y> y1:
#                y = y-1  # the extra increment in x inside while loop is removed
#            y = y+1


    cv2.imshow('img',y2)
 
    # Wait for Esc key to stop
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
 
# Close the window  
cap.release()
 
# De-allocate any associated memory usage
cv2.destroyAllWindows()
