class Rectangle:
    def __init__(self,w,l):
        self.width=w
        self.len=l

    def calculate_perimeter(self):
        return (self.width+self.len)*2

class Square:
    def __init__(self,l):
        self.len=l

    def calculate_perimeter(self):
        return self.len * 4

rec=Rectangle(10,20)
squ=Square(100)
print(rec.calculate_perimeter())
print(squ.calculate_perimeter())
        
    
