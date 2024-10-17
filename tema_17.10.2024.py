articol="""   In masina cu Adrian se mai aflau iubita lui, Iorga, fratele sau, care a fost arestat pentru ultraj pentru 30 de zile, si iubita acestuia.
„In noaptea de 11 spre 12 octombrie, in jurul orei 02:00, doi politisti din cadrul Sectiei 1 Politie Pitesti, care desfasurau activiati in filtru rutier, pe b-dul I.C. Bratianu din municipiul Pitesti, au observat un autoturism care, la intersectia dintre str. Ana Ipatescu si b-dul I.C. Bratianu a schimbat directia de mers spre sensul opus fata de politisti, cu incalcarea marcajului longitudinal continuu ce desparte sensurile de mers”, se arata in comunicatul IPJ Arges, conform ZiarulArgesul.
Se pare ca, dupa ce a jucat in filmul Buzz House, tanarul nu si-a mai iesit din rolul de actor. De data aceasta s-a crezut intr-un film cu Jason Statham!!Da
"""
jumatate= len(articol)//2

jumatate_1= articol[:jumatate]
jumatate_2= articol[jumatate:]


print("Acesta este numarul caracterelor din articol")
print(len(articol))
jumatate_1=jumatate_1.upper()
jumatate_1=jumatate_1.strip()
print("Aceasta este prima jumatate din articol:")
print (jumatate_1)
print()

print("***")
print("Aceasta este a doua jumatate din articol:")
jumatate_2=jumatate_2[::-1].strip()

jumatate_2_replaced=jumatate_2.capitalize().replace(".","").replace(",","").replace("!","").replace("?","")
print(jumatate_2_replaced)
print()
print("Iar acum le vom concatena")
print(jumatate_1+jumatate_2)