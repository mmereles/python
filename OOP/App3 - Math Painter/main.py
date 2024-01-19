from PIL import Image
import numpy as np

class Canvas:
    
    def __init__(self, height, width, color):
        self.color = color
        self.height = height
        self.width = width
        
        self.data = np.zeros((self.height,self.width,3), dtype=np.uint8)
        self.data[:] = self.color
        
    def make(self, imagepath):
        img = Image.fromarray(self.data, 'RGB')
        img.save(imagepath)

class Rectangle:
    
    def __init__(self, x, y, a, b, color):
        self.x = x
        self.y = y
        self.a = a
        self.b = b
        self.color = color
        
    def draw(self, canvas):
        pass
    

class Square:
    
    def __init__(self, x, y, a, color):
        self.color = color
        self.x = x
        self.y = y
        self.a = a
        
    def draw(self, canvas):
        pass