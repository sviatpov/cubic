from rubic import rubic
import numpy as np
# faces = ['front', 'back', 'right', 'left', 'upper', 'down']
# numpy = [  0,        1,      2,       3  ,   4  ,       5]
#colors = ["green", "blue", "red", "orange", "white", "yellow"]
def edges(rubic, val1, val2):
    def edge(rubic, col1, col2):
        if   rubic[4][0][1] == col1 and rubic[1][0][1] == col2:
            # return ([['upper', col1, 0, 1], ['back', col2, 0, 1]])
            return 0
        elif rubic[4][1][2] == col1 and rubic[2][0][1] == col2:
            return 1

        elif rubic[4][2][1] == col1 and rubic[0][0][1] == col2:
            return 2

        elif rubic[4][1][0] == col1 and rubic[3][0][1] == col2:
            return 3

        elif rubic[3][1][2] == col1 and rubic[0][1][0] == col2:
            return 4

        elif rubic[3][1][0] == col1 and rubic[1][1][2] == col2:
            return 5

        elif rubic[0][1][2] == col1 and rubic[2][1][0] == col2:
            return 6

        elif rubic[2][1][2] == col1 and rubic[1][1][0] == col2:
            return 7

        elif rubic[5][0][1] == col1 and rubic[0][2][1] == col2:
            return 8

        elif rubic[5][1][2] == col1 and rubic[2][2][1] == col2:
            return 9

        elif rubic[5][2][1] == col1 and rubic[1][2][1] == col2:
            return 10

        elif rubic[5][1][0] == col1 and rubic[3][2][1] == col2:
            return 11
        return 100 #infinity
    # pairs on edges  [Face, point, Face, Point]
    pairs = [[4,0,1, 1, 0,1], [4,1,2, 2,0,1], [4,2,1, 0,0,1], [4,1,0, 3, 0,1],
             [3,1,2, 0, 1,0], [3,1,0, 1,1,2], [0,1,2, 2,1,0], [2,1,2, 1, 1,0],
             [5,0,1, 0, 2,1], [5,1,2, 2,2,1], [5,2,1, 1,2,1], [5,1,0, 3, 2,1]]
    f1 = (edge(rubic, val1, val2), val1, val2)
    f2 = (edge(rubic, val2, val1), val2, val1)
    f = min((f1, f2), key=lambda x:x[0])
    if f[0] >= len(pairs):
        return False
    return np.concatenate((pairs[f[0]], [f[1]], [f[2]]))

def corners(rubic, val1, val2, val3):
    # [Face, poin, Face, Point, Face, Point]
    pairthree = [[4,0,0, 3, 0,0, 1, 0,2],
                 [4,0,2, 2, 0,2, 1, 0,0],
                 [4,2,2, 2, 0,0, 0, 0,2],
                 [4,2,0, 3, 0,2, 0, 0,0],
                 [5,0,0, 3, 2,2, 0, 2,0],
                 [5,0,2, 2, 2,0, 0, 2,2],
                 [5,2,2, 2, 2,2, 1, 2,0],
                 [5,2,0, 3, 2,0, 1, 2,2]]

    def corner(rubic, col1, col2, col3):
        if (rubic[4][0][0] == col1 and rubic[3][0][0] == col2 and rubic[1][0][2] == col3):
            return 0
    #2
        elif (rubic[4][0][2] == col1 and rubic[2][0][2] == col2 and rubic[1][0][0] == col3):
            return 1
    #3
        elif (rubic[4][2][2] == col1 and rubic[2][0][0] == col2 and rubic[0][0][2] == col3):
            return 2
    #4
        elif (rubic[4][2][0] == col1 and rubic[3][0][2] == col2 and rubic[0][0][0] == col3):
            return 3
    #5
        elif (rubic[5][0][0] == col1 and rubic[3][2][2] == col2 and rubic[0][2][0] == col3):
            return 4
    #6
        elif (rubic[5][0][2] == col1 and rubic[2][2][0] == col2 and rubic[0][2][2] == col3):
            return 5
    #7
        elif (rubic[5][2][2] == col1 and rubic[2][2][2] == col2 and rubic[1][2][0] == col3):
            return 6
    #8
        elif (rubic[5][2][0] == col1 and rubic[3][2][0] == col2 and rubic[1][2][2] == col3):
            return 7
        return 100
    f1=(corner(rubic, val1, val2, val3), val1, val2, val3)
    f2=(corner(rubic, val1, val3, val2), val1, val3, val2)
    f3=(corner(rubic, val2, val3, val1), val2, val3, val1)
    f4=(corner(rubic, val2, val1, val3), val2, val1, val3)
    f5=(corner(rubic, val3, val1, val2), val3, val1, val2)
    f6=(corner(rubic, val3, val2, val1), val3, val2, val1)
    f = min((f1,f2,f3,f4,f5,f6), key=lambda x:x[0])
    if f[0] >= len(pairthree):
        return False
    return np.concatenate((pairthree[f[0]], [f[1]], [f[2]], [f[3]]))
def edges_corners_checker(rubO, rubC, col1, col2, col3=None):
    if isinstance(col3, int):
        l1, l2 = corners(rubO, col1, col2, col3), corners(rubC, col1, col2, col3)
        return np.all(l1==l2)
    else:
        l1, l2 = edges(rubO, col1, col2), edges(rubC, col1, col2)
        return np.all(l1==l2)
#
if __name__ == '__main__':

    r = rubic()
    r.mix(100)
    a = edges(r.cub, 2, 1)
    print(a)
    print()