try:
  N = int(input())
  if N <= 1:
    print('Entrada inválida')
  else:
    print(f'Conjectura de Collatz para N = {N}')
    while N > 1:
      if N % 2 == 0:
        N = int(N/2)
      else:
        N = int(3*N+1)
      print(N, '\t', N*'#', sep='')

except:
  print('Entrada inválida')
