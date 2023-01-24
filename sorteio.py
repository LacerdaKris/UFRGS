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
        if len(jogador2) == 5:
          while len(sorteados) < 5:
            sorteio = random.randint(1, 20)
            if sorteio not in sorteados:
              sorteados.append(sorteio)
          pontos1.append(len(set(jogador1).intersection(sorteados)) * 10)
          pontos2.append(len(set(jogador2).intersection(sorteados)) * 10)
          jogador1.clear()
          jogador2.clear()
          sorteados.clear()
    numero = int(input())
  for i in range (len(pontos1)):
    print(f"JOGADOR 1 = {pontos1[i]}, JOGADOR 2 = {pontos2[i]}")
  if sum(pontos1) > sum(pontos2):
    print("JOGADOR 1 VENCEU!")
  elif sum(pontos1) < sum(pontos2):
    print("JOGADOR 2 VENCEU!")
  else:
    print("EMPATE!")

except:
  pass
