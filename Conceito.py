nota = float(input("Informe a nota de 0 a 100: "))

if 100 >= nota >= 90:
    print("A")
elif 90 > nota >= 80:
    print("B")
elif 80 > nota >= 70:
    print("C")
elif 70 > nota >= 60:
    print("D")
elif 60 > nota >= 0:
    print("F")
else:
    print("Nota inválida")
