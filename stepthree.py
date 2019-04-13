from rubic import rubic
from edges_corners_checker import edges_corners_checker, edges


# faces = ['front', 'back', 'right', 'left', 'upper', 'down']
# numpy = [  0,        1,      2,       3  ,   4  ,       5]
#colors = ["green", "blue", "red", "orange", "white", "yellow"]


class stepthree():
    def __init__(self):

        self.origin = rubic()
        self.mvcurent = []
        self.mvorig = []

    def solver(self, cub, mv):
        if not edges_corners_checker(self.origin.cub, cub.cub,0,3):
            self.rot(cub, mv, 0, 3, 0)
        if not edges_corners_checker(self.origin.cub, cub.cub,3,1):
            self.rot(cub, mv, 3, 1, 3)
        if not edges_corners_checker(self.origin.cub, cub.cub, 1, 2):
            self.rot(cub, mv, 1, 2, 1)
        if not edges_corners_checker(self.origin.cub, cub.cub,2,0):
            self.rot(cub, mv, 2, 0, 2)

    def rot(self, cub,mv, col1, col2, face):
        self.mvorig=edges(self.origin.cub, col1, col2)
        self.mvcurent=edges(cub.cub, col1, col2)

        chlist=self.chside(cub, col1, col2)

        if isinstance(chlist, str):
            self.mv2try(cub, mv, col1, col2)
        else:
            if self.mvcurent[0] != 5:
                self.todown(cub, mv, col1, col2)
                self.mvcurent = edges(cub.cub,col1, col2)
            if self.mvcurent[0] !=5:
                print("Sushi vesla")
                exit()
            self.mvcurent = edges(cub.cub,col1, col2)
            if self.mvcurent[0]==5:
                self.mv2centr(cub, mv, col1,col2)
                self.mvcurent = edges(cub.cub, col1, col2)
                self.mv2try(cub, mv, col1,col2)

    # def checkSide(self, cubCurrent, colorsList):
    #     down, face, colorDown, colorFace = self.getSideParams(cubCurrent, colorsList)
    #     if (down != "down"):
    #         return [False, "null"]
    #     if (face == "front"):
    #         if (colorDown == "orange" and colorFace == "green"):
    #             return [True, "leftPattern"]
    #         elif (colorDown == "red" and colorFace == "green"):
    #             return [True, "rightPattern"]
    #     if (face == "back"):
    #         if (colorDown == "orange" and colorFace == "blue"):
    #             return [True, "leftPattern"]
    #         elif (colorDown == "red" and colorFace == "blue"):
    #             return [True, "rightPattern"]
    #     if (face == "right"):
    #         if (colorDown == "blue" and colorFace == "red"):
    #             return [True, "rightPattern"]
    #         elif (colorDown == "green" and colorFace == "red"):
    #             return [True, "leftPattern"]
    #     if (face == "left"):
    #         if (colorDown == "green" and colorFace == "orange"):
    #             return [True, "rightPattern"]
    #         elif (colorDown == "blue" and colorFace == "orange"):
    #             return [True, "leftPattern"]
    #     return [False, "null"]

    def todown(self, cub, mv, col1, col2):
        f1, f2, c1, c2 = self.getterofside(cub, col1, col2)
        p = self.ptodown(f1, f2)
        if p == 'RP':
            self.mv2r(cub, mv, f1)
        elif p == 'RLP':
            self.mv2r(cub, mv, f1)

    def ptodown(self, f1, f2):
        if f1 == 3:
            if f2 == 0:
                return 'RP'
            elif f2 == 1:
                return 'LP'
        elif f1 == 0 and f2 == 2:
            return 'RP'
        elif f1 == 2 and f2 == 1:
            return 'RP'

    def getterofside(self, cub, col1, col2):
        self.mvcurent=edges(cub.cub, col1, col2)
        return self.mvcurent[0], self.mvcurent[3],\
               self.mvcurent[-2], self.mvcurent[-1]

    def chside(self, cub, col1, col2):
        dwn, fc, cold, colf = self.getterofside(cub, col1, col2)
        if dwn != 5:
            return None
        if fc == 0:
            if cold == 3 and colf == 0:
                return 'LP'
            elif cold == 2 and colf == 0:
                return 'RP'
        if fc == 1:
            if cold == 3 and colf == 1:
                return 'LP'
            elif cold == 2 and colf == 1:
                return 'RP'
        if fc == 2:
            if cold == 1 and colf == 2:
                return 'RP'
            elif cold == 0 and colf == 2:
                return 'LP'
        if fc == 3:
            if cold == 0 and colf == 3:
                return 'RP'
            elif cold == 1 and colf == 3:
                return 'LP'
        return None


    def mv2try(self, cub, mv, col1, col2):
        dwn, fc, cold, colf = self.getterofside(cub, col1, col2)
        chl = self.chside(cub, col1, col2)
        if not isinstance(chl, str):
            return
        if chl == 'RP':
            self.mv2r(cub, mv, fc)
        elif chl == 'LP':
            self.mv2l(cub, mv, fc)

    def mv2r(self, cub, mv, fc):
        def appendix(list, cub, mv):
            for l in list:
                cub.rotate_by_name(l)
                mv.append(l)
        if fc == 0:
            appendix([ "D'", "R'", "D", "R", "D", "F", "D'", "F'" ], cub, mv)
        elif fc == 3:
            appendix([ "D'", "F'", "D", "F", "D", "L", "D'", "L'" ], cub, mv)
        elif fc == 2:
            appendix([ "D'", "B'", "D", "B", "D", "R", "D'", "R'"], cub, mv)
        elif fc == 1:
            appendix([ "D", "R", "D'", "R'", "D'", "B'", "D", "B" ], cub, mv)

    def mv2l(self, cub, mv, fc):
        def appendix(list, cub, mv):
            for l in list:
                cub.rotate_by_name(l)
                mv.append(l)
        if fc == 0:
            appendix([ "D", "L", "D'", "L'", "D'", "F'", "D", "F" ], cub, mv)
        elif fc == 3:
            appendix([ "D", "B", "D'", "B'", "D'", "L'", "D", "L" ], cub, mv)
        elif fc == 1:
            appendix([ "D'", "L'", "D", "L", "D", "B", "D'", "B'" ], cub, mv)
        elif fc == 2:
            appendix([ "D", "F", "D'", "F'", "D'", "R'", "D", "R" ], cub, mv)
    # def moveToCente(self, cubCurrent, solveMoveList, colorsList, face):
    #     checkSideList = self.checkSide(cubCurrent, colorsList)
    #     while (checkSideList[0] == False):
    #         cubCurrent.moveD()
    #         solveMoveList.append("D")
    #         checkSideList = self.checkSide(cubCurrent, colorsList)


    def mv2centr(self, cub, mv, col1, col2):
        chlst = self.chside(cub, col1, col2)
        while not isinstance(chlst, str):
            cub.D()
            mv.append('D')
            chlst = self.chside(cub, col1, col2)
