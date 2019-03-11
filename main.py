# coding: utf-8
import csv
from student import *
from group import *

def main():
    grp = Group()

    with open('C:/Users/Nathan/Desktop/Group-Making-master/preferences.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for i,row in enumerate(spamreader):
            if(i!=0):
                idStudent = row[0]
                if(idStudent != ""):
                    stud = Student(idStudent)
                    del row[0]
                    preference = []
                    for note in row:
                        if(note == "AR"):
                            preference.append(0)
                        if(note == "I"):
                            preference.append(1)
                        if(note == "P"):
                            preference.append(2)
                        if(note == "AB"):
                            preference.append(3)
                        if(note == "B"):
                            preference.append(4)
                        if(note == "TB"):
                            preference.append(5)
                        if(note == "-1"):
                            preference.append(-1)
                    stud.setPreference(preference)
                    grp.addStudent(stud)
    for stud in  grp.members:
        print(str(stud.getIdStudent())+" prefere "+ str(grp.getPreferedMutualStudent(stud).getIdStudent()))
    print(" ")

    studToAssign = grp.getSortedStudents()
    nbGrp3Left = grp.getNbGrp3()
    finalRep = []
    fini =False
    res = 0
    
    while True:
         assigneGrp(finalRep,studToAssign, nbGrp3Left,0,grp)

def assigneGrp(finalrep,studToAssign, nbGrp3Left,jmax,grp):
    if len(studToAssign)<=0 :    
        for i,grp in enumerate(finalrep):
            print(" ")
            print("groupe "+ str(i))
            for j in finalrep[i]:
                print(str(j.getIdStudent()))
        writeDoc(finalrep)

        
    l = grp.getPreferedMutualList(studToAssign[0])
    print(studToAssign[0].getIdStudent())
    print("J'assigne : " + str(studToAssign[0].getIdStudent())+ " et sa matrice : "+ str(l))
    trouve = False
    j = 0
        
    while trouve == False and j<len(l)-1 and j<len(studToAssign)-1:
        print("Je teste "+ str(j) + " et il me reste "+ str(studToAssign))
        if(l[j] in studToAssign):
            #si le 1er student dans la liste de pref student à assigner est encore libre
            print("J'ajoute " + str(l[j].getIdStudent()) + " et "+ str(studToAssign[0].getIdStudent()))
            print("Je retire "+str(l[j].getIdStudent()))
            #quand on en a trouvé un on guette si il n'y a pas de student en égalité avec
            allEqualStudents = grp.getAllEqualStudents(studToAssign[0],l[j],studToAssign)
            for eq in allEqualStudents :
                if nbGrp3Left > 0:
                    degreCourant = 10
                    while trouve == False:
                        for stud in studToAssign:
                            if grp.prefCombined[grp.getIndexStudent(stud)][grp.getIndexStudent(eq)]>=degreCourant:
                                if grp.prefCombined[grp.getIndexStudent(stud)][grp.getIndexStudent(studToAssign[0])]>=degreCourant:
                                    if trouve == False and eq.getIdStudent() != stud.getIdStudent() and studToAssign[0].getIdStudent() != stud.getIdStudent():
                                        print("J'ajoute " + str(stud.getIdStudent()) + " de degré "+ str(degreCourant))
                                        trouve = True
                                        repForce3(list(finalrep),studToAssign[0] ,eq , stud, list(studToAssign), int(nbGrp3Left),int(jmax),grp)
                                        return 0
                        degreCourant = degreCourant-1
                else:
                    if eq.getIdStudent() != studToAssign[0].getIdStudent():
                        repForce2(list(finalrep),studToAssign[0],eq , list(studToAssign), int(nbGrp3Left), int(jmax),grp)
                        trouve = True
                        return 0
        else :
            j+=1
        jmax+=1

    
        

def repForce2(finalrep,stud1 ,stud2 , studToAssign, nbGrp3Left,jmax,grp):
    currentGrp=[stud1,stud2]
    studToAssign.remove(stud1)
    studToAssign.remove(stud2)
    finalrep.append(currentGrp)
    assigneGrp(finalrep,studToAssign, nbGrp3Left,jmax,grp)

def repForce3(finalrep,stud1 ,stud2 , stud3, studToAssign, nbGrp3Left,jmax,grp):
    currentGrp=[stud1,stud2,stud3]
    studToAssign.remove(stud1)
    studToAssign.remove(stud2)
    studToAssign.remove(stud3)
    finalrep.append(currentGrp)
    assigneGrp(finalrep,studToAssign, nbGrp3Left-1,jmax,grp)

    
def writeDoc(repartition):
    line = ""
    for i, grp in enumerate(repartition):
        for j in repartition[i]:
            line = line + str(j.getIdStudent()) + " "
        line = line + "; "
    line = line.split(";")
    print(line)

    with open('FGT.csv', 'r') as readFile:
        reader = csv.reader(readFile)
        lines = list(reader)
        lines[0] = line

    with open('FGT.csv', 'w') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(lines)


main()
