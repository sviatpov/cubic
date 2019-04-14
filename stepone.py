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

    def solver(self, cub, mvmain):
        if not edges_corners_checker(self.origin.cub, cub.cub, 4, 0):
            self.rotate(cub, mvmain, 4, 0, 0)
        if not edges_corners_checker(self.origin.cub, cub.cub, 4, 1):
            self.rotate(cub, mvmain, 4, 1, 1)
        if not edges_corners_checker(self.origin.cub, cub.cub, 4, 2):
            self.rotate(cub, mvmain, 4, 2, 2)
        if not edges_corners_checker(self.origin.cub, cub.cub, 4, 3):
            self.rotate(cub, mvmain, 4, 3, 3)
        return self.origin

    def rotate(self, cub, mvmain, col1, col2, face):
        self.mvcurent = edges(cub.cub, col1, col2)
        self.mvorig = edges(self.origin.cub, col1, col2)
        if face != self.mvcurent[0] and face != self.mvcurent[3]:
            self.mvdown2(cub, mvmain, col1,col2, face)
        if face == self.mvcurent[0] or face == self.mvcurent[3]:
            self.mvcentr(cub, mvmain, col1, col2, face)
            if self.mvcurent[-2] != self.mvorig[-2]:
                self.swapside(cub, mvmain, face)

    def swapside(self, cub, mv, face):
        def appendix(list, cub, mv):
            for l in list:
                cub.rotate_by_name(l)
                mv.append(l)
        if face == 0:
            appendix(["F", "U'", "R", "U"], cub, mv)
        elif face ==2:
            appendix(["R", "U'", "B", "U"], cub, mv)
        elif face == 3:
            appendix(["L", "U'", "F", "U"], cub, mv)
        elif face == 1:
            appendix(["B", "U'", "L", "U"], cub, mv)


    def mvcentr(self, cub, mv, col1, col2, face):
        fdic = {0:"F'", 2:"R'", 3:"L'",1:"B'"}
        while self.mvcurent[4] != self.mvorig[4]:
            val = fdic.get(face)
            if val != None:
                cub.rotate_by_name(val)
                mv.append(val)
            self.mvcurent = edges(cub.cub, col1, col2)


    def update_color(self, cub, col1, col2):
        self.mvcurent=edges(cub.cub, col1, col2)
        return self.mvcurent[0], self.mvcurent[3]

    def mvdown2(self, cub, mv, col1, col2, face):
        f1, f2 = self.update_color(cub, col1, col2)

        def mvdownc(cub, mv, col1, col2, face):
            f1,f2 = self.update_color(cub, col1, col2)
            while True:
                if f1 == face or f2 == face:
                    break
                cub.D()
                mv.append("D")
                f1, f2 = self.update_color(cub, col1, col2)
        def optimus(count, mv, el):
            if count == 3:
                count = 1
                mv.append(el + "'")
                return count, 1
            else:
                for i in range(count):
                    mv.append(el)
                return count, 0

        def ifrotate(f1,f2, f,cub, mv, col1, col2, face, letera):
            count = 0
            while True:
                if f1==f or f2==f:
                    break
                count += 1
                cub.rotate_by_name(letera)
                f1, f2 = self.update_color(cub, col1, col2)
            count, flag = optimus(count, mv, letera)
            mvdownc(cub, mv, col1, col2, face)
            for _ in range(count, 0, -1):
                if flag ==0:
                    cub.rotate_by_name(letera + "'")
                    mv.append(letera + "'")
                else:
                    cub.rotate_by_name(letera)
                    mv.append(letera)

        if f1==0 or f2==0:
            ifrotate(f1,f2,5,cub, mv, col1, col2, face, "F")
        elif f1 == 3 or f2 == 3:
            ifrotate(f1,f2,5,cub, mv, col1, col2, face, "L")
        elif f1 ==2 or f2 ==2:
            ifrotate(f1,f2,5,cub,mv,col1,col2,face,"R")
        elif f1 == 1 or f2 == 1:
            ifrotate(f1,f2,5,cub,mv,col1,col2,face,"B")
