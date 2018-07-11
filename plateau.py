from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot, pyqtProperty
from case import Case
import copy


class Plateau:
    def __init__(self):
        self.grille = []
        for i in range(9):
            for j in range(9):
                self.grille.append(Case(i, j))
        self.savegrille = copy.deepcopy(self.grille)
        self.vtest = []
        

    def testTout(self,case):
        i = case.x
        j = case.y
        u = case.carre

        for d in self.grille :
            if d.x == i and d.v in case.possible:
                case.possible.pop(case.possible.index(d.v))
            if d.y == j and d.v in case.possible :
                case.possible.pop(case.possible.index(d.v))
            if (d.carre == u) and (d.v in case.possible) :
                case.possible.pop(case.possible.index(d.v))
        
        for e in case.possible :
            kligne = 0
            kcarre = 0
            kcol = 0

            for f in self.grille :
                if (f.x == i) and (e in f.possible):
                    kligne += 1
                if (f.y == j) and (e in f.possible):
                    kcol += 1
                if (f.carre == u) and (e in f.possible):
                    kcarre += 1 

            if kcarre == 1 or kcol == 1 or kligne == 1 :
                case.possible2 = [e]


#Stratégie des chiffres exclusifs
    def hardClean(self,case):

        for numPos in case.possible :
            numPosSurAutreLigne = False
            numPosSurAutreCol = False

            for d in self.grille:
                if (d.carre == case.carre) and (numPos in d.possible):

                    if (d.x in case.autreligne) :
                        numPosSurAutreLigne = True

                    if (d.y in case.autrecol) :
                        numPosSurAutreCol = True
            
            if not numPosSurAutreLigne :
                for g in self.grille :
                    if (g.x == case.x) and (g.carre != case.carre) and (numPos in g.possible):
                        g.possible.pop(g.possible.index(numPos))
                        #print("num= ", numPos,",x = ", g.x, ",y = ", g.y , "testligne", "xdutest = ",case.x , "ydutest = ",case.y)
            
            if not numPosSurAutreCol :
                for g in self.grille :
                    if (g.y == case.y) and (g.carre != case.carre) and (numPos in g.possible):
                        g.possible.pop(g.possible.index(numPos))
                        #print("num= ", numPos,",x = ", g.x, ",y = ", g.y , "testcol","xdutest = ",case.x , "ydutest = ",case.y)

    
    #Stratégie des chiffres exclusifs dans une Région
    def hardCleanCarre(self,case):
        for numPos in case.possible :
            numPosHorsCarreMemeLigne = False
            numPosHorsCarreMemeCol = False

            for d in self.grille : 
                if (d.x == case.x) and (d.carre != case.carre) and (numPos in d.possible) :
                    numPosHorsCarreMemeLigne = True
                if (d.y == case.y) and (d.carre != case.carre) and (numPos in d.possible) :
                    numPosHorsCarreMemeCol = True
            
            if not numPosHorsCarreMemeLigne :
                for g in self.grille :
                    if (g.carre == case.carre) and (g.x != case.x) and (numPos in g.possible) :
                        g.possible.pop(g.possible.index(numPos))
                        #print("num= ", numPos,",x = ", g.x, ",y = ", g.y , "testligne2", "xdutest = ",case.x , "ydutest = ",case.y)

            if not numPosHorsCarreMemeCol :
                for g in self.grille :
                    if (g.carre == case.carre) and (g.y != case.y) and (numPos in g.possible) :
                        g.possible.pop(g.possible.index(numPos))
                        #print("num= ", numPos,",x = ", g.x, ",y = ", g.y , "testCol2", "xdutest = ",case.x , "ydutest = ",case.y)

            
    #Strategie des paires exclusive
    def hardCleanPaire(self,case):
        if len(case.possible) == 2:
            pairLigne = 0
            pairCol = 0
            pairCarre = 0
            
            for z in self.grille :
                if z.possible == case.possible and z.x == case.x and z != case :
                    pairLigne +=1
                    #print("TEST2possibilité ligne ","xdutest = ",case.x , "ydutest = ",case.y , "x = ", z.x , "y =" , z.y, "nb : ", pairLigne)
                if z.possible == case.possible and z.y == case.y and z != case :
                    pairCol += 1
                    #print("TEST2possibilité colone ","xdutest = ",case.x , "ydutest = ",case.y , "x = ", z.x , "y =" , z.y, "nb : ",pairCol)
                if z.possible == case.possible and z.carre == case.carre and z != case : 
                    pairCarre += 1
                    #print("TEST2possibilité carre ","xdutest = ",case.x , "ydutest = ",case.y , "x = ", z.x , "y =" , z.y, "nb : ",pairCarre )
                
            if pairLigne == 1 :
                for u in self.grille :
                    if u.x == case.x and len(u.possible) > 2:
                        for h in case.possible :
                            if h in u.possible :
                                u.possible.pop(u.possible.index(h))
                                #print("num= ", h,",x = ", u.x, ",y = ", u.y , "PaireLIGNE", "xdutest = ",case.x , "ydutest = ",case.y,u.possible)
             
            if pairCol == 1 :
                for u in self.grille :
                    if u.y == case.y and len(u.possible) > 2:
                        for h in case.possible :
                            if h in u.possible :
                                u.possible.pop(u.possible.index(h))
                                #print("num= ", h ,",x = ", u.x, ",y = ", u.y , "PaireCOLONNE", "xdutest = ",case.x , "ydutest = ",case.y,u.possible)

            if pairCarre == 1 :
                for u in self.grille :
                    if u.carre == case.carre and len(u.possible) > 2:
                        for h in case.possible :
                            if h in u.possible :
                                u.possible.pop(u.possible.index(h))
                                #print("num= ", h ,",x = ", u.x, ",y = ", u.y , "PaireCARRE", "xdutest = ",case.x , "ydutest = ",case.y,u.possible)


    def verif(self, case):
        if len(case.possible) == 1 and case.v == 0:
            case.v = case.possible[0]
        if case.v != 0:
            case.possible = []
        if len(case.possible2) == 1 and case.v == 0:
            case.v = case.possible2[0]


    def round1tour(self):
        for d in self.grille : 
            self.testTout(d)
            self.verif(d)
            #print("x :",d.x, "y : ", d.y, "carré : ", d.carre, "valeur : " , d.v ,"possible : ",d.possible)


    def round(self):
        while self.isChanged() and not self.isFini():
            self.savegrille = copy.deepcopy(self.grille)
            self.round1tour()

           
    def isFini(self):
        self.fini = True
        for d in self.grille :
            if d.v ==0 :
                self.fini = False
        return self.fini


    def isChanged(self):
        self.changed = False
        for d in range(0,81) :
            if  not ( self.grille[d].possible == self.savegrille[d].possible ) or not (self.grille[d].v == self.savegrille[d].v) :
                self.changed = True
        return self.changed


    def hardRound(self):
        for d in self.grille :
            self.hardCleanCarre(d)
            self.verif(d)
            self.hardClean(d)
            self.verif(d)
            self.hardCleanPaire(d)
            self.verif(d)
            #print("x :",d.x,"y : ",d.y,"carré : ",d.carre,"valeur : ",d.v,"possible : ",d.possible)
            
    def onTente(self):
        self.savedgrille = copy.deepcopy(self.grille)
        self.trybool = False
        c = 0
        while not ( self.trybool ) and (c < 81) :
            casetest = self.grille[c]

            if (len(casetest.possible) == 2) and (casetest.v == 0) :

                if not ( (c,0) in self.vtest ) :
                    casetest.v = casetest.possible[0]
                    self.vtest.append( (c,0) )
                    self.trybool = True

                elif not( (c,1) in self.vtest ) :
                    casetest.v = casetest.possible[1]
                    self.vtest.append( (c,1) )
                    self.trybool = True
            c += 1

        
        self.round()
        self.hardRound()
        self.round()
        self.hardRound()
        self.round()
        self.hardRound()
        if not self.isFini() :
            self.grille = self.savedgrille



            

            




