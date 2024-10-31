import random

# Lista de cuvinte
cuvinte = ["python", "programare", "calculator", "date", "algoritm"]
cuvant_de_ghicit = random.choice(cuvinte)
progres = ["_" for _ in cuvant_de_ghicit]

# Inițializarea numărului de încercări
incercari_ramase = 6
litere_incercate = []

print("Incepe jocul!\n")
print("Cuvântul de ghicit este:", " ".join(progres))
print(f"Încercări rămase: {incercari_ramase}")

while "_" in progres and incercari_ramase > 0:
    litera = input("Introdu o litera: ").lower()

    if len(litera) != 1 or not litera.isalpha():
        print("Te rog sa introduci o litera valida")
        continue

    if litera in litere_incercate:
        print("Ai mai incercat aceasta litera. Incearca alta.")
        continue

    litere_incercate.append(litera)
    print(litere_incercate)
    if litera in cuvant_de_ghicit:
        for i in range(len(cuvant_de_ghicit)):
            if cuvant_de_ghicit[i] == litera:
                progres[i] = litera
        print("Good job broo! Litera este in cuvant.")
    else:
        incercari_ramase -= 1
        print("Awww, nu-i ok. Litera nu este in cuvant.")

    print("Progres: ", " ".join(progres))
    print(f"Incercari ramase: {incercari_ramase}")

if "_" not in progres:
    print("Felicitari! Ai ghicit cuvantul:", cuvant_de_ghicit)
else:
    print("Ai pierdut! Cuvantul era:", cuvant_de_ghicit)