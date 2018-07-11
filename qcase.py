from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot, pyqtProperty
from PyQt5.QtQml import QQmlListProperty
from case import Case


class QCase(QObject):

    absysse_updated = pyqtSignal()
    ordonnee_updated = pyqtSignal()
    valeur_updated = pyqtSignal()
       
    def __init__(self, case, parent=None):
        super().__init__(parent)
        self.c = case


    @pyqtProperty(int, notify=valeur_updated)
    def valeur(self):
        #print("=>QCase getter", self.c.v)       
        return self.c.v

    @valeur.setter
    def valeur(self, e):
        self.c.v = e
        #print("QCase setter =>", self.c.v)
        self.valeur_updated.emit()

    @pyqtProperty(int, notify=absysse_updated)
    def absysse(self):       
        return self.c.x

    @pyqtProperty(int, notify=ordonnee_updated)
    def ordonnee(self):       
        return self.c.y
    

    