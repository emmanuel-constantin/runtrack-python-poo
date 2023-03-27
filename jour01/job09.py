class Student:
    def __init__(self, prenom:str = "", nom:str = "", noetudiant: int = 0, credits: int = 0):
        self.__prenom = prenom
        self.__nom = nom
        self.__noetudiant = noetudiant
        self.__credits = credits
        self.__level = self.__studentEval()
    def add_credits(self, nbcredits):
        self.__credits += nbcredits
        print("Le nombre de crédits de", self.__prenom, self.__nom, "est", self.__credits, "points")
    
    def __studentEval(self):
        if self.__credits >= 90:
            return "Excellent"
        elif self.__credits >= 80:
            return "Tres bien"
        elif self.__credits >= 70:
            return "Bien"
        elif self.__credits >= 60:
            return "Passable"
        else:
            return "Insuffisant"
    def studentInfo(self):
        print("Prenom =", self.__prenom)
        print("Nom =",self.__nom )
        print("id =", self.__noetudiant)
        print("Niveau =", self.__level)


student1 = Student("John", "Doe", 145, 0)
student1.add_credits(61)
student1.studentInfo()