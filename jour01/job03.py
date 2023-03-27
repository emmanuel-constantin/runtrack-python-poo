class Operation:
    def __init__(self):
        self.nombre1 = 12
        self.nombre2 = 3
        print("le nombre1 est",self.nombre1)
        print("le nombre2 est",self.nombre2)
    def addition(self):
        self.resultat = self.nombre1 + self.nombre2
        print("le resultat de l'addition de", self.nombre1, "et", self.nombre2, "est", self.resultat)


operation1 = Operation()
operation1.addition()