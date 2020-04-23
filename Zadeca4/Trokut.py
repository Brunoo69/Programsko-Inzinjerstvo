from math import sqrt

class Trokut():

    def __init__(self, a, b, c):
        if (a < 0 or b < 0 or c < 0) or (a + b <= c) or (c + b <= a) or (a + c <= b):
            raise ValueError("Nije Trokut")
        else:
            self.__stranice = (a, b, c)

    def __str__(self):
        return "trokut %i, %i, %i" % (self.__stranice[0], self.__stranice[1], self.__stranice[2])

    def __repr__(self):
        return "Trokut (%i, %i, %i)" % (self.__stranice[0], self.__stranice[1], self.__stranice[2])

    def opseg(self):
        return (self.__stranice[0] + self.__stranice[1] + self.__stranice[2])

    def povrsina(self):
        s = self.opseg() / 2
        return sqrt( (s - self.__stranice[0])*(s - self.__stranice[1])*(s - self.__stranice[2]) )
