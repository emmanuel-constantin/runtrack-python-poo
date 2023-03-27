class Rectangle:
    def __init__(self):
        self.__longueur = 10
        self.__largeur = 5
    def setLongueur(self, longueur):
        self.__longueur = longueur
    def setLargeur(self, largeur):
        self.__largeur = largeur
    def getLongueur(self):
        print("rectangle de longueur", self.__longueur)
    def getLargeur(self):
        print("rectangle de largeur", self.__largeur)

rectangle1 = Rectangle()
rectangle1.setLongueur(15)
rectangle1.setLargeur(10)
rectangle1.getLongueur()
rectangle1.getLargeur()


