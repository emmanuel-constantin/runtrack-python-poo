class Vehicule:
    def __init__(self,marque,modele,annee,prix):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.prix = prix
    def informationsVehicule(self):
        print("Marque :",self.marque)
        print("Modele :",self.modele)
        print("Annee", self.annee)
        print("Prix :", self.prix)
    def demarrer(self):
        print("Attention je roule")

class Voiture(Vehicule):
    def __init__(self,marque,modele,annee,prix):
        Vehicule.__init__(self,marque,modele,annee,prix)
        self.portes = 4
    def informationsVehicule(self):
        print(super().informationsVehicule())
        print("nb portes :", self.portes)
    def demarrer(self):
        print("Attention je roule en voiture")

class Moto(Vehicule):
    def __init__(self,marque,modele,annee,prix):
        Vehicule.__init__(self,marque,modele,annee,prix)
        self.roue = 2
    def informationsVehicule(self):
        print(super().informationsVehicule())
        print("Nombre de roues :", self.roue)
    def demarrer(self):
        print("Attention je roule en moto")


voiture1 = Voiture("Mercedes","Classe A", 2020, 18500)
voiture1.informationsVehicule()
print()
moto1 = Moto("Yamaha", "1200 Vmax", 1987, 4500)
moto1.informationsVehicule()
print()
voiture1.demarrer()
print()
moto1.demarrer()