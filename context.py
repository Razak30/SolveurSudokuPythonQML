from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot, pyqtProperty
from PyQt5.QtQml import QQmlListProperty
from plateau import Plateau
from case import Case
from qplateau import QPlateau
from qcase import QCase


class Context(QObject):
    qplateau_updated = pyqtSignal()
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.plateauQ = QPlateau()   

    def setContext(self, context):        
        self.m_context = context
        self.m_context.setContextProperty( "Context", self )
        print( "context settled")

    @pyqtSlot()
    def roundQ(self):
        self.plateauQ.p.round()
        self.plateauQ.tableau = [QCase(d) for d in self.plateauQ.p.grille]
        self.qplateau_updated.emit()
        print("round effectué")

    @pyqtSlot()
    def hardRoundQ(self):
        self.plateauQ.p.hardRound()
        self.plateauQ.tableau = [QCase(d) for d in self.plateauQ.p.grille]
        self.qplateau_updated.emit()
        print("hardRound effectué")

    @pyqtSlot("QString", result = "QString")
    def generate(self, a):
        ch = a
        if len(ch) == 81 :
            for i in range(0,81) :
                self.plateauQ.grilleQ[i].valeur = int(ch[i])
                #print(self.plateauQ.grilleQ[i].valeur)
                i = i +1
            self.plateauQ.tableau = [QCase(d) for d in self.plateauQ.p.grille]
            self.qplateau_updated.emit()
            print("generated")
            return "La grille a été générée"
        else :
            return "Erreur de format"

    @pyqtSlot()
    def clean(self):
        self.plateauQ = QPlateau()
        self.qplateau_updated.emit()

    @pyqtSlot(result=bool)
    def resolu(self):
        return self.plateauQ.p.isFini()

    @pyqtSlot(result=bool)
    def grillechanged(self):
        return self.plateauQ.p.isChanged()
    
    @pyqtSlot()
    def onTenteQ(self):
        self.plateauQ.p.onTente()
        self.plateauQ.tableau = [QCase(d) for d in self.plateauQ.p.grille]
        self.qplateau_updated.emit()


#=======================================================
    qplateau_updated = pyqtSignal()
    @pyqtProperty(QPlateau, notify=qplateau_updated)
    def plateauQ(self):
        return self.plateau

    @plateauQ.setter
    def plateauQ(self, plateau):        
        self.plateau = plateau
        self.qplateau_updated.emit()


if __name__ == "__main__":    
    print( "ok" )