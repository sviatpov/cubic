from rubic import rubic
from stepone import stepone
from steptwo import steptwo

# faces = ['front', 'back', 'right', 'left', 'upper', 'down']
# numpy = [  0,        1,      2,       3  ,   4  ,       5]
#colors = ["green", "blue", "red", "orange", "white", "yellow"]

if __name__ == "__main__":
    r = rubic()
    # r.mix()
    # print(r.cub)
    # "F D' L D' R'"
    # r.L()
    r.rotate_by_name('F')
    r.rotate_by_name("D'")
    r.rotate_by_name("L")
    r.rotate_by_name("D'")
    r.rotate_by_name("R'")

    # r.rotate_by_name("U'")
    # r.rotate_by_name("R")
    # r.rotate_by_name("L'")
    # r.rotate_by_name("F'")
    s = stepone()
    s2 = steptwo()
    mv = []
    orig = s.solver(r, mv)
    print(mv)
    s2.solver(r,mv)

    print(mv)