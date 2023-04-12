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
# ###########################################################################################################
# Variables
# ###########################################################################################################
    viewer = "cv2" #or can be matlib....
    preview = None
    drawing_mode = None
    file_name = None
    thickness = None
    color = (255,0,0)
    ix = None
    iy = None
    img = None
    img_clone = None
    imageName = "Image1"
    refpts = []

# ###########################################################################################################
# Initialise Class
# ###########################################################################################################
    def __init__(self) -> None:
        self.drawing = False
        # self.mode = True
        self.color = (255,0,0)
        self.ix = -1
        self.iy = -1
        self.img = np.zeros((512,512,3), np.uint8)
        pass
# ###########################################################################################################
# Image Functions
# ###########################################################################################################
    def draw(self,event,x,y,flags,param):
        # global img,ix,iy,drawing,mode
        if event == cv2.EVENT_LBUTTONDOWN:
            drawing = True
            self.ix = x
            self.iy = y
            self.refpts.append(('Line Start', x,y,self.color,self.thickness))
            self.preview = self.img.copy()
            cv2.line(self.preview, (self.ix, self.iy), (x,y), self.color, 1)
        elif event == cv2.EVENT_MOUSEMOVE:
            if self.preview is not None:
                self.preview = self.img.copy()
                cv2.line(self.preview, (self.ix, self.iy), (x,y), self.color, 1)
        elif event == cv2.EVENT_LBUTTONUP:
            drawing = False
            print("color 1:" +str(self.color))
            if self.preview is not None:
                self.preview = None
                self.refpts.append(('Line End',x,y,self.color,self.thickness))
                cv2.line(self.img,(self.ix,self.iy),(x,y),self.color,self.thickness)
                # cv2.circle(self.img,(x,y),100,(255,0,0),-1) 
                # print(self.refpts, self.color, self.thickness)
                
     
    

    def open_image(self, filename):
    # global img, mode
        # self.img = cv2.imread("/home/gavinswilson/Downloads/test.jpg", cv2.IMREAD_GRAYSCALE)
        self.img = cv2.imread(filename, cv2.IMREAD_COLOR)
        cv2.namedWindow(self.imageName, cv2.WINDOW_NORMAL)
        cv2.setMouseCallback(self.imageName, self.draw)
        cv2.setWindowTitle(self.imageName, self.file_name)
        # cv2.setWindowProperty(self.imageName, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN, )
        while(1):
            if self.preview is None:
                cv2.imshow(self.imageName,self.img)
            else:
                cv2.imshow(self.imageName,self.preview)
            k = cv2.waitKey(1) & 0xFF
            if k == ord('m'):
                self.mode = not self.mode
            elif k == 27:
                break
        # if cv2.waitKey(20) & 0xFF == 27:
        #     break
        cv2.destroyAllWindows()
# ###########################################################################################################
# Maths Functions
# ###########################################################################################################
    def delete_last_object(self):
        arraylen = len(self.refpts)
        # print(arraylen)
        if (self.refpts[arraylen-1][0] == 'Line End'):
            self.refpts.pop()
            self.refpts.pop()





# ###########################################################################################################
# Get and set functions
# ###########################################################################################################
    def set_image_savepoint(self):
        self.refpts = []
        self.img_clone = self.img.copy()
    
    def set_drawing_color(self, newcolor):
        # print("new Color:" + str(newcolor))
        self.color = newcolor
        # print(self.color)

    def set_drawing_mode(self, mode):
        self.drawing_mode = mode
    
    def set_file_name(self, file_name):
        self.file_name = file_name
    
    def set_thickness(self, thickness):
        self.thickness = thickness

    def get_drawing_mode(self):
        return(self.drawing_mode)
    
    def get_file_name(self):
        return(self.file_name)

    def get_thickness(self):
        return(self.thickness)
    
    def get_drawing_color(self):
        return(self.color)
# ###########################################################################################################
