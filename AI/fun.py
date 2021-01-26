class point:
    x = 0
    y = 0
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __str__(self):
        print("({},{})".format(x,y))

p1 = point(1,2)
print(p1)
