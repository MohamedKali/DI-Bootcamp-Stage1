#🌟 Exercice 1 : Animaux Domestiques

class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Siamois(Cat):
    pass

chat1=Bengal('Aline',3)
chat2=Chartreux('prixi',1)
chat3=Siamois('Mix',2.5)
all_cats=[chat1,chat2,chat3]
sara_pets=Pets(all_cats)
sara_pets.walk()


#🌟 Exercice 2 : Chiens

class Dog:
    def __init__(self,name,age,weight):
        self.name=name
        self.age=age
        self.weight=weight

    def bark(self):
        return f"'{self.name}' aboie"

    def run_speed(self):
        return (self.weight/self.age*10)

    def fight(self,other_dog):
        run_speed1=self.run_speed()
        run_speed2=other_dog.run_speed()
        if run_speed1*self.weight >run_speed2*other_dog.weight:
            return self
        else:
            return other_dog

'''

chien1=Dog("Rex",4,20)
chien2=Dog("Milou",1,10)
chien3=Dog("Medor",6,26)

print(chien1.bark())
print(chien2.bark())
print(chien3.bark())

print(f"run_speed de {chien1.name} : {chien1.run_speed()}")
print(f"run_speed de {chien2.name} : {chien2.run_speed()}")
print(f"run_speed de {chien3.name} : {chien3.run_speed()}")
vainqueur=chien3.fight(chien1)
print(f"le vainqueur est : {vainqueur.name}")
'''


#🌟 Exercice 3 : Chiens Domestiqués
'''
class PetsDog(Dog):
    def __init__(self,name,age,weight,trained):
        self.name=name
        self.age=age
        self.weight=weight
        self.trained=True

    def train(self):
        self.trained=True
        print(self.bark())

    def play(self,*args):
        liste=[]
        for i in args:
            liste.append(i)
        liste=' '.join(liste)
        print(f"{liste} tous jouent ensemble")

    def do_a_trick(self):
        import random
        liste=[f"{self.name} fait un tonneau ",f"{self.name} se dresse sur ses pattes arrieres "
        ,f"{self.name} te serre la main ",f"{self.name} fait le mort",]
        a=random.choice(liste)
        if self.trained==True:
            print(a)


A=PetsDog('Rex',12,20,True)
A.do_a_trick()
'''