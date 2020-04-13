from itertools import groupby
class MultiSkup():
    # Zadatak 1 - MultiSkup



    def __init__(self, multiSkup = None):
        self.__multiSkup = {}

        if isinstance(multiSkup, MultiSkup):
            self.__multiSkup = multiSkup
        else:
            for key, group in groupby(multiSkup):
                self.__multiSkup[key] = len(list(group))

    def __str__(self):
        output = []
        for key, value in self.__multiSkup.items():
            output.append("%r*%r" % (key, value))
        return "{{" + ", ".join(output) + "}}"



    #Zadatak 2 - MultiSkup



    def __iter__(self):
        array = []

        for key, value in self.__multiSkup.items():
            for i in range(value):
                array.append(key)

        return iter(array)


    def __repr__(self):
        output = []
        for key, value in self.__multiSkup.items():
            output.append("%r: %r" % (key, value))
        return "Multiskup([" + ", ".join(output) + "])"


    


    #Zadatak 3 - MultiSkup

   

    def add(self, key):
        if(key not in self.__multiSkup.keys()):
            self.__multiSkup[key] = 1
        else:
            self.__multiSkup[key] += 1

    def add(self, key, value = 1):
        if(key not in self.__multiSkup.keys()):
            raise ValueError('Ključ ne postoji.')
        else:
            self.__multiSkup[key] += value

    def remove(self, key, value = 1):
        if (key not in self.__multiSkup.keys()):
            raise ValueError('Ključ ne postoji.')
        else:
            self.__multiSkup[key] -= value


print("Zadatak 1 - MultiSkup")
dict = MultiSkup([1,1,2,2,2,3,3,4])

print(dict)



print("Zadatak 2 - MultiSkup")

for el in dict:
    print(el)

print(repr(dict))



print("Zadatak 3 - MultiSkup")

dict.add(1)
print("Dodavanje samo sa key-em: ", dict)

dict.add(1, 3)
print("Za key '1' value nadodajemo 3: ", dict)

dict.remove(1, 2)
print("Za key '1' value oduzimamo 2: ", dict)

