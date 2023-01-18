refri = 5.0
suco = 8.5
hamburguerSimples = 25.8
hamburguerDuplo = 28.4
batatas = 15.0

bebidas = 0
total = 0
lucro = 0
fritas = "Não"
simples = 0
duplo = 0
codigo = int(input())
while 6 > codigo > 0:
  if codigo == 1:
    bebidas += 1
    total += refri
  elif codigo == 2:
    bebidas += 1
    total += suco
  elif codigo == 3:
    simples += 1
    total += hamburguerSimples
  elif codigo == 4:
    duplo += 1
    total += hamburguerDuplo
  elif codigo == 5:
    fritas = "Sim"
    total += batatas
  codigo = int(input())

maisVendido = ""
if duplo > simples:
  maisVendido = "Duplo"
elif duplo == simples:
  maisVendido = "Empate"
else:
  maisVendido = "Simples"
print(f"- Relatório da Venda -")
print(f"Quantidade de bebidas vendidas: {bebidas}")
print(f"Valor total: R$ {total:.2f}")
print(f"Lucro obtido: R$ {total*0.3:.2f}")
print(f"Batatas fritas vendidas? {fritas}")
print(f"Hambúrguer mais vendido: {maisVendido}")
