try:
    nota = float(input("Digite a nota: "))
    assert 0 <= nota <= 100
    if nota >= 90:
        print("Conceito: A")
    elif 90 > nota >= 80:
        print("Conceito: B")
    elif 80 > nota >= 70:
        print("Conceito: C")
    elif 70 > nota >= 60:
        print("Conceito: D")
    else:
        print("Conceito: F")

except:
    print("Nota inválida")
