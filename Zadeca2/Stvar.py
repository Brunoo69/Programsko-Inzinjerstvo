
class Stvar(object):

    brojStvari = 0

    def __init__(self):
        Stvar.brojStvari += 1

    def __del__(self):
        Stvar.brojStvari -= 1


s1=Stvar
print(Stvar.brojStvari)
s2=Stvar()
print(Stvar.brojStvari)
s3=s2
print(Stvar.brojStvari)

del(s2)
print(Stvar.brojStvari)
del(s3)
print(Stvar.brojStvari)
del(s1)














