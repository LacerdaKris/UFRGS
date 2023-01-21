#imprimir divisores dos dois numeros digitados, e verificar pela soma dos divisores se são números amigos

#solução com listas:
try:
  N1 = int(input("Digite o primeiro número: "))
  N2 = int(input("Digite o segundo número: "))
  divisoresN1 = []
  divisoresN2 = []
  soma1 = 0
  soma2 = 0

  for i in range(1, N1):
    if (N1 % i) == 0:
      soma1 = soma1 + i
      divisoresN1.append(i)

  for j in range(1, N2):
    if (N2 % j) == 0:
      soma2 = soma2 + j
      divisoresN2.append(j)

  print(f"Divisores próprios de {N1}:", end=' ')
  print(*divisoresN1, end='')
  print(", cuja soma é", soma1)
  print(f"Divisores próprios de {N2}:", end=' ')
  print(*divisoresN2, end='')
  print(", cuja soma é", soma2)
  if soma1 == N2 and soma2 == N1:
    print(f"{N1} e {N2} são amigos")
  else:
    print(f"{N1} e {N2} não são amigos")

except:
  pass

#solução com impressão pelo range:
try:
  N1 = int(input("Digite o primeiro número: "))
  N2 = int(input("Digite o segundo número: "))
  soma1 = 0
  soma2 = 0
  
  print(f"Divisores próprios de {N1}:", end=' ')
  for i in range(1, N1):
    if (N1 % i) == 0:
      soma1 = soma1 + i
      print(i, end=' ')
  print("cuja soma é", soma1)
  
  print(f"Divisores próprios de {N2}:", end=' ')
  for j in range(1, N2):
    if (N2 % j) == 0:
      soma2 = soma2 + j
      print(j, end=' ')
  print("cuja soma é", soma2)
  
  if soma1 == N2 and soma2 == N1:
    print(f"{N1} e {N2} são amigos")
  else:
    print(f"{N1} e {N2} não são amigos")

except:
  pass
