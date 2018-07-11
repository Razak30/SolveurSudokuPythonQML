class Case:
    def __init__(self, x, y):
        self.v = 0
        self.possible = [1,2,3,4,5,6,7,8,9]
        self.x = x
        self.y = y
        self.carre = 0
        self.setCarre()
        self.autreligne=[]
        self.autrecol=[]
        self.setLiCol()
        self.possible2 = []
        print("case etabli", x, y, self.carre)
        
    def setCarre(self):
        if self.x < 3 :
            if self.y < 3 :
                self.carre = 1
            elif self.y < 6 :
                self.carre = 4
            else :
                self.carre = 7
        elif self.x < 6 :
            if self.y < 3 :
                self.carre = 2
            elif self.y < 6 :
                self.carre = 5
            else :
                self.carre = 8
        else :
            if self.y < 3 :
                self.carre = 3
            elif self.y < 6 :
                self.carre = 6
            else :
                self.carre = 9

    def setLiCol(self):
        if self.x == 0 :
            self.autreligne = [1,2]
        elif self.x == 1 :
            self.autreligne = [0,2]
        elif self.x == 2:
            self.autreligne = [0,1]
        elif self.x == 3:
            self.autreligne = [4,5]
        elif self.x == 4:
            self.autreligne = [3,5]
        elif self.x == 5:
            self.autreligne = [3,4]
        elif self.x == 6:
            self.autreligne = [7,8]
        elif self.x == 7:
            self.autreligne = [6,8]
        elif self.x == 8:
            self.autreligne = [6,7]

        if self.y == 0 :
            self.autrecol = [1,2]
        elif self.y == 1 :
            self.autrecol = [0,2]
        elif self.y == 2:
            self.autrecol = [0,1]
        elif self.y == 3:
            self.autrecol = [4,5]
        elif self.y == 4:
            self.autrecol = [3,5]
        elif self.y == 5:
            self.autrecol = [3,4]
        elif self.y == 6:
            self.autrecol = [7,8]
        elif self.y == 7:
            self.autrecol = [6,8]
        elif self.y == 8:
            self.autrecol = [6,7]

    #def __str__(self):
    #    return str( self.v)
