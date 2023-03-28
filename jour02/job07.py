import random

class Jeu():
    def __init__(self):
        self.scorejoueur = 0
        self.paquet = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]*4
        self.mainjoueur = []
    def pioche(self):
        i = random.randint(1,14)
        self.mainjoueur.append(i)
        self.paquet.pop(i)
        
class Carte():
    def __init__(self):
        self.valeur = ""
        self.couleur = ""
        
        
    def setPaquet(self):
        self.paquet.append()

jeu1 = Jeu()
jeu1.pioche()




while True:
        scorejoueur = 0
        while scorejoueur < 21:
            nbdecarte = 0
            if 2 <= nbdecarte <= 10:
                scorejoueur += nbdecarte
            elif nbdecarte == 1:
                choix = int(input("Voulez vous 1 point (1) ou 11 points (2) ? : "))
                if choix == 1:
                    scorejoueur += 1
                elif choix == 2:
                    scorejoueur += 11
                else:
                    print("Choix invalide !")
        print("Jeu terminé !, score :", scorejoueur)
