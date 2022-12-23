chaine=input("Entrer une chaine de caractere contenant 10 caractere: ")
if len(chaine)>10:
	print('chaine trop longue')
elif len(chaine)<10:
	print("chaîne pas assez longue")
else:
	print("votre chaine contient exactement 10 caractere")