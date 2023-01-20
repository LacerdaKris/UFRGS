a = int(input())
b = int(input())
intervalo = []
soma = 0
if b < a:
  for i in range(b, a+1):
    intervalo.append(i)
    soma += i
else:
  for i in range(a, b+1):
    intervalo.append(i)
    soma += i
comprimento = len(intervalo)
metade = int(comprimento/2)
print(f"Início do intervalo: {a}")
print(f"Fim do intervalo: {b}")
print(f"Somatório do intervalo {soma}")
if (comprimento % 2) == 0:
  print(f"Metade do intervalo {intervalo[metade-1]} e {intervalo[metade]}")
else:
  print(f"Metade do intervalo {intervalo[metade]}")
