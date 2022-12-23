'''	#1-
chaine=input("Entrer une chaine de caractere contenant 10 caractere: ")
taille=len(chaine)
if taille>10:
	print('chaine trop longue')
elif taille<10:
	print("chaîne pas assez longue")
else:
	print("votre chaine contient exactement 10 caractere")

	#2-
print(f"le premier caractere de votre chaine est {chaine[0]}")
print(f"le dernier caractere de votre chaine est {chaine[taille-1]}")

	#3-
for lettre in range(chaine):
	print(chaine[0:lettre])
	
'''
