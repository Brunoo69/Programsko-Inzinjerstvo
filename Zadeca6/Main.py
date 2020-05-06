from Ispit import Ispit
from IspitDB import IspitiDB



isp = Ispit()
isp.dodaj("Ante Antić", "Linearna algebra", 5)
isp.dodaj("Ante Antić", "Programiranje 1", 4)
isp.dodaj("Marija Marijić", "Linearna algebra", 4)
isp.dodaj("Marija Marijić", "Matematička analiza", 5)

isp.spremi_datoteka("ispiti.txt")
print(open("ispiti.txt", encoding="utf8").read())

isp = Ispit.ucitaj_datoteku("ispiti.txt")
print(isp)



isp.spremi_json("ispiti.json")
print(open("ispiti.json", encoding="utf8").read())
Ispit.ucitaj_json("ispiti.json")
print(isp)




db = IspitiDB("ispiti.sqlite")
print(db.cur.execute("SELECT * FROM studenti").fetchall())

db.dodaj_student("Ante Antić")
db.dodaj_student("Ana Anić")
db.dodaj_student("Pero Perić")
print(db.cur.execute("SELECT * FROM studenti").fetchall())
print(db.vrati_student_id("Pero Perić"))
print(db.vrati_student_id("Marija Marijić"))

db.izbrisi_student("Pero Perić")
db.promijeni_student("Ana Anić","Marija Marijić")
print(db.cur.execute("SELECT * FROM studenti").fetchall())




db = IspitiDB("ispiti.sqlite")
db.dodaj_student("Ante Antić")
db.dodaj_student("Marija Marijić")
db.dodaj_kolegiji("Linearna algebra")
db.dodaj_kolegiji("Programiranje 1")
db.dodaj_kolegiji("Matematička analiza")
db.ispitaj("Ante Antić", "Linearna algebra", 5)
db.ispitaj("Ante Antić", "Linearna algebra", 3)
print(db.svi_ispiti())
db.ispitaj("Ante Antić","Linearna algebra",4)
print(db.svi_ispiti())
db.ispitaj("Ante Antić","Linearna algebra")
print(db.svi_ispiti())
db.ispitaj("Ante Antić","Linearna algebra",5)
db.ispitaj("Marija Marijić","Programiranje 1",5)
db.ispitaj("Marija Marijić","Matematička analiza",4)
print(db.svi_ispiti())