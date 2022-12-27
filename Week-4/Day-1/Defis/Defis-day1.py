	#1-
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
taille=len(chaine)
for lettre in range(taille+1) :
	print(chaine[0:lettre])

#4-
 '''Etape pour melanger une chaine de caractere
 	1- transformer la chaine en liste avec list()
 	2- Melanger la liste  avec random.shuffle()
 	3- Transformer la liste en chaine avec str.join()
 '''


import random

ma_liste=list(chaine)
print(ma_liste)
random.shuffle(ma_liste)
print(ma_liste)
chaine_melanger=''.join(ma_liste)
print(chaine_melanger)


	

