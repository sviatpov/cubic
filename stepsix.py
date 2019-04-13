from rubic import rubic
from edges_corners_checker import edges_corners_checker, edges, corners


class stepsix():
    def __init__(self):

        self.origin = rubic()
        self.mvcurent = []
        self.mvorig = []


    def solver(self, cub, mv):
        c=0
        if edges_corners_checker(self.origin.cub, cub, 5, 0, 2):
            c+=1
        if edges_corners_checker(self.origin.cub, cub, 5, 1, 3):
            c += 1
        if edges_corners_checker(self.origin.cub, cub, 5, 2, 1):
            c += 1
        if edges_corners_checker(self.origin.cub, cub, 5, 3, 0):
            c += 1
        if c == 4:
            return
        c = 0
        isrightcorner=[]

        self.mvcurent= corners(cub, 5, 0, 2)
        if self.facolor(cub, 0):
            c+=1
            # isrightcorner.append(5)
            # isrightcorner.append(0)
            # isrightcorner.append(2)
        self.mvcurent=corners(cub, 5, 1, 2)
        if self.facolor(cub, 2):
            c+=1
            # isrightcorner.append(5)
            # isrightcorner.append(1)
            # isrightcorner.append(2)
        self.mvcurent = corners(cub, 5, 1, 3)
        if self.facolor(cub, 1):
            c+=1
            # isrightcorner.append(5)
            # isrightcorner.append(1)
            # isrightcorner.append(3)
        self.mvcurent = corners(cub, 5, 0, 3)
        if self.facolor(cub, 3):
            c+=1
            # isrightcorner.append(5)
            # isrightcorner.append(0)
            # isrightcorner.append(3)
        if c == 4:
            return
        if c == 0:
            self.appendix(["D", "L", "D'", "R'", "D", "L'", "D'", "R"],cub, mv)

        c = 0
        isrightcorner = []

        self.mvcurent = corners(cub, 5, 0, 2)
        if self.facolor(cub, 0):
            c += 1
            isrightcorner.append(5)
            isrightcorner.append(0)
            isrightcorner.append(2)
        self.mvcurent = corners(cub, 5, 1, 2)
        if self.facolor(cub, 2):
            c += 1
            isrightcorner.append(5)
            isrightcorner.append(1)
            isrightcorner.append(2)
        self.mvcurent = corners(cub, 5, 1, 3)
        if self.facolor(cub, 1):
            c += 1
            isrightcorner.append(5)
            isrightcorner.append(1)
            isrightcorner.append(3)
        self.mvcurent = corners(cub, 5, 0, 3)
        if self.facolor(cub, 3):
            c += 1
            isrightcorner.append(5)
            isrightcorner.append(0)
            isrightcorner.append(3)


    def appendix(self, list, cub, mv):
        for l in list:
            cub.rotate_by_name(l)
            mv.append(l)
    def face2color(self,fc, side):
        c=0
        if len(self.mvcurent) > 0:
            for i in range(0,3):
                if self.mvcurent[i*3]==fc or self.mvcurent[i*3]==side:
                    c+=1
        return c==2

    def facolor(self, cub, face):
        ff = {0: 2, 2: 1, 1: 3, 3: 0}
        ff = ff.get(face)
        if ff != None:
            return self.face2color(face, ff)
        return False