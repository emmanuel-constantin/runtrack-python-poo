class Livre:
    def __init__(self):
        self.__titre = ""
        self.__auteur = ""
        self.__nbPages = 0
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
livre1.setTitre("Le Seigneur des Anneaux")
livre1.setAuteur("J.R.R. Tolkien")
livre1.setnbPages(800)
livre1.getTitre()
livre1.getAuteur()
livre1.getnbPages()
