#Create class
class point:
    def __init__(self, x = 0, y = 0):
        self.__x = x
        self.__y = y
    #method to print points in coordinate format
    def __str__(self):
        return "({0},{1})".format(self.__x, self.__y)
#Create Object
p1 = point(2, 3)
print(p1)