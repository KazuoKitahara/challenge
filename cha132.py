#2
class Square:
    def __init__(self,l):
        self.len=l

    def change_size(self,d):
        self.len+=d

squ=Square(10)
print(squ.len)
squ.change_size(3)
print(squ.len)
squ.change_size(-4)
print(squ.len)
        
