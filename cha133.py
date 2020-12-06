class Shape:
    def what_am_i(self):
        print("I am a shape")

class Rectangle(Shape):
    def __init__(self,w,l):
        self.width=w
        self.len=l

class Square(Shape):
    def __init__(self,l):
        self.len=l

rec=Rectangle(10,20)
squ=Square(30)
rec.what_am_i()
squ.what_am_i()

    
