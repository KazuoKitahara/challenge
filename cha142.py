#2
class Square:
    def __init__(self,l):
        self.len=l

    def __repr__(self):
        return "{} by {} by {} by {}".format(self.len,self.len,self.len,self.len)
    

sq=Square(29)
print(sq)
