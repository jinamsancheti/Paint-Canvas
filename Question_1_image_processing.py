import numpy as np 
import cv2 

draw = False #if true then mouse button is pressed or else not 

def connect(x):
    pass              

# function which helps us draw 

def doodle(event,x,y,flag,jay):   
    global draw  
    if(event == cv2.EVENT_LBUTTONDOWN):  
        draw = True  
    if (event == cv2.EVENT_MOUSEMOVE):  
        if draw == True:  
            cv2.circle(img2,(x,y),t,(b,g,r),-1)  
    if(event == cv2.EVENT_LBUTTONUP):  
        draw = False
        
cv2.namedWindow("canvas")    

# Create a white image on which we can draw 

img2 = np.ones((1024,1024,3), np.uint8)*255

# making track bars for selecting the colour and thickness 

def colour_select():
    img = np.zeros([300,500,3],np.uint8)*255
    cv2.namedWindow("Colour Picker")
    global r,g,b,t
    str = "0 : OFF \n 1 : ON"

    cv2.createTrackbar(str, "Colour Picker", 0, 1, connect)
    cv2.createTrackbar("R", "Colour Picker", 0, 255, connect)
    cv2.createTrackbar("G", "Colour Picker", 0, 255, connect)
    cv2.createTrackbar("B", "Colour Picker", 0, 255, connect)
    cv2.createTrackbar("Thickness", "Colour Picker", 1, 40, connect)
    # we randomly choose size to be b/w 1 and 40 

    # synchronisation of both the windows !!
    while True:
        cv2.imshow("Colour Picker",img)
        k = cv2.waitKey(1) & 0xFF 
        if k == 27 : 
            break 
        
        s = cv2.getTrackbarPos(str, "Colour Picker")
        r = cv2.getTrackbarPos("R", "Colour Picker")
        g = cv2.getTrackbarPos("G", "Colour Picker")
        b = cv2.getTrackbarPos("B", "Colour Picker")
        t = cv2.getTrackbarPos("Thickness", "Colour Picker")
        if s == 0 :
            img[:] = 0
        else :
            img[:] = [b,g,r]
        cv2.setMouseCallback("canvas",doodle)
        cv2.imshow("canvas",img2)
        

colour_select() 

cv2.destroyAllWindows()



