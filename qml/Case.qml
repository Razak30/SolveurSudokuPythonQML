import QtQuick 2.0

Rectangle{

    signal dominoClicke(int a, int b)

    id : root
    property int largeur : 60
    property int valeur : 0
    property int absysse : 0
    property int ordonnee : 0

    width : root.largeur
    height : root.largeur
    color : "ivory"
    border.width: 1
    antialiasing: true

    TextInput {
        id: textInput
        text: root.valeur
        font.wordSpacing: 0
        horizontalAlignment: Text.AlignHCenter
        anchors.fill: parent
        font.pixelSize: 24
        onTextChanged: root.valeur = text*1
    }





}
