#refri = 5.0 suco = 8.5 hamburguerSimples = 25.8 hamburguerDuplo = 28.4 batatas = 15.0

try:
  bebidas = 0
  simples = 0
  duplo = 0
  fritas = "Não"
  total = 0
  maisVendido = ""
  codigo = int(input())
  while codigo != 0:
    if codigo == 1:
      bebidas = bebidas+1
      total = float(total+5.0)
    elif codigo == 2:
      bebidas = bebidas+1
      total = float(total+8.5)
    elif codigo == 3:
      simples = simples + 1
      total = float(total+25.8)
    elif codigo == 4:
      duplo = duplo + 1
      total = float(total+28.4)
    elif codigo == 5:
      fritas = "Sim"
      total = float(total+15.0)
    codigo = int(input())
  if duplo > simples:
    maisVendido = "Duplo"
  elif (duplo + simples) == 0:
    maisVendido = "Nenhum"
  elif duplo < simples:
    maisVendido = "Simples"
  elif duplo == simples:
    maisVendido = "Empate"
  print("- Relatório da Venda -")
  print(f"Quantidade de bebidas vendidas: {bebidas}")
  print(f"Valor total: R$ {total:.2f}")
  print(f"Lucro obtido: R$ {total*0.3:.2f}")
  print(f"Batatas fritas vendidas? {fritas}")
  print(f"Hambúrguer mais vendido: {maisVendido}")
except:
  pass
