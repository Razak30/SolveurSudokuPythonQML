from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot, pyqtProperty
from PyQt5.QtQml import QQmlListProperty
from case import Case
from qcase import QCase
from plateau import Plateau


class QPlateau(QObject):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.p = Plateau()
        self.tableau = [QCase(d) for d in self.p.grille]

     #-----------------------------------------
    grille_updated = pyqtSignal()
    @pyqtProperty(QQmlListProperty, notify=grille_updated)
    def grilleQ(self):        
        #print( "grille updated")  
        return QQmlListProperty(QCase, self, self.tableau)
