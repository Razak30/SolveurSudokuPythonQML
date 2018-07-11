import sys

from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlContext, qmlRegisterType
from PyQt5.QtQuick import QQuickView
from PyQt5.QtCore import QUrl
from context import Context
from PyQt5.QtQml import QQmlListProperty

from plateau import Plateau
from case import Case
from qplateau import QPlateau
from qcase import QCase

if __name__ == "__main__":
    app = QGuiApplication(sys.argv)
    
    myApp = Context()
 
    view = QQuickView()
    view.resize(800, 800)
    view.setResizeMode(QQuickView.SizeRootObjectToView)

    qmlRegisterType(QPlateau, 'temp', 1, 0, 'QPlateau')
    qmlRegisterType(QCase, 'temp0', 1, 0, 'QCase')
        
    ctx = view.rootContext()
    myApp.setContext( ctx )
            
    view.setSource(QUrl("qml/main.qml"))
    view.show()
    
    sys.exit(app.exec_())
    