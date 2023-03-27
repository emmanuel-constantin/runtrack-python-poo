class Livre:
    def __init__(self):
        self.__titre = ""
        self.__auteur = ""
        self.__nbPages = 0
        self.__disponible = True 

    def verification(self):
        if self.__disponible == True:
            return True 
        else:
            return False
        
    def emprunter(self):
        if self.verification():
            self.__disponible = False
        else:
            print("Livre indisponible")


    def rendre(self):
        if not self.verification():
            self.__disponible = True
        else :
            print("le livre est disponible ! vous ne pouvez pas le rendre")

    def setTitre(self, titre):
        self.__titre  = titre

    def setAuteur(self, auteur):
        self.__auteur = auteur

    def setnbPages(self, nbPages):
        if isinstance(nbPages, int) and nbPages > 0:
            self.__nbPages = nbPages
        else:
            print("Le nombre de pages entré n'est pas valide")

    def getTitre(self):
        print("Le titre est", self.__titre)

    def getAuteur(self):
        print("L'auteur est :", self.__auteur)

    def getnbPages(self):
        if int(self.__nbPages):
            print("Nombre de pages :", self.__nbPages)

livre1 = Livre()
livre1.emprunter()
livre1.rendre()
livre1.rendre()
livre1.emprunter()
livre1.emprunter()


