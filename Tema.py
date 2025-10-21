text = "Gigi Becali și-a criticat jucătorii după înfrângerea cu Metaloglobus: „Au făcut bani și nu mai au smerenie"

mijloc = len(text) // 2
prima_parte = text[:mijloc]
a_doua_parte = text[mijloc:]

prima_parte = prima_parte.upper().strip()

a_doua_parte = a_doua_parte[::-1]
a_doua_parte = a_doua_parte.capitalize()
a_doua_parte = ''.join(c for c in a_doua_parte if c not in ".,!?")

rezulatat = prima_parte + " " + a_doua_parte
print(rezulatat)


