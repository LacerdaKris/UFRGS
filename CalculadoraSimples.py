a = float(input("Digite um número: "))
b = float(input("Digite outro número: "))
c = str(input("Digite um símbolo de operação: "))
d = str(input("Digite a ordem da operação, sendo N para normal e R para reversa: "))

if c == "+":
    resultado = a+b
elif c == "*":
    resultado = a*b
elif c == "-":
    if d == 'r':
        resultado = b-a
    else:
        resultado = a-b
elif c == "/":
    if d == 'r':
        resultado = b/a
    else:
        resultado = a/b
        
print(f"{resultado:.2f}")
