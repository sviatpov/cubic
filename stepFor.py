from rubic import rubic
from edges_corners_checker import edges_corners_checker, edges


# def checkBackState(cubFace, color):
#
#     if cubFace[0][1] == color and cubFace[1][1] == color and cubFace[1][2] == color and cubFace[1][0] == color and cubFace[2][1] == color:
# 		return (4, 0)
# 	elif cubFace[1][0] == color and cubFace[1][1] == color and cubFace[1][2] == color:
# 		return (3, 0)
# 	elif cubFace[0][1] == color and cubFace[1][1] == color and cubFace[2][1] == color:
# 		return (3, 1)
# 	elif cubFace[2][1] == color and cubFace[1][1] == color and cubFace[1][2] == color:
# 		return (2, 0)
# 	elif cubFace[1][0] == color and cubFace[1][1] == color and cubFace[2][1] == color:
# 		return (2, 1)
# 	elif cubFace[0][1] == color and cubFace[1][1] == color and cubFace[1][0] == color:
# 		return (2, 2)
# 	elif cubFace[0][1] == color and cubFace[1][1] == color and cubFace[1][2] == color:
# 		return (2, 3)
# 	elif cubFace[1][1] == color:
# 		return (1, 0)
# 	return False, False


# faces = ['front', 'back', 'right', 'left', 'upper', 'down']
# numpy = [  0,        1,      2,       3  ,   4  ,       5]
#colors = ["green", "blue", "red", "orange", "white", "yellow"]
def backcolor(arr, col):
    if arr[0][1] == col and arr[1][1] == col and arr[1][2] == col and arr[1][0] == col and \
            arr[2][1] == col:
        return 0, 4
    elif arr[1][0] == col and arr[1][1] == col and arr[1][2] == col:
        return 0, 3
    elif arr[0][1] == col and arr[1][1] == col and arr[2][1] == col:
        return 1, 3
    elif arr[2][1] == col and arr[1][1] == col and arr[1][2] == col:
        return 0, 2
    elif arr[1][0] == col and arr[1][1] == col and arr[2][1] == col:
        return 1,2
    elif arr[0][1] == col and arr[1][1] == col and arr[1][0] == col:
        return 2,2
    elif arr[0][1] == col and arr[1][1] == col and arr[1][2] == col:
        return 3,2
    elif arr[1][1] == col:
        return 0, 1
    return None, None

class stepfore():
    def solver(self, cub, mv):
        def appendix(list, cub, mv):
            for l in list:
                cub.rotate_by_name(l)
                mv.append(l)
        c1, c2 = backcolor(cub.cub[5], 5)
        if c2 == 4:
            return
        if c2 == 1:
            appendix(["F", "L", "D", "L'", "D'", "F'"], cub, mv)

        c1, c2 = backcolor(cub.cub[5], 5)

        if c1 == 0 and c2 == 2:
            appendix(["F", "L", "D", "L'", "D'", "F'"], cub, mv)
        elif c1 == 1 and c2 == 2:
            appendix(["D'", "F", "L", "D", "L'", "D'", "F'"], cub, mv)
        elif c1 == 2 and c2 == 2:
            appendix(["D'", "D'", "F", "L", "D", "L'", "D'", "F'"], cub, mv)
        elif c1 == 3 and c2 == 2:
            appendix(["D", "F", "L", "D", "L'", "D'", "F'"], cub, mv)

        c1, c2 = backcolor(cub.cub[5], 5)
        if c2 == 3 and c1 ==0:
            appendix(["F", "L", "D", "L'", "D'", "F'"], cub, mv)
        elif c2 == 3 and c1 == 1:
            appendix(["D", "F", "L", "D", "L'", "D'", "F'"], cub, mv)