'''
			#Exercice 3: List

basket=['Banana','Apples','Orange','BlueBerries']
print(f"panier de depart: {basket}")
basket.remove('Banana')
print(f"supression de banne{basket}")
basket.remove('BlueBerries')
print(f"supression de BlueBerries: {basket}")
basket.append('kiwi')
print(f"Ajout de kiwi: {basket}")
basket.insert(0,'Apples')
print(f"Ajout de Apple: {basket}")
print(f"le nombre de Apple dans notre panier est : {basket.count('Apples')}")
print(f"vidage du panier {basket.clear()}")


'''

'''
		#Exercice 4: Float

1- un float est un type de donner en python relatif au nombre 
#2-

i=1.5
liste_float=[]
while i<=5:
	liste_float.append(i)
	i=i+0.5
print(liste_float)


'''


'''
		#Exercice 5

for x in range(1,21):
 	print(x)
print('2-Affichage des nombres pairs compris entre 1 et 20:')
for i in range(1,20):
	if i%2==0:
		print(i)

'''


#'''
	#Exercice6: En boucle
mon_nom='Mohamed'
nom=input("Entrer votre nom").capitalize()
while nom is not mon_nom:
	nom=input("Entrer votre nom")
print(f"nous avons le meme nom Mr{nom}")



