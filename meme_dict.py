meme_dict = {
"LOL": "una respuesta a algo gracioso",
"CRINGE": "algo raro o embarazoso",
"ROFL": "una respuesta a una broma",
"SHEESH": "ligera desaprobación",
"CREEPY": "aterrador, siniestro",
"AGGRO": "ponerse agresivo/enojado"
}

print("¡Bienvenido al Diccionario Moderno!")
print("Escribe una palabra en MAYÚSCULAS para conocer su significado.\n")

for i in range(5):
  word = input("Escribe una palabra: ")


  if word in meme_dict.keys():
    print("Significado:", meme_dict[word])
  else:
    print("Esa palabra no está en el diccionario.")

  print()
