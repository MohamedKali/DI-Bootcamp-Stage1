
#Defis 1


chaine=input("Entrer un mot: ")
index={}
for (i,j) in enumerate(chaine):
	if j in index.keys():
		index[j].append(i)
	else:

		index[j]=[i]
print(index)

"""
# Defis 2
Produits_disponibles= {
  "Ordinateur": 300000,
  "RAM": 12000,
  "Carte Graphique":45000,
  "Cle USB":8000,
  "Clavier":15000,
  "Souris":7000,
  "Ecran":35000,
  "Batterie":25000
}
print('Listes des produits disponibles dans notre boutique')
print("---------------------------------------------------\n")
for i in Produits_disponibles:
	print(i)
budget=int(input("Entrer votre budjet: "))
panier=[]
for i in Produits_disponibles:
		if Produits_disponibles[i] <= budget:
			panier.append(i)
if not panier:
	print("Vous ne pouvez rien acheter")
else:
	print(f" vous pouvez acheter ses articles : {panier}")
"""