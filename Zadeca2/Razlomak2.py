class Razlomak(object):
    ### Drugi zadatak

    def __init__(self,brojnik,nazivnik=1):
        if nazivnik==0: raise Exception('Nazivnik ne moze biti 0')
        self._brojnik=brojnik
        self._nazivnik=nazivnik

    def __str__(self):
        return'%d|%d' % (self._brojnik,self._nazivnik)

    @staticmethod
    def inverz(self):
        return Razlomak(self._nazivnik,self._brojnik)


    ### Treci zadatak
    @staticmethod
    def pretvori (num):
        x= str(num)
        if not '.' in x:
            return 0
        return len(x) -x.index('.')-1


    @staticmethod
    def stvori (x:float):
        brojdec=Razlomak.pretvori(x)
        broj='1'
        for i in range (brojdec):
            broj+='0'
        return Razlomak(x*int(broj),int(broj))




r1=Razlomak (314,100)
print (r1)
r2=Razlomak.inverz(r1)


print(r2,r1,r2)

r1=Razlomak.stvori(3.14)

print(r1)
r2 =Razlomak.stvori(0.006021)
print (r2)
r3=Razlomak.stvori(-75.204)
print(r3)