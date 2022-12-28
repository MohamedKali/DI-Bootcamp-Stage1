'''
🌟 Exercice 1 : Set

my_fav_num=set({'66-00-18-05','66-18-19-20','72-56-20-24'})

my_fav_num.add('66-18-87-20')
my_fav_num.add('72-56-56-24')
print(my_fav_num)
my_fav_num.remove('66-00-18-05')
print(f"\nmy_fav_num avec le dernier numero supprimer {my_fav_num}\n")
my_friend_fav=set({'64-87-18-05','73-53-03-20','68-32-03-20','73-24-99-20'})
print(f"my_friend_fav: {my_friend_fav}\n")
our_fav_numbers=set(list(my_fav_num)+list(my_friend_fav))
print(f"mon nouveau ensemble (mes contact favoris + de mon ami): {our_fav_numbers}\n")

'''

#🌟 Exercice 2 : Tuple

	#Il n'est pas possible d'ajouter un element car les tuples sont imuables.




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


'''
	#Exercice6: En boucle
mon_nom='Mohamed'
nom=input("Entrer votre nom: ").capitalize()
while nom != mon_nom:
	nom=input("Entrer votre nom: ")
print(f"nous avons le meme nom Mr {nom}") 

'''


"""
#Exercice 7: fruit prefere

fruit_prefere=input("Entrer vos fruits prefere sur une ligne ex:( mange goyave banane): ").capitalize()
liste_fruit_prefere=fruit_prefere.split()
fruit=input("Entrer le nom d'un fruit: ").capitalize()
if fruit in liste_fruit_prefere:
	print("Vous avez choisir un de vos fruits preferes! profitez-en!")
else:
	print("Vous avez choisi un nouveau fruit. J'espere que vous apprecierez")
print(liste_fruit_prefere)

"""


"""
	#Exercice 8: Qui a commander une pizza!

graniture=[]
grani=input("Entrer les graintures de votre pizza (une fois terminer taper \"Quit\" pour enregistrer): ").capitalize()
while grani != 'Quit' :
	if grani in graniture:
		print(f"{grani} deja presente dans votre pizza")
	else:
		graniture.append(grani)
		print(f"vous venez d'ajouter {grani} a votre pizza")
	grani=input("graintures suivante: (une fois terminer taper \"Quit\" pour enregistrer): ").capitalize()
	#if grani =="Quit"

print('Liste des graintures presente dans votre pizza :')
print('----------------------------------------------')
for x in graniture:
	print(f" {x}")
print(f"Le prix total de votre pizza est de: {10 + 2.5*len(graniture)}$")
"""

'''
		#Exercice 9 : Cinémax
from os import system
import time
liste_age=[]
prix_total=0
age=int(input("Enrer l'age de tous les membre de la famille (taper '1000' pour enregistrer une fois tous les ages saisir): "))
while age != 1000:
	liste_age.append(age)
	if age <3:
		pass
	elif age >=3 and age<12:
		prix_total+=10
	else:
		prix_total+=15
	age=int(input("Enrer l'age du membre suivant (taper '1000' pour enregistrer une fois tous les ages saisir): "))


print(f"le cout total des tickets pour votre famille est de: {prix_total}$")
system('pause')
system('cls')



# 4-
print ("Question 4: Exercice 9\n\n")
liste_nom=[]
nom=input("Entrer vos noms ('save' pour enregistrer la liste): ").capitalize()
while nom != 'Save':
	liste_nom.append(nom)
	nom=input("personne suivante ('save' pour enregistrer la liste): ").capitalize()

for x in liste_nom:
	age=int(input(f"Mr {x} quel est votre age: "))
	if age <16:
		print(f"Mr {x} vous n'etes pas autorisez a reagarder ce film veillez sortir svp !!!")
		liste_nom.remove(x)
	else:
		print(f"desole du derangement Mr {x} ")

print("liste des personnes autorisez a suivre cet film")
print("-----------------------------------------------")
for x in liste_nom:
	print( x)
'''