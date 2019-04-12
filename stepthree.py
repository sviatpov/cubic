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

        if chlist[0]:
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
                self.mv2cent(cub, mv, col1,col2,face)
                self.mvcurent = edges(cub.cub, col1, col2)
                self.mv2try(cub, mv, col1,col2)

    def chside(self, cub, col1, col2):
        pass
    def mv2try(self, cub, mv, col1, col2):
        pass