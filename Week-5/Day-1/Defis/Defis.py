class Farm:
    def __init__(self,name):
        self.name=name
        self.liste_animal={}
    def add_animal(self,name,number=1):
        if name in self.liste_animal:
            self.liste_animal[name]+=number
        else:
            self.liste_animal[name]=number

    def get_info(self):
        print(f"\n{self.name}'s farm\n\n")
        for i,j in self.liste_animal.items():
            print(f'{i} : {j}')
        return f"\nE-I-E-I-0!"

    def get_animal_types(self):
        liste=[]
        for i in self.liste_animal.keys():
            liste.append(i)
        liste.sort()
        return liste

    def get_short_info(self):
        liste=self.get_animal_types()
        last=liste.pop(-1)
        liste=' des '.join(liste)
        if 'des' in liste:
            liste=liste.replace(' des',', des')
        return f'la ferme {self.name} possede des {liste} et des {last}'


macdonald = Farm("McDonald")
macdonald.add_animal('cow',5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('rabbit',9)
macdonald.add_animal('goat', 12)
print(macdonald.get_info())
print(macdonald.get_short_info())