class Forme:
    def __init__(self):
        None
    def aire(self):
        return 0
    
class Rectangle(Forme):
    def __init__(self):
        self.largeur = 10
        self.hauteur = 5
    def aire(self):
        self.aire = self.largeur * self.hauteur
        print(self.aire)

rectangle1 = Rectangle()
rectangle1.aire()