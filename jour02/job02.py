class Personne:
    def __init__(self, age):
        self.age = age
    def afficherAge(self):
        print("Age :", self.age)
    def bonjour(self):
        print("Hello")
    def modifierAge(self, age):
        self.age = age

class Eleve(Personne):
    def __init__(self, age):
        Personne.__init__(self, age)
    def allerEnCours(self):
        print("Je vais en cours")
    def afficherAge(self):
        print("J'ai", self.age, "ans")

class Professeur(Personne):
    def __init__(self, matiereEnseignee, age):
        Personne.__init__(self, age)
        self.__matiereEnseignee = matiereEnseignee
    def enseigner(self):
        print("Le cours va commencer")

eleve1 = Eleve(15)
eleve1.bonjour()
eleve1.allerEnCours()
print()
professeur1 = Professeur("maths",40)
professeur1.bonjour()
professeur1.enseigner()


    