from rubic import rubic
from stepone import stepone


if __name__ == "__main__":
    r = rubic()
    # r.mix()
    # print(r.cub)
    r.rotate_by_name('F')
    r.rotate_by_name("D'")
    r.rotate_by_name("L")
    r.rotate_by_name("D'")
    r.rotate_by_name("R'")
    s = stepone()
    mv = []
    s.solver(r, mv)

    print(mv)