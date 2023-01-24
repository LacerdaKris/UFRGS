import random

try:
  jogador1 = []
  jogador2 = []
  sorteados = []
  pontos1 = []
  pontos2 = []
  numero = int(input())
  while numero != 0:
    if 0 < numero <= 20:
      if len(jogador1) < 5:
        jogador1.append(numero)
      elif len(jogador2) < 5:
        jogador2.append(numero)
      else:
        while len(sorteados) < 5:
          sorteio = random.randint(1, 20)
          if sorteio not in sorteados:
            sorteados.append(sorteio)
        pontos1.append(len(set(jogador1).intersection(sorteados)) * 10)
        pontos2.append(len(set(jogador1).intersection(sorteados)) * 10)
        .clear()
    numero = int(input())

  for i, j in pontos1, pontos2:
    print(f"JOGADOR 1 = {i}, JOGADOR 2 = {j}")

  print(jogador1, jogador2, sorteados)

  if sum(pontos1) > sum(pontos2):
    print("JOGADOR 1 VENCEU!")
  elif sum(pontos1) < sum(pontos2):
    print("JOGADOR 2 VENCEU!")
  elif sum(pontos1) == sum(pontos2):
    print("EMPATE!")

except:
  pass
