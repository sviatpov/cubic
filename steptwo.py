
from rubic import rubic
from edges_corners_checker import edges_corners_checker, corners

# faces = ['front', 'back', 'right', 'left', 'upper', 'down']
# numpy = [  0,        1,      2,       3  ,   4  ,       5]
#colors = ["green", "blue", "red", "orange", "white", "yellow"]

class steptwo():
    # def __init__(self, cubOrigin):
    #     self.cubOrigin = cubOrigin
    #     self.listPositionCubCurrent = list()
    #     self.listPositionCubOrigin = list()
    #     self.checkerManager = CheckerColors()


    def __init__(self):
        self.origin = 0
        self.mvcurent = []
        self.mvorig = []

    def solver(self, cub, mvmain):
        if not edges_corners_checker(self.origin.cub, cub.cub,4, 0, 2):
            self.rotate(cub, mvmain, 4,0,2,0)
        if not edges_corners_checker(self.origin.cub, cub.cub,4, 2, 1):
            self.rotate(cub, mvmain, 4,2,1,2)
        if not edges_corners_checker(self.origin.cub, cub.cub,4, 1, 3):
            self.rotate(cub, mvmain, 4,1,3,1)
        if not edges_corners_checker(self.origin.cub, cub.cub,4, 3, 0):
            self.rotate(cub, mvmain, 4,3,0,3)

    # def moving(self, cubCurrent, solveMoveList, colorOne, colorTwo, colorThree, face):
    #     self.listPositionCubOrigin = self.updatePositionList(self.cubOrigin, colorOne, colorTwo, colorThree)
    #     self.listPositionCubCurrent = self.updatePositionList(cubCurrent, colorOne, colorTwo, colorThree)
    #
    #     if (self.checkSide(cubCurrent, face)) == False:
    #         if (self.listPositionCubCurrent[0][0] == "upper"):
    #             self.moveEdgeDown(cubCurrent, solveMoveList, colorOne, colorTwo, colorThree)
    #         if (self.listPositionCubCurrent[0][0] == "down"):
    #             self.moveEdgeDownToTryPosition(cubCurrent, solveMoveList, colorOne, colorTwo, colorThree, face)
    #     self.listPositionCubCurrent = self.updatePositionList(cubCurrent, colorOne, colorTwo, colorThree)
    #     if (self.checkSide(cubCurrent, face)) == True:
    #         self.moveSide(cubCurrent, solveMoveList, colorOne, colorTwo, colorThree, face)
    def rotate(self,cub,mv,col1,col2,col3,face):
        self.mvorig = corners(self.origin.cub, col1,col2,col3)
        self.mvcurent=corners(cub.cub, col1, col2, col3)

        if not self.facolor(cub, face):
            if self.mvcurent[0] == 4:
                self.mvcanny(cub, mv, col1,col2,col3)
            if self.mvcurent[0] == 5:
                self.mvcanny2(cub, mv,col1,col2,col3, face)
        self.mvcurent=corners(cub.cub,col1,col2,col3)
        if self.facolor(cub, face):
            self.mvfaces(cub, mv, col1,col2,col3, face)

    def facolor(self, cub, face):
        ff = {0: 2, 2: 1, 1: 3, 3: 0}
        ff = ff.get(face)
        if ff != None:
            return self.face2color(face, ff)
        return False

    # def checkSide(self, cubCurrent, face):
    #     if (face == "front"):
    #         return (self.checkDoubleSide(face, "right"))
    #     elif (face == "right"):
    #         return (self.checkDoubleSide(face, "back"))
    #     elif (face == "back"):
    #         return (self.checkDoubleSide(face, "left"))
    #     elif (face == "left"):
    #         return (self.checkDoubleSide(face, "front"))
    #     return False




    # def checkDoubleSide(self, face, subFace):
    #     count = 0
    #     i = 0
    #     while (i < len(self.listPositionCubCurrent)):
    #         if (((self.listPositionCubCurrent[i][0]) == face) or ((self.listPositionCubCurrent[i][0]) == subFace)):
    #             count += 1
    #         i += 1
    #     return (count == 2)


#### Mby trabls
    def face2color(self,fc, side):
        c=0
        if len(self.mvcurent) > 0:
            for i in range(0,3):
                if self.mvcurent[i*3]==fc or self.mvcurent[i*3]==side:
                    c+=1
        return c==2

    # def moveEdgeDown(self, cubCurrent, solveMoveList, colorOne, colorTwo, colorThree):
    #     self.listPositionCubCurrent = self.updatePositionList(cubCurrent, colorOne, colorTwo, colorThree)
    #     mixManager = MixManager()
    #     if ((self.listPositionCubCurrent[1][0] == "right" and self.listPositionCubCurrent[2][0] == "front")):
    #         mixManager.mixRun(["F", "D'", "F'"], cubCurrent)
    #         appendListInList(solveMoveList, ["F", "D'", "F'"])
    #     elif ((self.listPositionCubCurrent[1][0] == "left" and self.listPositionCubCurrent[2][0] == "front")):
    #         mixManager.mixRun(["F'", "D", "F"], cubCurrent)
    #         appendListInList(solveMoveList, ["F'", "D", "F"])
    #     elif ((self.listPositionCubCurrent[1][0] == "right" and self.listPositionCubCurrent[2][0] == "back")):
    #         mixManager.mixRun(["B'", "D", "B"], cubCurrent)
    #         appendListInList(solveMoveList, ["B'", "D", "B"])
    #     elif ((self.listPositionCubCurrent[1][0] == "left" and self.listPositionCubCurrent[2][0] == "back")):
    #         mixManager.mixRun(["B", "D'", "B'"], cubCurrent)
    #         appendListInList(solveMoveList, ["B", "D'", "B'"])
    #     self.listPositionCubCurrent = self.updatePositionList(cubCurrent, colorOne, colorTwo, colorThree)


    def mvcanny(self, cub, mv, col1,col2,col3):
        def appendix(list, cub, mv):
            for l in list:
                cub.rotate_by_name(l)
                mv.append(l)
        self.mvcurent = corners(cub.cub, col1,col2,col3)
        if self.mvcurent[3]==2 and self.mvcurent[6]==0:
            appendix(["F", "D'", "F'"], cub, mv)
        elif self.mvcurent[3]==3 and self.mvcurent[6]==0:
            appendix(["F'", "D", "F"], cub, mv)
        elif self.mvcurent[3]==2 and self.mvcurent[6]==1:
            appendix(["B'", "D", "B"], cub, mv)
        elif self.mvcurent[3]==3 and self.mvcurent[6]==1:
            appendix(["B", "D'", "B'"], cub, mv)
        self.mvcurent = corners(cub.cub, col1,col2,col3)
    #
    # def moveEdgeDownToTryPosition(self, cubCurrent, solveMoveList, colorOne, colorTwo, colorThree, face):
    #     while (self.checkSide(cubCurrent, face)) == False:
    #         cubCurrent.moveD()
    #         solveMoveList.append("D")
    #         self.listPositionCubCurrent = self.updatePositionList(cubCurrent, colorOne, colorTwo, colorThree)


    def mvcanny2(self, cub, mv, col1,col2,col3,face):
        while not self.facolor(cub, face):
            cub.D()
            mv.append("D")
            self.mvcurent = corners(cub.cub,col1,col2,col3)
    #
    # def moveSide(self, cubCurrent, solveMoveList, colorOne, colorTwo, colorThree, face):
    #     mixManager = MixManager()
    #     while ((self.finishedThreeColorPosition(cubCurrent, colorOne, colorTwo, colorThree)) == False):
    #         if (face == "front"):
    #             mixManager.mixRun(["R'", "D'", "R", "D"], cubCurrent)
    #             appendListInList(solveMoveList, ["R'", "D'", "R", "D"])
    #         elif (face == "right"):
    #             mixManager.mixRun(["B'", "D'", "B", "D"], cubCurrent)
    #             appendListInList(solveMoveList, ["B'", "D'", "B", "D"])
    #         elif (face == "back"):
    #             mixManager.mixRun(["L'", "D'", "L", "D"], cubCurrent)
    #             appendListInList(solveMoveList, ["L'", "D'", "L", "D"])
    #         elif (face == "left"):
    #             mixManager.mixRun(["F'", "D'", "F", "D"], cubCurrent)
    #             appendListInList(solveMoveList, ["F'", "D'", "F", "D"])
    def mvfaces(self, cub, mv, col1, col2, col3,face):
        def appendix(list, cub, mv):
            for l in list:
                cub.rotate_by_name(l)
                mv.append(l)
        while not edges_corners_checker(self.origin.cub, cub.cub, col1,col2,col3):
            if face == 0:
                appendix(["R'", "D'", "R", "D"],cub,mv)
            elif face == 2:
                appendix(["B'", "D'", "B", "D"], cub,mv)
            elif face ==1:
                appendix(["L'", "D'", "L", "D"], cub, mv)
            elif face == 3:
                appendix(["F'", "D'", "F", "D"], cub,mv)