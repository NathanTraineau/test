class Student:
    def __init__(self, idStudent):
        self.idStudent = idStudent
        self.prefStudent = []
        self.prefObtainedStudent = []

    def getIdStudent(self):
        return int(self.idStudent)

    def getPrefStudent(self):
        return self.prefStudent

    def setPreference(self, table):
        self.prefStudent = table

    def setPreferenceObtained(self, table):
        self.prefObtainedStudent = table

    def getPreferenceObtained(self):
        return self.prefObtainedStudent

    def getAveragePreferenceObtained(self):
        return sorted(self.prefObtainedStudent)[int(len(self.prefObtainedStudent)/2)]

    def getVoteSuperior(self):
        avg = self.getAveragePreferenceObtained()
        nb = 0
        for i, pref in enumerate(self.prefObtainedStudent):
            if pref > avg:
                nb+=1
        return nb/len(self.prefObtainedStudent)

    def getVoteInferior(self):
        avg = self.getAveragePreferenceObtained()
        nb = 0
        for i, pref in enumerate(self.prefObtainedStudent):
            if pref < avg:
                nb+=1
        return nb/len(self.prefObtainedStudent)

    def displayStudent(self):
        print("Etudiant " + str(self.idStudent))

