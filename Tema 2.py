#date initiale
elevi = ["Ana", "Bogdan", "Carmen", "Darius", "Elena"]
note  = [9,       7,        10,       4,        8]

elev_nou        = "Felix"
nota_elev_nou   = 6
elev_de_sters   = "Darius"

interogari_nume = ["Ana", "Mara", "Elena", "stop"]

absente = [1, 0, 2, 3, 0]

#A1
for nume, nota in zip(elevi, note):
    print(f"{nume} are nota {nota}")

#A2
nota_maxima = max(note)
nota_minima = min(note)

elevi_max = [nume for nume, n in zip(elevi, note) if n == nota_maxima]
elevi_min = [nume for nume, n in zip(elevi, note) if n == nota_minima]

print(f"\nNota maxima este {nota_maxima}. Elevii cu aceasta nota: {','.join(elevi_max)}")
print(f"Nota minima este {nota_minima}. Elevii cu aceasta nota: {','.join(elevi_min)}")

idx_max = note.index(nota_maxima)
idx_min = note.index(nota_minima)

#A3
total = 0
for i in note:
    total += i
media = total / len(note)
print(f"\nMedia clasei este {media:.2f}")

#A4
print(f"\nNotele dupa crestere (+1, max10):")
for nume, nota in zip(elevi, note):
    print(f"{nume} are nota {nota}")


#B6
elevi.append(elev_nou)
note.append(nota_elev_nou)

print(f"\nLista actualizata:")
print("Elevi:", elevi)
print("Note:", note)

#B7
print("Stergerea elevului nou:")
pozitie = elevi.index(elev_de_sters)
elev_eliminat = elevi.pop(pozitie)
nota_eliminat = note.pop(pozitie)
print(f"S-a sters elevul {elev_eliminat} cu nota {nota_eliminat}")
print("\nLista actualizata:")
print("Elevi:", elevi)
print("Note:", note)

#B8
for nume, nota in zip(elevi, note):
    print(f"{nume} are nota {nota}")

#C10
promovati = sum(1 for n in note if n >=5)
respinsi = sum(1 for n in note if n < 5)
print(f"\nNumar promovati: {promovati}")
print(f"Numar respinsi.: {respinsi}")


