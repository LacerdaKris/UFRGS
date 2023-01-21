try:
  N1 = int(input())
  N2 = int(input())
  divisoresN1 = []
  divisoresN2 = []
  soma1 = 0
  soma2 = 0

  for i in range(1, N1/2):
    if (N1 % i) == 0:
      soma1 = int (soma1 + i)
      divisoresN1.append(i)
  for j in range(1,N2/2):
    if (N2 % j) == 0:
      soma2 = soma2 + j
      divisoresN2.append(j)

  print(f"Divisores próprios de {N1}: {divisoresN1} cuja soma é {soma1}")
  if soma1 == N2 and soma2 == N1:
    print(f"{N1} e {N2} são amigos")
  else:
    print(f"{N1} e {N2} não são amigos")

except:
  pass
