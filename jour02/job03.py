class Rectangle:
    def __init__(self):
        self.__longueur = 10
        self.__largeur = 5
    
    def perimetre(self):
        self.perimetre = (self.__longueur + self.__largeur)*2
    
    def surface(self):
        self.surface = self.__longueur * self.__largeur
    
    def setLongueur(self, longueur):
        self.__longueur = longueur
    
    def setLargeur(self, largeur):
        self.__largeur = largeur
    
    def getLongueur(self):
        print("Longueur :", self.__longueur)
    
    def getLargeur(self):
        print("Largeur :", self.__largeur)

class Parallepipede(Rectangle):
    def __init__(self, hauteur):
        Rectangle.__init__(self)
        self.hauteur = hauteur

    def volume(self):
        self.volume = self.__longueur * self.__largeur * self.hauteur

