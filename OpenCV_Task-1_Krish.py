import numpy as np
import cv2 as cv

class Tools:
    def blur(self, path):
        img = cv.imread(path)
        if img is None:
            print("Image could not be read.")
            return
        s = int(input("Enter kernel size (n x n): "))
        if s <= 0 or s % 2 == 0:
            print("Kernel size must be a positive odd integer.")
            return
        blur = cv.GaussianBlur(img,(s,s),0)
        cv.imshow("Blurred Image", blur)
        cv.waitKey(0)

    def resize(self,path):
        img = cv.imread(path)
        if img is None:
            print("Image could not be read.")
            return
        x=float(input("Enter scaling factor in x:"))
        y=float(input("Enter scaling factor in y:"))
        if(0<=x<=1 and 0<=y<=1):
            resize = cv.resize(img, None, fx=x, fy=y, interpolation=cv.INTER_AREA)
            cv.imshow("Resized image", resize)
            cv.waitKey(0)
        else:
            print("Scaling factor can't be less than 0 or greater than 1.")
            return
        
    def gray_image(self,path):
        img = cv.imread(path)
        if img is None: 
            print("Image not found.")
            return
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        cv.imshow("Grayscale", gray)
        cv.waitKey(0)

    def threshold(self, path):
        img = cv.imread(path)
        if img is None: 
            print("Image not found.")
            return
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        min= int(input("Enter minimum value [0‑255]: "))
        max = int(input("Enter max value [0‑255]: "))
        
        if(0<=min<=255 and 0<=max<=255 and min<max):
            ret, thresh_img = cv.threshold(gray, min, max, cv.THRESH_BINARY)
            cv.imshow("Threshold_Image", thresh_img)
            cv.waitKey(0)
        else:
            if(min<max):
               print("minimum value and maximum value should be between [0‑255]")
               return
            else:
               print("minimum value should be less than maximum value.")
               return
            
    def Morphology(self,path,tool):
        img = cv.imread(path)
        if img is None:
            print("Image could not be read.")
            return
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        if tool=='Erosion':
            n=int(input("Enter kernal size(n x n) such that greater the value of 'n' greater is the thickness:"))
            kernel = np.ones((n,n),np.uint8)
            erosion = cv.erode(gray,kernel,iterations = 1)
            cv.imshow("Morphological-Erosion Image", erosion)
            cv.waitKey(0)
        elif tool=='Dilation':
            n=int(input("Enter kernal size(n x n) such that greater the value of 'n' smaller is the thickness:"))
            kernel = np.ones((n,n),np.uint8)
            dilation = cv.dilate(gray,kernel,iterations = 1)
            cv.imshow("Morphological-Dilation Image", dilation)
            cv.waitKey(0)
        else:
            print("Tool not implemented due to invalid option selection.")
            return
        
            
class Main:
    def __init__(self):
        self.t=Tools()
    def start(self):
        path = input("Enter image path: ")

        print("Available tools:")
        print("1 - Blur")
        print("2 - Resize")
        print("3 - Morphological operations")
        print("4 - Convert to Grayscale")
        print("5 - Threshold")
        tool = input("Enter the tool to perform (e.g., Blur or Resize,etc.): ")

        if tool == 'Blur':
            self.t.blur(path)
        elif tool=='Resize':
            self.t.resize(path)
        elif tool=='Convert to Grayscale':
            self.t.gray_image(path)
        elif tool=='Threshold':
            self.t.threshold(path)
        elif tool=='Rotate':
            self.t.rotate(path)
        elif tool=='Morphological operations': 
            print("1-Erosion")
            print("2-Dilation")
            tools=input("Enter the operation(Erosion/Dilation):")
            self.t.Morphology(path,tools)
        else:
            print("Tool not implemented due to invalid option.")


if __name__ == "__main__":
    app = Main()
    app.start()