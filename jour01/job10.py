class Voiture:
    def __init__(self):
        self.__marque= ""
        self.__modele= ""
        self.__Km= 0
        self.__en_marche = False
        self.__reservoir= 6
    
    def setMarque(self, marque):
        self.__marque = marque
    
    def setModele(self, modele):
        self.__modele = modele
    
    def setKm(self, Km):
        self.__Km = Km
    
    def setEnMarche(self, en_marche):
        self.__en_marche = en_marche
    
    def getMarque(self):
        print("Marque :", self.__marque)
    
    def getModele(self):
        print("Modele :", self.__modele)
    
    def getKm(self):
        print("Kilometrage :", self.__Km)
    
    def getEnMarche(self):
        print("En marche :", self.__en_marche)
    
    def demarrer(self):
        if self.__verifier_plein() > 5:
            self.__en_marche = True
        else:
            print("La voiture n'a pas assez d'essence dans le réservoir:", self.__reservoir, "L")
    def arreter(self):
        self.__en_marche = False

    def __verifier_plein(self):
        return self.__reservoir

voiture1 = Voiture()
voiture1.demarrer()
voiture1.getEnMarche()
