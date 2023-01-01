#- Exercice 1

def display_message():
    print("j'apprend a creer et a manipuler des fonctions dans ce cours")

display_message()

'''
#🌟 Exercice 2 : Quel Est Votre Livre Préféré ?

def favorite_book(title):
	print(f"One of my favorite books is '{title}'")

favorite_book("L'ame du monde")
'''


'''
#🌟 Exercice 3 : Un Peu De Géographie

def describe_city(ville,pays="Burkina Faso"):
    print(f"{ville} est en {pays}")

describe_city("Ouagadougou")
'''

'''
#Exercice 4 : Aléatoire

def nombre_aleatoire(nombre):
    import random
    nombre_aleatoire=random.randint(1,100)
    if nombre==nombre_aleatoire:
        print('bravo')
    else:
        print(f"dommage le nombre etait {nombre_aleatoire}")


nombre_aleatoire(50)
'''

'''
#🌟 Exercice 5 : Créons Des Chemises Personnalisées !

def make_shirt(taille,message):
    print(f"la taille de la chemise est <{taille}> et le texte est <{message}>")

make_shirt('S','Good Night')

#5-4
def make_shirt(taille="XXL",message="I Love Python"):
    print(f"la taille de la chemise est <{taille}> et le texte est <{message}>")

print("Chemise avec taille et message par defaut")
print('-----------------------------------------')
make_shirt()

print("\nChemise message par defaut")
print('---------------------------')
make_shirt('XL')


print("\nChemise avec taille et message quelquonque")
print('-----------------------------------------')
make_shirt("LM","Bonjour tous le monde")

'''

'''

#🌟 Exercice 6 : Magiciens …

magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']
def presentation_magicien(liste):
    for i in liste:
        print(f"mon nom est: {i}")
#-------------------------------------------------------------------------
def show_magician(liste):
    print(new)

#--------------------------------------------------------------------------

def make_great(liste):
    new=[]
    for i in liste:
        new.append(i+" the Great")
    return new
#---------------------------------------------------------------------------
presentation_magicien(magician_names)

new=make_great(magician_names)
show_magician(new)

'''



'''
#🌟 Exercice 7 : Conseils De Température


#--------------LES FONCTIONS-----------------------------------------------------


def get_random_temp():
    import random 
    degre=random.randint(-10,40)
    return degre
#print(f"le degre est de: {get_random_temp()}")

#-------------------------------------------------------------------------

def get_random_temp_2(saison):
    import random 
    if saison == 'Hiver':
        maxi=16
        mini=-10
    elif saison == 'Printemps':
        maxi=23
        mini=16
    elif saison == 'Automne':
        maxi=32
        mini=24
    elif saison == 'ete':
        maxi=40
        mini=33
    else:
        maxi=40
        mini=-10
    degre=random.randint(mini,maxi)
    return degre
#----------------------------------------------------------------------------------------------
#print(f"le degre est de: {get_random_temp()}")
def main():
    temperature=get_random_temp()
    print(f"la temperature actuelle est de {temperature}")
    if temperature <0:
        print("temperature glaciale!!! Veillez bien vous couvrir")
    elif temperature <16:
        print("Assez froid ! N'oubliez pas votre manteau")
    elif temperature <23:
        print("temperature Assez agreable ")
    elif temperature <32:
        print("Temps ensoleile ideal pour faire un tour a la plage")
    else:
        print("Chaleur ardente actuellement!! il est conseille de s'habiller leger")

#------------------------------------------------------------------------------------------------

def main_2():
    saison=input("Entrez une saison: ").capitalize()
    temperature= get_random_temp_2(saison)
    print(f"la temperature actuelle est de {temperature}")
    if temperature <0:
        print("temperature glaciale!!! Veillez bien vous couvrie")
    elif temperature <16:
        print("Assez froid ! N'oubliez pas votre manteau")
    elif temperature <23:
        print("temperature Assez agreable ")
    elif temperature <32:
        print("Temps ensoleile ideal pour faire un tour a la plage")
    else:
        print("Chaleur ardente actuellement!! il est conseille de s'habiller leger")

#---------------------BONUS------------BONUS--------------BONUS------------------BONUS-----------------


def get_random_temp_Bonus(mois):
    import random 
    if mois in (12,1,2):
        maxi=16
        mini=-10
    elif mois in (3,4,5):
        maxi=23
        mini=16
    elif mois in (9,10,11):
        maxi=32
        mini=24
    elif mois in (6,7,8):
        maxi=40
        mini=33
    else:
        maxi=40
        mini=-10
    degre=random.uniform(mini,maxi)
    degre=round(degre,1)
    return degre

#--------------------------------------------------------------------------


def main_Bonus():
    mois=int(input("Entrez le mois (compris entre 1 et 12): "))
    temperature= get_random_temp_Bonus(mois)
    print(f"la temperature actuelle est de {temperature}")
    if temperature <0:
        print("temperature glaciale!!! Veillez bien vous couvrie")
    elif temperature <16:
        print("Assez froid ! N'oubliez pas votre manteau")
    elif temperature <23:
        print("temperature Assez agreable ")
    elif temperature <32:
        print("Temps ensoleile ideal pour faire un tour a la plage")
    else:
        print("Chaleur ardente actuellement!! il est conseille de s'habiller leger")


from os import system
print("Test de la fonction Numero 1 : Fonctionalite Basique")
print("-----------------------------------------------------")
main()
print("\n")
system('pause')
system('cls')


print("Test de la fonction Numero 2 : Fonctionalite de Saison")
print("-----------------------------------------------------")
main_2()
print("\n")
system('pause')
system('cls')


print("Test de la fonction Numero 3 : Fonctionalite avec les mois")
print("----------------------------------------------------------")
main_2()
print("\n")

'''