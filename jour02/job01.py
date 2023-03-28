class Personne:
    def __init__(self):
        self.age = 14
    def afficherAge(self):
        print("Age :", self.age)
    def bonjour(self):
        print("Hello")
    def modifierAge(self, age):
        self.age = age

class Eleve(Personne):
    def allerEnCours(self):
        print("Je vais en cours")
    def afficherAge(self):
        print("J'ai", self.age, "ans")

class Professeur(Personne):
    def __init__(self, matiereEnseignee):
        self.__matiereEnseignee = matiereEnseignee
    def enseigner(self):
        print("Le cours va commencer")

personne1 = Personne()
eleve1 = Eleve()
eleve1.afficherAge()

    