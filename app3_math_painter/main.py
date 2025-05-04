import numpy as np
from PIL import Image

class Color:
    """
    class to define the colors
    """
    def __init__(self,r,g,b):
        self.r=r
        self.g=g
        self.b=b


class Canvas:
    """
    class to create the canvas
    """
    def __init__(self, height,width,color):
        self.height = height
        self.width = width
        self.color = color
        self.data = np.zeros((self.height, self.width, 3), dtype=np.uint8)
        self.data[:] = self.color

    def make(self,image_path):
        """
        create the canvas and to store the image in the .png file
        """
        img=Image.fromarray(self.data,'RGB')
        return img.save(image_path)



class Square:
    def __init__(self,x,y,side,color):
        self.x = x
        self.y = y
        self.side = side
        self.color = color

    def draw(self,canvas):
        """
        create the square inside the canvas
        """
        canvas.data[self.x:self.side+self.x,self.y:self.y+self.y]=self.color

class Rectangle:
    def __init__(self, width, height,x,y,a,b,color):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.a = a
        self.b = b
        self.color = color

    def draw(self,canvas):
        """
        create the rectangle inside the canvas
        """
        canvas.data[self.x:self.a+self.x,self.y:self.b+self.y]=self.color

can=Canvas(height=100,width=100,color=(255,255,255))
rec=Rectangle(3,4,10,20,3,4,color=(100,200,0))
rec.draw(can)
sqr=Square(1,2,4,color=(10,100,0))
sqr.draw(can)
can.make("canva.png")