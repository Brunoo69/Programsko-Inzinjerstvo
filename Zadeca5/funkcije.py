from likovi import *
from math import pi

# Zadatak 5.2


def opseg(lik):
    if isinstance(lik, Kruznica) == True:
        return 2 * lik.radijus * pi
    elif isinstance(lik, Kvadrat) == True:
        return 4 * lik.duljina_stranice

def povrsina(lik):
    if isinstance(lik, Kruznica) == True:
        return (lik.radijus * lik.radijus) * pi
    elif isinstance(lik, Kvadrat) == True:
        return lik.duljina_stranice * lik.duljina_stranice

if __name__ == "__main__":
    print(opseg.__name__)
    print(povrsina.__name__)