from rubic import rubic
from edges_corners_checker import edges_corners_checker, edges, corners
import numpy as np
class stepseven():
    def __init__(self):

        self.origin = rubic()
        self.mvcurent = []
        self.mvorig = []


    def solver(self, cub, mv):
        if np.all(self.origin.cub == cub.cub):
            return
        self.rotateside(cub, mv,5, 0, 3)
        cub.D()
        mv.append('D')
        self.rotateside(cub, mv, 5, 1, 3)
        cub.D()
        mv.append('D')
        self.rotateside(cub, mv, 5, 1, 2)
        cub.D()
        mv.append('D')
        self.rotateside(cub, mv, 5, 2, 0)
        cub.D()
        mv.append('D')

    def appendix(self, list, cub, mv):
        for l in list:
            cub.rotate_by_name(l)
            mv.append(l)

    def rotateside(self, cub, mv, col1,col2, col3):
        while True:
            pos = corners(cub.cub, col1, col2, col3)
            if pos[0]==5 and pos[-3]==5:
                break
            self.appendix(["L'", "U'", "L", "U"], cub, mv)