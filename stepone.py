from rubic import rubic
from edges_corners_checker import edges_corners_checker, edges
import  numpy as np

# faces = ['front', 'back', 'right', 'left', 'upper', 'down']
# numpy = [  0,        1,      2,       3  ,   4  ,       5]
#colors = ["green", "blue", "red", "orange", "white", "yellow"]


class stepone():
    def __init__(self):
        self.origin = rubic()
        self.mvcurent = []
        self.mvorig = []

    # def edgeMoveTwoColor(self, cubCurrent, solveMoveList, colorOne, colorTwo, face):
    #     self.listPositionCubCurrent = self.checkerManager.two(cubCurrent, colorOne, colorTwo)
    #     self.listPositionCubOrigin = self.checkerManager.two(self.cubOrigin, colorOne, colorTwo)
    #
    #     if (face != self.listPositionCubCurrent[0][0] and face != self.listPositionCubCurrent[1][0]):
    #         self.moveDownTwoColor(cubCurrent, solveMoveList, colorOne, colorTwo, face)
    #
    #     if (face == self.listPositionCubCurrent[0][0] or face == self.listPositionCubCurrent[1][0]):
    #         self.moveCenter(cubCurrent, solveMoveList, face, colorOne, colorTwo)
    #         if (self.listPositionCubCurrent[0][1] != self.listPositionCubOrigin[0][1]):
    #             self.changeSide(cubCurrent, solveMoveList, face)

    def solver(self, cub, mvmain):
        if edges_corners_checker(self.origin, cub, 4, 0):
            self.rotate(cub, mvmain, 4, 0, 0)
        if edges_corners_checker(self.origin, cub, 4, 1):
            self.rotate(cub, mvmain, 4, 1, 1)
        if edges_corners_checker(self.origin, cub, 4, 2):
            self.rotate(cub, mvmain, 4, 2, 2)
        if edges_corners_checker(self.origin, cub, 4, 3):
            self.rotate(cub, mvmain, 4, 3, 3)

    def rotate(self, cub, mvmain, col1, col2, face):
        self.mvcurent = edges(cub, col1, col2)
        self.mvorig = edges(self.origin, col1, col2)
        if face != self.mvcurent[0] and face != self.mvcurent[3]:
            self.mvdown2()
        if face == self.mvcurent[0] or face == self.mvcurent[3]:
            self.mvcentr(cub, mvmain, col1, col2, face)
            if self.mvcurent[0] != self.mvorig[0]:
                self.swapside()

    def swapside(self):
        pass


    def mvcentr(self, cub, mv, col1, col2, face):
        fdic = {0:"F'", 2:"R'", 3:"L'",1:"B'"}
        while self.mvcurent[4] != self.mvorig[4]:
            val = fdic.get(face)
            if val != None:
                cub.rotate_by_name(val)
                mv.append(val)
            self.mvcurent = edges(cub, col1, col2)

        pass

    def update_color(self):
        pass

    def mvdown2(self):
        pass
    # def moveDownTwoColor(self, cubCurrent, solveMoveList, colorOne, colorTwo, face):
    #     faceOne, faceTwo = self.updateFaceColor(cubCurrent, colorOne, colorTwo)
    #
    #     def moveDownCenter(cubCurrent, solveMoveList, colorOne, colorTwo, face):
    #         faceOne, faceTwo = self.updateFaceColor(cubCurrent, colorOne, colorTwo)
    #         while (1):
    #             if (faceOne == face or faceTwo == face):
    #                 break
    #             cubCurrent.moveD()
    #             solveMoveList.append("D")
    #             faceOne, faceTwo = self.updateFaceColor(cubCurrent, colorOne, colorTwo)
    #
    #     def optimizationStep(count, solveMoveList, move):
    #         if (count == 3):
    #             count = 1
    #             solveMoveList.append(move + "'")
    #             return count, 1
    #         else:
    #             x = 0
    #             while (x != count):
    #                 x += 1
    #                 solveMoveList.append(move)
    #         return count, 0
    #
    #     count = 0
    #     if (faceOne == "front" or faceTwo == "front"):
    #         while (1):
    #             if (faceOne == "down" or faceTwo == "down"):
    #                 break
    #             count += 1
    #             cubCurrent.moveF()
    #             faceOne, faceTwo = self.updateFaceColor(cubCurrent, colorOne, colorTwo)
    #         count, flag = optimizationStep(count, solveMoveList, "F")
    #         moveDownCenter(cubCurrent, solveMoveList, colorOne, colorTwo, face)
    #         while (count != 0):
    #             count -= 1
    #             if (flag == 0):
    #                 cubCurrent.moveBackF()
    #                 solveMoveList.append("F'")
    #             else:
    #                 cubCurrent.moveF()
    #                 solveMoveList.append("F")
    #     elif (faceOne == "left" or faceTwo == "left"):
    #         while (1):
    #             if (faceOne == "down" or faceTwo == "down"):
    #                 break
    #             count += 1
    #             cubCurrent.moveL()
    #             faceOne, faceTwo = self.updateFaceColor(cubCurrent, colorOne, colorTwo)
    #         count, flag = optimizationStep(count, solveMoveList, "L")
    #         moveDownCenter(cubCurrent, solveMoveList, colorOne, colorTwo, face)
    #         while (count != 0):
    #             count -= 1
    #             if (flag == 0):
    #                 cubCurrent.moveBackL()
    #                 solveMoveList.append("L'")
    #             else:
    #                 cubCurrent.moveL()
    #                 solveMoveList.append("L")
    #
    #     elif (faceOne == "right" or faceTwo == "right"):
    #         while (1):
    #             if (faceOne == "down" or faceTwo == "down"):
    #                 break
    #             count += 1
    #             cubCurrent.moveR()
    #             faceOne, faceTwo = self.updateFaceColor(cubCurrent, colorOne, colorTwo)
    #         count, flag = optimizationStep(count, solveMoveList, "R")
    #         moveDownCenter(cubCurrent, solveMoveList, colorOne, colorTwo, face)
    #         while (count != 0):
    #             count -= 1
    #             if (flag == 0):
    #                 cubCurrent.moveBackR()
    #                 solveMoveList.append("R'")
    #             else:
    #                 cubCurrent.moveR()
    #                 solveMoveList.append("R")
    #
    #     elif (faceOne == "back" or faceTwo == "back"):
    #         while (1):
    #             if (faceOne == "down" or faceTwo == "down"):
    #                 break
    #             count += 1
    #             cubCurrent.moveB()
    #             faceOne, faceTwo = self.updateFaceColor(cubCurrent, colorOne, colorTwo)
    #         count, flag = optimizationStep(count, solveMoveList, "B")
    #         moveDownCenter(cubCurrent, solveMoveList, colorOne, colorTwo, face)
    #         while (count != 0):
    #             count -= 1
    #             if (flag == 0):
    #                 cubCurrent.moveBackB()
    #                 solveMoveList.append("B'")
    #             else:
    #                 cubCurrent.moveB()
    #                 solveMoveList.append("B")
