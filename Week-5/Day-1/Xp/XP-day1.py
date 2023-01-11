#🌟 Exercice 1 : Chats
class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age


def plus_grand(liste_cat):
    age=[]
    for i in liste_cat:
        age.append(i.age)
    grand=max(age)
    for i in liste_cat:
        print(i.age)
        if i.age==grand:
            return i

chat1=Cat('lili',4)
chat2=Cat('spy',2)
chat3=Cat('piwi',2)
super_chat=plus_grand([chat1,chat2,chat3])
print(f"Le chat le plus age est '{super_chat.name}' et a {super_chat.age}ans")
'''
#🌟 Exercice 2 : Chiens

class Dog:
    def __init__(self, dog_name, dog_height):
        self.name = dog_name
        self.heigth = dog_height

    def bark(self):
        print(f"{self.name} va Woof!")

    def jump(self):
        print(f"{self.name} saute {self.heigth*2} en cm de haut!")


davids_dog=Dog('Rex',50)
print(f"name dog: {davids_dog.name}, dog height: {davids_dog.heigth} ")

davids_dog.bark()
davids_dog.jump()

sarahs_dog=Dog("Teacup",20)

print(f"name dog: {sarahs_dog.name}, dog height: {sarahs_dog.heigth} ")

sarahs_dog.bark()
sarahs_dog.jump()

if sarahs_dog.heigth > davids_dog.heigth:
    print(f"le chien le plus grand est : {sarahs_dog.name}")
else:
    print(f"le chien le plus grand est : {davids_dog.name}")
'''

'''
#🌟 Exercice 3 : Qui Est Le Producteur De La Chanson ?

class Song:
    """docstring for ClassName"""
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for i in self.lyrics:
            print(i)

regarde_moi="""Regarde moi,je suis la France d'en bas,Le Chômage et la crise,Mais dit moi qui l'a combat?,Je vis au quotidien,Ce que tu ne connais pas,ce que tu ne comprend pas,Juste en bas de chez toi,Regarde moi,Regarde moi,Regarde moi,Regarde moi """
regarde_moi=regarde_moi.split(',')
#print(kiss)
soprano=Song(regarde_moi)
soprano.sing_me_a_song()

#Exercice 4 : Après-Midi Au Zoo

class Zoo:
    def __init__(self,zoo_name):
        self.name=zoo_name
        self.animals=[]
    def add_animal(self,new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)

    def get_animal(self):
        for i in self.animals:
            print(i)

    def seel_animal(self,animal_sold):
        if new_animal in self.animals:
            self.animals.remove('animal_sold')
        else:
            print(f"{animal_sold} n'est pas dans notre zoo")

    def sort_animal(self):
        self.animals.sort()
        let=self.animals[0][0]
        liste=[]
        dico={}
        j=1
        for i in self.animals:
            if i[0]==let:
                liste.append(i)
                dico[j]=liste

            else:
                let=i[0]
                liste=[]
                j+=1
                liste.append(i)
            
        return dico


    def get_group(self,dico):
        j=1
        for i in dico.values():
            i=' '.join(i)
            print(f'group {j}: {i}')
            j+=1


ramat_gan_safari=Zoo("Abobo")

ramat_gan_safari.add_animal("mouton")
ramat_gan_safari.add_animal("bufle")
ramat_gan_safari.add_animal("canard")
ramat_gan_safari.add_animal("boeuf")
ramat_gan_safari.add_animal("lion")
ramat_gan_safari.add_animal("caiman")
ramat_gan_safari.add_animal("lionne")
ramat_gan_safari.add_animal("cabri")
ramat_gan_safari.add_animal("yack")
ramat_gan_safari.add_animal("lyinx")
ramat_gan_safari.add_animal("baleine")
ramat_gan_safari.add_animal("lievre")
dico=ramat_gan_safari.sort_animal()
ramat_gan_safari.get_group(dico)
'''