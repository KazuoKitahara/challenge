class Horse:
    def __init__(self,name, rider):
        self.name=name
        self.rider=rider

class Rider:
    def __init__(self, name):
        self.name=name

take=Rider("Take Yutaka")
Dee=Horse("Deep Impact",take)
print(Dee.rider.name)
