from rubic import rubic
from edges_corners_checker import edges_corners_checker, edges




class stepfive():
    def __init__(self):

        self.origin = rubic()
        self.mvcurent = []
        self.mvorig = []
        self.pattern1=["L", "D", "L'", "D", "L", "D2", "L'", "D"]
        self.pattern4 = ["B", "D", "B'", "D", "B", "D2", "B'", "D"]
        self.pattern3 = ["F", "D", "F'", "D", "F", "D2", "F'", "D"]
        self.pattern2=["R", "D", "R'", "D", "R", "D2", "R'", "D"]


    def solver(self, cub, mv):
        r = self.mv2d(cub, mv)
        if r == 2:
            self.mv2f(cub, mv)


    def mv2f(self, cub, mv):
        r=2
        if edges_corners_checker(self.origin.cub, cub.cub, 5, 0):
            if edges_corners_checker(self.origin.cub, cub.cub, 5, 1):
                r = self.moveanotherside(cub, mv, 2)
        if edges_corners_checker(self.origin.cub, cub.cub, 5, 2):
            if edges_corners_checker(self.origin.cub, cub.cub, 5, 3):
                r = self.moveanotherside(cub, mv, 0)
        if r ==2:
            sd = -1
            green=edges_corners_checker(self.origin.cub, cub.cub,5,0)
            blue=edges_corners_checker(self.origin.cub, cub.cub, 5, 1)
            red = edges_corners_checker(self.origin.cub, cub.cub, 5, 2)
            orange = edges_corners_checker(self.origin.cub, cub.cub, 5, 3)
            if blue and orange:
                sd = 0
            elif green and orange:
                sd = 2
            elif green and red:
                sd = 1
            elif red and blue:
                sd = 3
            self.rotatecorner(cub, mv,sd)

    def rotatecorner(self, cub, mv,sd):
        def appendix(list, cub, mv):
            for l in list:
                cub.rotate_by_name(l)
                mv.append(l)
        if sd == 0:
            appendix(self.pattern1, cub, mv)

        if sd == 1:
            appendix(self.pattern2, cub, mv)

        if sd == 2:
            appendix(self.pattern3, cub, mv)

        if sd == 3:
            appendix(self.pattern4, cub, mv)



    def  moveanotherside(self, cub, mv, side):
        def appendix(list, cub, mv):
            for l in list:
                cub.rotate_by_name(l)
                mv.append(l)
        if side == 0:
            appendix(["L", "D", "L'", "D", "L", "D2", "L'"], cub, mv)
        if side == 2:
            appendix(["F", "D", "F'", "D", "F", "D2", "F'"], cub, mv)
        r = self.mv2d(cub, mv)
        return r

    def mv2d(self, cub, mv):
        c = 0

        while c < 2:
            if edges_corners_checker(self.origin.cub, cub.cub,5,0):
                c+=1
            if edges_corners_checker(self.origin.cub, cub.cub, 5, 1):
                c += 1
            if edges_corners_checker(self.origin.cub, cub.cub, 5, 2):
                c += 1
            if edges_corners_checker(self.origin.cub, cub.cub, 5, 3):
                c += 1
            if c==4:
                return 'OK'
            if c<2:
                c=0
                cub.D()
                mv.append("D")
        return 2

