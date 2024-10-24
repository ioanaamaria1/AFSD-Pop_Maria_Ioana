from csv import DictWriter

meniu = ['papanasi'] * 10 + ['ceafa'] * 3 + ["guias"] * 6
preturi = [["papanasi", 7], ["ceafa", 10], ["guias", 5]]
studenti = ["Liviu", "Ion", "George", "Ana", "Florica"]  # coada FIFO
comenzi = ["guias", "ceafa", "ceafa", "papanasi", "ceafa"]  # coada FIFO
tavi = ["tava"] * 7  # stiva LIFO
istoric_comenzi = []
cata_ceafa_s_a_comandat= comenzi.count("ceafa")
cata_ceafa_exista_la_inceput= meniu.count("ceafa")
cati_papanasi_exista=meniu.count("papanasi")
cati_papanasi_s_au_comandat= comenzi.count("papanasi")
cat_guias_exista=meniu.count("guias")
cat_guias_s_a_comandat= comenzi.count("guias")
print()
print("Rezolvarea < Comenzi >")
print()
while studenti and comenzi and tavi:
    student = studenti.pop(0)
    comanda = comenzi.pop(0)
    print(f"{student} a comandat {comanda}.")
    tava = tavi.pop()
    istoric_comenzi.append(comanda)
print()
print("Rezolvare < Inventar >")
print()
print(f"S-au comandat {cata_ceafa_s_a_comandat} portii de ceafa")
print(f"S-au comandat {cati_papanasi_s_au_comandat} portii de papanasi")
print(f"S-au comandat {cat_guias_s_a_comandat} portii de guias")
print()

cefe_ramase= cata_ceafa_exista_la_inceput-cata_ceafa_s_a_comandat

papanasi_ramasi=cati_papanasi_exista-cati_papanasi_s_au_comandat

guias_ramas= cat_guias_exista-cat_guias_s_a_comandat

if cefe_ramase>0:
    print("Mai exista cefe:")
    print(f"Au ramas {cefe_ramase} cefe ")
else:
    if cefe_ramase==0:
         print("Nu mai exista cefe")
if papanasi_ramasi>0:
    print("Mai exista papanasi:")
    print(f"Au ramas {papanasi_ramasi} papanasi")
else:
    if papanasi_ramasi==0:
        print("Nu mai exista papanasi")

if guias_ramas>0:
    print("Mai exista guias:")
    print(f"Au ramas {guias_ramas} guias")
else:
    if guias_ramas==0:
        print("Nu mai exista guias")
print()
print("Numarul de tavi ramase:")
print(len(tavi))
print()
print("Rezolvare < Finante >")
print()
pret_papanasi=preturi[0][1]
pret_ceafa=preturi[1][1]
pret_guias=preturi[2][1]
print("Cantina a incasat:")
pret_total= cata_ceafa_s_a_comandat*pret_ceafa+cat_guias_s_a_comandat*pret_guias+cati_papanasi_s_au_comandat*pret_papanasi
print(pret_total)
print("In acest meniu, urmatoarele lucruri costa cel mult 7 lei :")
if pret_papanasi<=7:
    print("Papanasi")
if pret_ceafa<=7:
    print("ceafa")
if pret_guias<=7:
    print("Guias")