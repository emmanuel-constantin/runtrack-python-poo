class Forme:
    def __init__(self):
        None
    def aire(self):
        return 0
    
class Cercle(Forme):
    def __init__(self):
        self.radius = 3
    def aire(self):
        self.aire = ((self.radius)**2)*3.14
        print(self.aire)

class Rectangle(Forme):
    def __init__(self):
        self.largeur = 10
        self.hauteur = 5
    def aire(self):
        self.aire = self.largeur * self.hauteur
        print(self.aire)

rectangle1 = Rectangle()
rectangle1.aire()

cercle1 = Cercle()
cercle1.aire()



