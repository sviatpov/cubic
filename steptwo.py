
from rubic import rubic
from edges_corners_checker import edges_corners_checker, corners

# faces = ['front', 'back', 'right', 'left', 'upper', 'down']
# numpy = [  0,        1,      2,       3  ,   4  ,       5]
#colors = ["green", "blue", "red", "orange", "white", "yellow"]

class steptwo():

    def __init__(self):
        self.origin = rubic()
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

#### Mby trabls
    def face2color(self,fc, side):
        c=0
        if len(self.mvcurent) > 0:
            for i in range(0,3):
                if self.mvcurent[i*3]==fc or self.mvcurent[i*3]==side:
                    c+=1
        return c==2


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


    def mvcanny2(self, cub, mv, col1,col2,col3,face):
        while not self.facolor(cub, face):
            cub.D()
            mv.append("D")
            self.mvcurent = corners(cub.cub,col1,col2,col3)
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