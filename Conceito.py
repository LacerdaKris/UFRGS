try:
    nota = float(input("Digite a nota: "))
    assert 0 < nota < 100
    if 100 >= nota >= 90:
        print("A")
    elif 90 > nota >= 80:
        print("B")
    elif 80 > nota >= 70:
        print("C")
    elif 70 > nota >= 60:
        print("D")
    else:
        print("F")
    
except:
    print("Nota inválida")
