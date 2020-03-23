#Zadatak 1:

class Razlomak(object):

    def __init__(self, brojnik, nazivnik):
        self.brojnik = brojnik
        self.nazivnik = nazivnik

    @property
    def brojnik(self):
        return self._brojnik

    @brojnik.setter
    def brojnik(self, value):
        self._brojnik = value

    @property
    def nazivnik(self):
        return self._nazivnik

    @nazivnik.setter
    def nazivnik(self, value):
        self._nazivnik = value

    def skrati(self):

        broj = 1
        for i in range(1, self.brojnik + 1):
            if(self.brojnik % i == 0 and self.nazivnik % i == 0):
                broj = i
                i += 1
        return self.brojnik/broj, self.nazivnik/broj

#Zadatak 2:

    def __repr__(self):
        return "Razlomak(" + repr(self._brojnik) + "," + repr(self._nazivnik) + ")"
    
    def __str__(self):
        return "Razlomak" + str(self._brojnik) +  "|" + str(self._nazivnik)



    def __eq__(self, other):
        return self.brojnik/self.nazivnik == other.brojnik/other.nazivnik
    def __lt__(self,other):
        return self.brojnik/self.nazivnik < other.brojnik/other.nazivnik
    def __le__(self,other):
        return self.brojnik/self.nazivnik <= other.brojnik/other.nazivnik
    def __gt__(self,other):
        return self.brojnik/self.nazivnik > other.brojnik/other.nazivnik
    def __ge__(self,other):
        return self.brojnik/self.nazivnik >= other.brojnik/other.nazivnik

#Zadatak3:

    def __mul__(self,other):
        return Razlomak(self.brojnik * other.brojnik, self.nazivnik * other.nazivnik)
    
    def __truediv__(self,other):
        return Razlomak(self.brojnik / other.nazivnik, self.nazivnik / other.brojnik)

    def __add__(self,other):
        a= self.nazivnik
        b= other.nazivnik
        nv=1
        if(a<b):
            nv=a
            if(b%a == 0):
                b=b/a
            else:
                b=b
                nv=a*b
        else:
            nv=b
            if(a%b == 0):
                a=a/b
            else:
                a=a
                nv=a*b
        return Razlomak(nv / self.nazivnik * self.brojnik + nv / other.nazivnik * other.brojnik, nv)

    def __sub__(self,other):
        a= self.nazivnik
        b= other.nazivnik
        nv=1
        if(a<b):
            nv=a
            if(b%a == 0):
                b=b/a
            else:
                b=b
                nv=a*b
        else:
            nv=b
            if(a%b == 0):
                a=a/b
            else:
                a=a
                nv=a*b
        return Razlomak(nv / self.nazivnik * self.brojnik - nv / other.nazivnik * other.brojnik, nv)



r1 = Razlomak(12,30)
r2 = Razlomak(2,5)
r3 = Razlomak(3,6)


print("Usporedivanje(==)drugog i treceg razlomka: ", r2 == r3)
print("Usporedivanje(==) prvog i drugog razlomka: ", r1 == r2)
print("Usporedivanje(==) prvog i trećeg razlomka: ", r1 == r3)

print("Usporedivanje(>) drugog i treceg razlomka: ", r2 > r3)
print("Usporedivanje(>) prvog i drugog razlomka: ", r1 > r2)
print("Usporedivanje(>) prvog i trećeg razlomka: ", r1 > r3)

print("Usporedivanje(<) drugog i treceg razlomka: ", r2 < r3)
print("Usporedivanje(<) prvog i drugog razlomka: ", r1 < r2)
print("Usporedivanje(<) prvog i trećeg razlomka: ", r1 < r3)


print("Množenje(*) prvog u drugog razlomka: ", r1*r2)
print("Djeljenje(/) prvog i drugog razlomka: ", r2/r1)
print ("Zbrajanje(+) prvog i drugog razlomka: ", r1+r2)
print("Oduzimanje(-) prvog i drugog razlomka: ", r1-r2)


print("Oduzimanje novostvorenog razlomaka: ", Razlomak(5,2)-Razlomak(3,2))

   







