#!/usr/bin/python3
import cv2
import numpy as np
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from drawing_tools import *

drawing = False # true if mouse is pressed
mode = True # Press 'm' to toggle to curve
color_1 = (255,0,0)
color_2 = (0,255,0)
ix,iy = -1,-1
img = np.zeros((512,512,3), np.uint8)

def draw_line(event,x,y,flags,param):
    global img,ix,iy,drawing,mode
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if mode == True:
            cv2.line(img,(ix,iy),(x,y),color_1,5)
        else:
            cv2.line(img,(ix,iy),(x,y),color_2,5)
            # cv2.circle(img,(x,y),5,(0,0,255),-1)


def draw_circle(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img,(x,y),100,(255,0,0),-1) 
# Create a black image, a window and bind the function to window
# img = np.zeros((512,512,3), np.uint8)

# mouse callback function


def flip_color():
    global mode
    print("Color Flipped")
    mode = not mode


def open_image():
    global img, mode
    img = cv2.imread("/home/gavinswilson/Downloads/test.jpg", cv2.IMREAD_GRAYSCALE)
    cv2.namedWindow('test_image')
    cv2.setMouseCallback('test_image', draw_line)
    while(1):
        cv2.imshow('test_image',img)
        k = cv2.waitKey(1) & 0xFF
        if k == ord('m'):
            mode = not mode
        elif k == 27:
            break
    # if cv2.waitKey(20) & 0xFF == 27:
    #     break
    cv2.destroyAllWindows()

def window():
   app = QApplication(sys.argv)
   widget = QWidget()
   
   button1 = QPushButton(widget)
   button1.setText("Open Image")
   button1.move(64,32)
   button1.clicked.connect(button1_clicked)

   button2 = QPushButton(widget)
   button2.setText("Change Color")
   button2.move(64,64)
   button2.clicked.connect(flip_color)

   widget.setGeometry(50,50,320,200)
   widget.setWindowTitle("Analyse")
   widget.show()
   sys.exit(app.exec_())


def button1_clicked():
   open_image()
   
   
if __name__ == '__main__':
   window()






# import numpy as np
# import matplotlib.pyplot as plt
# img=cv2.imread("/home/gavinswilson/Downloads/test.jpg")
# RGB_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# start_point = (200,500)
# end_point = (800,0)
# line_color = (255,0,0)
# line_thickness = 2
# RGB_img = cv2.line(RGB_img, start_point, end_point, line_color, line_thickness)
# grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# #Displaying image using plt.imshow() method
# plt.imshow(RGB_img)
 
# #hold the window
# plt.waitforbuttonpress()
# plt.close('all')

