try:
  camisa = int(input())
  votos = [0]*24
  total = 0

  while camisa != 0:
    if 1 <= camisa <= 24:
      votos[camisa-1] += 1
      total += 1
    camisa = int(input())

  print(f"TOTAL DE VOTOS = {total}")
  for i in range(len(votos)):
    voto = votos[i]
    if voto > 0:
      print(f"JOGADOR = {i+1}, VOTOS = {voto}, PERCENTUAL = {int((voto/total)*100)}%")
  print(f"MELHOR JOGADOR = {(votos.index(max(votos)))+1}")

except:
  pass
