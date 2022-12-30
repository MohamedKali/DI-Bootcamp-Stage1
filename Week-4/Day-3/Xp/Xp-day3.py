# 🌟 Exercice 1 : Convertir Des Listes En Dictionnaires

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
dic={}
for i,j in zip(keys,values):
	dic[i]=j

print(dic)
'''
#🌟 Exercice 2 : Cinémax

prix=0
family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
for i,j in family.items():
	if j < 3:
		print(f"vous ne payer rien petit(e) {i} profiter de votre film")

	elif j >12 :
		print(f"{i} vous devez payer 10$ ")
		prix+=10
	else:

		print(f"{i} vous devez payer 15$ ")
		prix+=15

print(f"\nle prix total des billets pour cette magnifique famille est de: {prix}$\nprofitez bien du film")

		#Question 5
prix=0
family = {}
reponse=''
print('Veuillez entrer le nom et l\'age de tous les membre de la famille presente pour assister au film\n')
while reponse!='Oui':
	nom=input("Entre le nom: ").capitalize()
	age=int(input("entre l'age:  "))
	reponse=input("Avez vous saisir toute les informations?: (Taper 'oui' ou 'non') ").capitalize()
	family[nom]=age
for i,j in family.items():
	if j < 3:
		print(f"vous ne payer rien petit(e) {i} profiter de votre film")

	elif j >12 :
		print(f"{i} vous devez payer 10$ ")
		prix+=10
	else:

		print(f"{i} vous devez payer 15$ ")
		prix+=15

print(f"\nle prix total des billets pour cette magnifique famille est de: {prix}$\nprofitez bien du film")
'''
'''
  #🌟 Exercice 3 : Zara


marque={
'name': 'Zara',
'creation_date': 1975,
'creator_name': 'Amancio Ortega Gaona', 
'type_of_clothes':['men', 'women', 'children', 'home'],
'international_competitors':['Gap', 'H&M', 'Benetton'],
'number_stores': 7000,
'major_color': 
    {'France': 'blue', 
    'Spain': 'red', 
    'US': ('pink', 'green')
    }
}

marque['number_stores']=2
#print(marque['number_stores'])
print(f"les clients de la marque {marque['name']} sont:")
print("------------------------------------------------\n")

for x in marque['type_of_clothes']:
	print(x)
marque['country_creation']='Spain'
if 'international_competitors' in marque:
	marque['international_competitors'].append('Desigual')
	#print(marque['international_competitors'])
del marque['creator_name'], marque['country_creation'],marque['creation_date']
#print(marque.get('creation_date','aucune information correspondnte'))
dernier_element=len(marque['international_competitors'])
print(f"le dernier concurent de {marque['name']} est : {marque['international_competitors'][dernier_element-1]}")
print("les couleur les plus utilise au USA sont:")
for i in marque['major_color']['US']:
	print(i)
print(f"\nInformations completes concernant la marque {marque['name']}:")
print("-----------------------------------------------------\n")
for (i,j) in marque.items():
	print(f"{i} ---> {j}")
print(f"\nListe de tous les information disponibles (cles de dictionnaire) sur la marque '{marque['name']}'")
print("-------------------------------------------------------------------------------------------\n")

for i in marque:
	print(i)

more_on_zara={'creation_date':1975  ,'number_stores':10000}

marque.update(more_on_zara)
print (marque)
'''

'''
#Exercice 4 : Personnages Disney

users = ["Mickey","Minnie","Donald","Ariel","Pluto"]
print("Question 1")
print("----------")

disney_users_A={}
for (i,j) in enumerate(users):
	disney_users_A[j]=i
print(f"{disney_users_A}\n")

#2-
disney_users_B={}

print("Question 2")
print("----------")

for (i,j) in enumerate(users):
	disney_users_B[i]=j
print(f"{disney_users_B}\n")


#3-
print("Question 3")
print("----------")
disney_users_C={}
users.sort()
for (i,j) in enumerate(users):
	disney_users_C[j]=i
print(f"{disney_users_C}\n")

#4-1
print("Question 4")
print("----------")

disney_users_A={}
for (i,j) in enumerate(users):
	if 'i' in j:
		disney_users_A[j]=i
print(f"{disney_users_A}\n")

#4-2
print("Question 4-2")
print("------------")

disney_users_A={}
for (i,j) in enumerate(users):
	if j[0]=="p" or j[0]=="P" or j[0]=="m" or j[0]=="M":
		disney_users_A[j]=i
print(f"{disney_users_A}\n")'''