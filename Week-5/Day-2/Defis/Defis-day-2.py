class Pagination():
    
    def __init__(self,items=[],pageSize=10):
        self.items=items
        self.pageSize=pageSize
        self.curseur=0
        self.taille=0

    def getVisibleItems(self):
        page=[]
        conteneur=[]
        compteur=1
        for i in self.items[0]:
            if compteur < self.pageSize:
                page.append(i)
                compteur= compteur+1
            else:
                page.append(i)
                conteneur.append(page)
                compteur=1
                page=[]

        conteneur.append(page)
        self.taille=len(conteneur)-1
        print(conteneur[self.curseur])

    def nextPage(self):
        if self.taille<=self.curseur:
            self.curseur=self.taille
        else:
            self.curseur+=1


    def lastPage(self):
        self.curseur=self.taille

    def firstPage(self):
        self.curseur=0

    def goToPage(self,number):
        if number > self.taille:
            self.curseur=self.taille
        elif number <= 0:
            self.curseur=0
        else:
            self.curseur=number

    def prevPage(self):
        if 0>=self.curseur:
            self.curseur=0
        else:
            self.curseur-=1


alphabetList = "abcdefghijklmnopqrstuvwxyz".split()

p = Pagination(alphabetList, 4)
print("page initiale")
p.getVisibleItems() 
print('\n')

#p.prevPage()
print('page suivante')
p.nextPage()
p.getVisibleItems()
print("\nderniere page")
p.lastPage()
p.getVisibleItems()
print("\npremiere page")
p.firstPage()
p.getVisibleItems()
print("\npage 3")
p.goToPage(3)
p.getVisibleItems()
print('\npage precedente')
p.prevPage()
p.getVisibleItems()
