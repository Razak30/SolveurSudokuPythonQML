import QtQuick 2.0
import QtQuick.Layouts 1.3
import QtQuick.Controls 1.2

Item{
    height: 800
    width: 800

    Rectangle {
        id: rectangle
        x: 0
        y: 0
        width: 800
        height: 800
        color: "#ffffff"

        Rectangle{
            id : grille
            x: 194
            y: 31
            color : "lavender"
            height: 540
            width: 540
            Layout.preferredWidth: root.width *.15
            Layout.fillHeight: true
            Layout.alignment: Qt.AlignRight

            GridView{
                id : idGridView
                width: 540
                height: 540
                cellHeight: 60
                cellWidth: 60
                cacheBuffer: 320
                boundsBehavior: Flickable.StopAtBounds
                flickableDirection: Flickable.AutoFlickDirection
                anchors.fill: parent
                model : Context.plateauQ.grilleQ
                onModelChanged : console.log( "modelChangedfFrom QML")
                delegate : Case{
                    id : root
                    valeur : modelData.valeur
                    ordonnee : modelData.ordonnee
                    absysse : modelData.absysse

                    Keys.onReturnPressed :{
                        console.log(" ici")
                        modelData.valeur = root.valeur
                        root.color = "green"
                    }


                }

            }
        }

        Rectangle {
            id: btn2
            x: 8
            y: 543
            width: 115
            height: 47
            color: "#2f2f2f"
            Text {
                id: txtbtn2
                color: "#ffffff"
                text: qsTr("Débloquer")
                verticalAlignment: Text.AlignVCenter
                anchors.fill: parent
                MouseArea {
                    id: mouseArea1
                    anchors.rightMargin: 0
                    anchors.topMargin: 0
                    anchors.fill: parent
                    onClicked: {
                        console.log("RESOLUTION HARDCORE ")
                        Context.hardRoundQ()
                        if (Context.grillechanged())
                        {
                            textEtat.text = "Déblocage effectué ! ( Réessayez de résoudre )"

                        } else {
                            textEtat.text = "Le Sudoku est très compliqué ! Appuyez sur debug jusqu'à avoir la solution !"
                        }
                        btn2.color = "#2f2f2f"

                    }
                }
                font.pixelSize: 14
                horizontalAlignment: Text.AlignHCenter
            }
            border.width: 0
        }

        Rectangle {
            id: btndebug
            x: 8
            y: 480
            width: 115
            height: 47
            color: "#2f2f2f"
            border.width: 0
            Text {
                id: txtbtn3
                color: "#ffffff"
                text: qsTr("Debug")
                verticalAlignment: Text.AlignVCenter
                font.pixelSize: 14
                anchors.fill: parent
                horizontalAlignment: Text.AlignHCenter
                MouseArea {
                    id: mouseArea2
                    anchors.topMargin: 0
                    anchors.fill: parent
                    anchors.rightMargin: 0
                    onClicked: {
                        Context.onTenteQ()
                        if (Context.resolu())
                        {
                            textEtat.text = "Enfin résolu !"
                        } else {
                            textEtat.text = "Essayez le debug à nouveau (sauf si ça fait deja 20fois, envoyez moi la grille :) )"
                        }
                    }
                }
            }
        }

    }

    Rectangle {
        id: btn1
        x: 8
        y: 599
        width: 114
        height: 65
        color: "#2f2f2f"
        border.width: 0

        Text {
            id: txtbtn1
            color: "#ffffff"
            text: qsTr("Résoudre")
            verticalAlignment: Text.AlignVCenter
            horizontalAlignment: Text.AlignHCenter
            anchors.fill: parent
            font.pixelSize: 15

            MouseArea {
                id: mouseArea
                anchors.fill: parent
                onClicked: {
                    console.log("C'est partie, on resoud !")
                    Context.roundQ()
                    if (Context.resolu())
                    {
                        textEtat.text = "Le sudoku est résolu"
                    } else {
                        textEtat.text = "Le sudoku est compliqué essayez le deblocage"
                        btn2.color = "green"

                    }


                }


            }
        }
    }

    Rectangle {
        id: recGrille
        x: 0
        y: 670
        width: 800
        height: 130
        color: "#ffffff"
        TextField {
            id: t4
            x: 39
            y: 22
            width: 524
            height: 49
            placeholderText: qsTr("grille de sodoku")
            font.pixelSize: 12
        }

        Rectangle {
            id: recGen
            x: 582
            y: 22
            width: 172
            height: 49
            color: "#89ff77"
            Text {
                id: txtbtn4
                text: qsTr("Générer")
                verticalAlignment: Text.AlignVCenter
                horizontalAlignment: Text.AlignHCenter
                font.pixelSize: 21
                anchors.fill: parent

                MouseArea {
                    id: mouseArea3
                    anchors.fill: parent
                    onClicked: {

                        textEtat.text = Context.generate(t4.text)
                        btn2.color = "#2f2f2f"

                    }
                }
            }
        }

        Rectangle {
            id: recRei
            x: 582
            y: 88
            width: 172
            height: 27
            color: "#aa0204"
            Text {
                id: txtbtn5
                text: qsTr("Réinitialisé")
                font.pixelSize: 17
                verticalAlignment: Text.AlignVCenter
                MouseArea {
                    id: mouseArea4
                    anchors.fill: parent
                    onClicked: {
                        Context.clean()
                        textEtat.text = "Grille réinitialisée ! Entrez un Sudoku à résoudre !"
                        btn2.color = "#2f2f2f"
                    }
                }
                anchors.fill: parent
                horizontalAlignment: Text.AlignHCenter
            }
        }

    }

    Rectangle {
        id: recEtat
        x: 128
        y: 599
        width: 664
        height: 65
        color: "#5385b0"

        Text {
            anchors.fill: parent
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignVCenter
            id: textEtat
            x: 62
            y: 17
            color: "#ffffff"
            text: qsTr("Entrez un Sudoku à résoudre !")
            font.pixelSize: 16
        }
    }
}
