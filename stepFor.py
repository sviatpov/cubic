from rubic import rubic
from edges_corners_checker import edges_corners_checker, edges



# faces = ['front', 'back', 'right', 'left', 'upper', 'down']
# numpy = [  0,        1,      2,       3  ,   4  ,       5]
#colors = ["green", "blue", "red", "orange", "white", "yellow"]
def backcolor(arr, col):
    if          arr[0][1] == col \
            and arr[1][1] == col \
            and arr[1][2] == col \
            and arr[1][0] == col and \
            arr[2][1] == col:
        return 0, 4
    elif        arr[1][0] == col \
            and arr[1][1] == col \
            and arr[1][2] == col:
        return 0, 3

    elif        arr[2][1] == col \
            and arr[1][1] == col \
            and arr[1][2] == col:
        return 0, 2
    elif        arr[0][1] == col \
            and arr[1][1] == col \
            and arr[1][2] == col:
        return 3, 2
    elif        arr[1][0] == col \
            and arr[1][1] == col \
            and arr[2][1] == col:
        return 1,2
    elif        arr[0][1] == col \
            and arr[1][1] == col \
            and arr[2][1] == col:
        return 1, 3
    elif        arr[0][1] == col \
            and arr[1][1] == col \
            and arr[1][0] == col:
        return 2,2

    elif arr[1][1] == col:
        return 0, 1
    return None, None

class stepfore():
    def __init__(self):
        self.origin = rubic()
        self.mvcurent = []
        self.mvorig = []
        self.pattern1=["F", "L", "D", "L'", "D'", "F'"]
        self.pattern2=["F", "L", "D", "L'", "D'", "F'"]
        self.pattern3=["D'", "F", "L", "D", "L'", "D'", "F'"]
        self.pattern4=["D'", "D'", "F", "L", "D", "L'", "D'", "F'"]
        self.pattern5=["D", "F", "L", "D", "L'", "D'", "F'"]
        self.pattern6=["F", "L", "D", "L'", "D'", "F'"]
        self.pattern7=["D", "F", "L", "D", "L'", "D'", "F'"]
    def solver(self, cub, mv):
        def appendix(list, cub, mv):
            for l in list:
                cub.rotate_by_name(l)
                mv.append(l)
        c1, c2 = backcolor(cub.cub[5], 5)
        if c2 == 4:
            return
        if c2 == 1:
            appendix(self.pattern1, cub, mv)

        c1, c2 = backcolor(cub.cub[5], 5)

        if c1 == 0 and c2 == 2:
            appendix(self.pattern2, cub, mv)
        elif c1 == 1 and c2 == 2:
            appendix(self.pattern3, cub, mv)
        elif c1 == 2 and c2 == 2:
            appendix(self.pattern4, cub, mv)
        elif c1 == 3 and c2 == 2:
            appendix(self.pattern5, cub, mv)

        c1, c2 = backcolor(cub.cub[5], 5)
        if c2 == 3 and c1 ==0:
            appendix(self.pattern6, cub, mv)
        elif c2 == 3 and c1 == 1:
            appendix(self.pattern7, cub, mv)