import random

class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur

    def get_valeur(self):
        if self.valeur in ['Valet', 'Dame', 'Roi']:
            return 10
        else:
            return int(self.valeur)

class Jeu:
    def __init__(self):
        self.paquet = []
        for couleur in ['Coeur', 'Carreau', 'Trèfle', 'Pique']:
            for valeur in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valet', 'Dame', 'Roi', 'As']:
                self.paquet.append(Carte(valeur, couleur))

    def melanger(self):
        random.shuffle(self.paquet)

    def distribuer(self):
        return self.paquet.pop()

class Joueur:
    def __init__(self, nom):
        self.nom = nom
        self.main = []

    def ajouter_carte(self, carte):
        self.main.append(carte)

    def get_total(self):
        total = 0
        for carte in self.main:
            total += carte.get_valeur()
        return total

class Croupier(Joueur):
    def __init__(self):
        self.nom = 'Croupier'
        self.main = []

    def montrer_carte_cachee(self):
        return self.main[0]

    def jouer(self):
        while self.get_total() < 17:
            self.ajouter_carte(jeu.distribuer())

jeu = Jeu()
jeu.melanger()

joueur1 = Joueur('Joueur')
croupier1 = Croupier()

joueur1.ajouter_carte(jeu.distribuer())
joueur1.ajouter_carte(jeu.distribuer())
croupier1.ajouter_carte(jeu.distribuer())
croupier1.ajouter_carte(jeu.distribuer())

print(f"Main du joueur1: [{joueur1.main[0].valeur} de {joueur1.main[0].couleur}, {joueur1.main[1].valeur} de {joueur1.main[1].couleur}], Total: {joueur1.get_total()}")
while joueur1.get_total() < 21:
    choix = input("Voulez-vous prendre une carte (p) ou passer (n)? ")
    if choix == 'p':
        carte = jeu.distribuer()
        joueur1.ajouter_carte(carte)
        if carte.valeur == 'As':
            choix_as = input("Vous avez pioché un As. Voulez-vous lui donner une valeur de 1 ou de 11? ")
            while choix_as != '1' and choix_as != '11':
                choix_as = input("Veuillez entrer une valeur valide pour l'As (1 ou 11): ")
            carte.valeur = choix_as
        print(f"Carte reçue: {carte.valeur} de {carte.couleur}")
        print(f"Main du joueur1: {[str(carte.valeur) + ' de ' + str(carte.couleur) for carte in joueur1.main]}, Total: {joueur1.get_total()}")
    else:
        break
    
print(f"Main du croupier1: [{croupier1.main[0].valeur} de {croupier1.main[0].couleur}, *]")
croupier1.jouer()
print(f"Main du croupier1: {[str(carte.valeur) + ' de ' + str(carte.couleur) for carte in croupier1.main]}, Total: {croupier1.get_total()}")
if joueur1.get_total() >= 21:
    print("Le joueur1 a dépassé 21, le croupier1 gagne.")
elif croupier1.get_total() >= 21:
    print("Le croupier1 a dépassé 21, le joueur1 gagne.")
elif joueur1.get_total() > croupier1.get_total():
    print("Le joueur1 a un total supérieur, il gagne.")
elif joueur1.get_total() < croupier1.get_total():
    print("Le croupier1 a un total supérieur, il gagne.")
else:
    print("Match nul.")
