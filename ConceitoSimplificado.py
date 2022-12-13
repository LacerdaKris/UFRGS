N = float(input("Informe a nota final: "))
F = float(input("Informe a frequência: "))

if 0 > N or F > 100:
    print("Entrada inválida")
elif N >= 60 and F >= 75:
    print("Aprovado")
elif N < 60 and F >= 75:
    print("Exame")
elif F < 75:
    print("Reprovado")
