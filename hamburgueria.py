#refri = 5.0 suco = 8.5 hamburguerSimples = 25.8 hamburguerDuplo = 28.4 batatas = 15.0

bebidas = 0
simples = 0
duplo = 0
fritas = "Não"
total = 0
codigo = int(input())
while 6 > codigo > 0:
  if codigo == 1:
    bebidas += 1
    total += 5
  elif codigo == 2:
    bebidas += 1
    total += 8.5
  elif codigo == 3:
    simples += 1
    total += 25.8
  elif codigo == 4:
    duplo += 1
    total += 28.4
  elif codigo == 5:
    fritas = "Sim"
    total += 15
  codigo = int(input())

maisVendido = "Nenhum"
if duplo > simples:
  maisVendido = "Duplo"
elif duplo & simples == 0:
  maisVendido = "Nenhum"
elif duplo < simples:
  maisVendido = "Simples"
else:
  maisVendido = "Empate"

print("- Relatório da Venda -")
print(f"Quantidade de bebidas vendidas: {bebidas}")
print(f"Valor total: R$ {total:.2f}")
print(f"Lucro obtido: R$ {total*0.3:.2f}")
print(f"Batatas fritas vendidas? {fritas}")
print(f"Hambúrguer mais vendido: {maisVendido}")
