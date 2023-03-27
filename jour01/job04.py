class Personne:
    def __init__(self, prenom, nom):
        self.nom = nom
        self.prenom = prenom
    def SePresenter(self):
        print("Je suis", self.prenom,self.nom)

personne1 = Personne("John", "Doe")
personne2 = Personne("Jean", "Dupond")

personne1.SePresenter()
personne2.SePresenter()
 
