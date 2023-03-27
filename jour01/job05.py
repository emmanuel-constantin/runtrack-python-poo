class Animal:
    def __init__(self):
        self.age = 0
        self.prenom = ""
        print("L'age de l'animal", self.age, "ans")
    def vieillir(self):
        self.age += 1
    def nommer(self, prenom):
        self.prenom = prenom
        


animal1 = Animal()
animal1.vieillir()
print("L'age de l'animal", animal1.age, "ans")
animal1.nommer("Toto")
print("L'animal se nomme", animal1.prenom)


