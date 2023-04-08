import cv2
import numpy as np
import matplotlib.pyplot as plt

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


class image_analysis:
    viewer = "cv2" #or can be matlib....
    
    def __init__(self) -> None:
        self.drawing = False
        self.mode = True
        self.color_1 = (239,41,41)
        self.color = (255,0,255)
        self.color_2 = (41, 239, 41)
        self.ix = -1
        self.iy = -1
        self.img = np.zeros((512,512,3), np.uint8)
        pass

    def draw_line(self,event,x,y,flags,param):
        # global img,ix,iy,drawing,mode
        if event == cv2.EVENT_LBUTTONDOWN:
            drawing = True
            self.ix = x
            self.iy = y
        elif event == cv2.EVENT_LBUTTONUP:
            drawing = False
            if self.mode == True:
                print("color 1:" +str(self.color_1))
                cv2.line(self.img,(self.ix,self.iy),(x,y),self.color_1,5)
            else:
                print("color 2:" +str(self.color_2))
                cv2.line(self.img,(self.ix,self.iy),(x,y),self.color_2,5)
                # cv2.circle(img,(x,y),5,(0,0,255),-1)

    def draw_circle(self,event,x,y,flags,param):
        if event == cv2.EVENT_LBUTTONDBLCLK:
            cv2.circle(self.img,(x,y),100,(255,0,0),-1) 
    
    def flip_color(self):
    # global mode
        print("Color Flipped")
        self.mode = not self.mode
    
    def set_drawing_color(self, newcolor):
        print("new Color:" + str(newcolor))
        self.color_1 = newcolor
        print(self.color_1)

    def open_image(self, filename):
    # global img, mode
        # self.img = cv2.imread("/home/gavinswilson/Downloads/test.jpg", cv2.IMREAD_GRAYSCALE)
        self.img = cv2.imread(filename, cv2.IMREAD_COLOR)
        cv2.namedWindow('test_image')
        cv2.setMouseCallback('test_image', self.draw_line)
        while(1):
            cv2.imshow('test_image',self.img)
            k = cv2.waitKey(1) & 0xFF
            if k == ord('m'):
                self.mode = not self.mode
            elif k == 27:
                break
        # if cv2.waitKey(20) & 0xFF == 27:
        #     break
        cv2.destroyAllWindows()
