try:
    n = int(input())
    print("Conjectura de Collatz para N =\t", n)
    while n > 1:
      if n % 2 == 0:
        n /= 2
      else:
        n = 3*n+1
      print(n, "\t", n*"#")

except ValueError:
    print("Entrada inválida")
