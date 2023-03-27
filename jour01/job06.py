class Rectangle:
    def __init__(self):
        self.longueur = 10
        self.largeur = 5
    def setLongueur(self, longueur):
        self.longueur = longueur
    def setLargeur(self, largeur):
        self.largeur = largeur
    def getLongueur(self):
        print("rectangle de longueur", self.longueur)
    def getLargeur(self):
        print("rectangle de largeur", self.largeur)

rectangle1 = Rectangle()
rectangle1.setLongueur(15)
rectangle1.setLargeur(10)
rectangle1.getLongueur()
rectangle1.getLargeur()


