import math

class Group:
    def __init__(self):
        self.members = []
        self.prefCombined = []

    def addStudent(self, student):
        self.members.append(student)

    def getSize(self):
        return len(self.members)

    def displayGroup(self):
        print("Etudiants : ")
        for student in self.members:
            student.displayStudent()

    def getPreferenceCombined(self):
        #If the combined preference matrix doesn't exist
        if(self.prefCombined == []):
            n = len(self.members)
            grid = [[0] * n for i in range(n)]

            for i,row in enumerate(grid):
                for j,elem in enumerate(row):
                    grid[i][j] = self.members[i].getPrefStudent()[j] + self.members[j].getPrefStudent()[i]
            self.prefCombined = grid
            return grid
        else:
            return self.prefCombined

    def computePreferenceObtained(self):
        for i, student in enumerate(self.members):
            preferenceObtained = []
            for j, stud in enumerate(self.members):
                pref = self.members[j].getPrefStudent()[i]
                if pref != -1:
                    preferenceObtained.append(pref)
            self.members[i].setPreferenceObtained(preferenceObtained)

    def getSortedStudents(self):
        if(len(self.members[0].getPreferenceObtained()) == 0):
            self.computePreferenceObtained()
        grpSorted = []
        for student in self.members:
            studAdded = False
            index = 0
            while(studAdded != True):
                if(len(grpSorted)==index):
                    grpSorted.append(student)
                    studAdded = True
                else:
                    if(grpSorted[index].getAveragePreferenceObtained() == student.getAveragePreferenceObtained()):
                        voteMax = max(grpSorted[index].getVoteInferior(), grpSorted[index].getVoteSuperior(),student.getVoteSuperior(), student.getVoteInferior())
                        if(voteMax == grpSorted[index].getVoteInferior() or voteMax == student.getVoteSuperior()):
                            grpSorted.insert(index, student)
                            studAdded = True
                    else:
                        if(grpSorted[index].getAveragePreferenceObtained() < student.getAveragePreferenceObtained()):
                            grpSorted.insert(index, student)
                            studAdded = True
                index = index+1
        return grpSorted

    def getIndexStudent(self, student):
        index = 0;
        trouve = False
        res = 0
        while (index != len(self.members) and (trouve == False)):
            if(self.members[index].getIdStudent() == student.getIdStudent()):
                res = index
            index+=1
        return res

    def getPreferedMutualStudent(self, student):
        maxPref = 0
        res = 0
        for i, pref in enumerate(self.getPreferenceCombined()[self.getIndexStudent(student)]):
            if pref > maxPref:
                maxPref = pref
                res=i
        return self.members[res]

    def getAllEqualStudents(self, student1, student2, studToAssign):
        #fonction qui retourne une liste des autres students (n'étant pas deja dans un groupe
        #qui ont une note combiné égale
        #au student2 par rapport au student1
        currentPref = self.getPreferenceCombined()[self.getIndexStudent(student1)][self.getIndexStudent(student2)]
        res = 0
        listEqualStud = [student2]
        for i, pref in enumerate(self.getPreferenceCombined()[self.getIndexStudent(student1)]):
            if pref == currentPref:
                if self.members[i] in studToAssign :
                        listEqualStud.append(self.members[i])
        return listEqualStud
                

    def getPreferedMutualList(self, student):
        l = self.getPreferenceCombined()[self.getIndexStudent(student)]
        print(l)
        res = []
        for i, pref in enumerate(self.getPreferenceCombined()[self.getIndexStudent(student)]):
            maxVal = max(l)
            if(maxVal != -1):
                maxId = l.index(maxVal)
                res.append(self.members[maxId])
                l[maxId] = -1
        return res

    def getNbGrp3(self):
        taille = self.getSize()
        res = -1
        if(taille>54):
            res = -1
        else:
            if(taille<=36):
                if(taille%2 == 1):
                    res = 1
                else:
                    res= 0
            else:
                for i in range(0,19):
                    nbgrp2 = (taille-(i*3))/2
                    if((math.fmod(nbgrp2,1.0) == 0.0) and nbgrp2+i == 18.0):
                        res = i
        return res






