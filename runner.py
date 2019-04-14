from rubic import rubic
from stepone import stepone
from steptwo import steptwo
from stepthree import stepthree
from stepFor import stepfore
from stepfive import stepfive
from stepsix import stepsix
from stepseven import stepseven
from argpareser import parse_line
from cube_interactive import main_gui
# faces = ['front', 'back', 'right', 'left', 'upper', 'down']
# numpy = [  0,        1,      2,       3  ,   4  ,       5]
#colors = ["green", "blue", "red", "orange", "white", "yellow"]


def print_mv(mm):
    for m in mm:
        print(m)

if __name__ == "__main__":
    step, gui = parse_line()
    if gui:
        main_gui(step)
    else:
        s1 = stepone()
        s2 = steptwo()
        s3 = stepthree()
        s4 = stepfore()
        s5 = stepfive()
        s6 = stepsix()
        s7 = stepseven()
        r = rubic()
        if isinstance(step, list):
            for s in step:
                r.rotate_by_name(s)
        else:
            r.mix(int(step))
        mv = []
        orig = s1.solver(r, mv)
        # print(mv)
        s2.solver(r,mv)
        # print(mv)
        # mvv = []
        s3.solver(r, mv)
        # print(mv)
        s4.solver(r, mv)
        # print(mv)
        s5.solver(r, mv)
        # print(mv)
        s6.solver(r, mv)
        # print(mv)
        s7.solver(r, mv)
        # print(mv)
        # print(r.cub)
        print_mv(mv)
