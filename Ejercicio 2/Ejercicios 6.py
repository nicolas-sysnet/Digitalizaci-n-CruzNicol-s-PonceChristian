notas = {
    "Ana": 8,
    "Luis": 4,
    "Marta": 6,
    "Pablo": 5
    }

media = sum(notas.values()) / len(notas)

for clave, valor in notas.items():
    if valor >= 5:
        print(f"{clave} -> {valor} -> aprobado")
   

print (f"La media es {media} ")