import numpy as np

# faces = ['front', 'back', 'right', 'left', 'upper', 'down']
# numpy = [  0,        1,      2,       3  ,   4  ,       5]
#colors = ["green", "blue", "red", "orange", "white", "yellow"]

# see https://docs.scipy.org/doc/numpy-1.13.0/reference/arrays.indexing.html
class rubic():
    def __init__(self, size=3):

        self.cub = np.zeros((6,size,size), dtype='uint8')
        self.size = size
        for i, c in enumerate(self.cub):
            c += i

        self.slice = np.array([i for i in range(self.size)])
        self.zero = np.zeros(self.size, dtype='uint8')
        self.last = np.ones(self.size, dtype='uint8') * (-1)
        # print(self.cub)

        self.fb = [self._face_([2,5,3,4]),
                   np.concatenate((self.slice, self.zero, self.slice, self.last)),
                   np.concatenate((self.zero, self.slice, self.last, self.slice))]
        self.fa = [self._face_([4,2,5,3]),
                   np.concatenate((self.last, self.slice, self.zero, self.slice)),
                   np.concatenate((self.slice, self.zero, self.slice, self.last))]

        self.rb = [self._face_([1,5,0,4]),
                   np.concatenate((self.slice, self.slice, self.slice, self.slice)),
                   np.concatenate((self.zero, self.last, self.last, self.last))]
        self.ra = [self._face_([4,1,5,0]),
                   np.concatenate((self.slice, self.slice, self.slice, self.slice)),
                   np.concatenate((self.last, self.zero, self.last, self.last))]

        self.lb = [self._face_([0,5,1,4]),
                   np.concatenate((self.slice, self.slice, self.slice, self.slice)),
                   np.concatenate((self.zero, self.zero, self.last, self.zero))]
        self.la = [self._face_([4,0,5,1]),
                   np.concatenate((self.slice, self.slice, self.slice, self.slice)),
                   np.concatenate((self.zero, self.zero, self.zero, self.last))]

        self.bb = [self._face_([3,5,2,4]),
                    np.concatenate((self.slice, self.last, self.slice, self.zero)),
                    np.concatenate((self.zero, self.slice, self.last, self.slice))]
        self.ba = [self._face_([4,3,5,2]),
                   np.concatenate((self.zero, self.slice, self.last, self.slice )),
                   np.concatenate((self.slice,self.zero, self.slice, self.last))]

        self.ub = [self._face_([2,0,3,1]),
                   np.concatenate((self.zero, self.zero, self.zero, self.zero)),
                   np.concatenate((self.slice, self.slice, self.slice, self.slice))]
        self.ua = [self._face_([1, 2, 0, 3]),
                   np.concatenate((self.zero, self.zero, self.zero, self.zero)),
                   np.concatenate((self.slice, self.slice, self.slice, self.slice))]

        self.db = [self._face_([2,1,3,0]),
                   np.concatenate((self.last, self.last, self.last, self.last)),
                   np.concatenate((self.slice, self.slice, self.slice, self.slice))]
        self.da = [self._face_([0, 2,1,3]),
                   np.concatenate((self.last, self.last, self.last, self.last)),
                   np.concatenate((self.slice, self.slice, self.slice, self.slice))]

    def _face_(self, fc):
        bef = np.concatenate((np.ones(self.size, dtype='uint8')*fc[0],
                              np.ones(self.size, dtype='uint8')*fc[1],
                              np.ones(self.size, dtype='uint8')*fc[2],
                              np.ones(self.size, dtype='uint8')*fc[3]))
        return bef


    def _rot90(self,front,b,a, is_clock=True):
        if is_clock:
            self.cub[front] = np.rot90(self.cub[front], k=3)
            self.cub[tuple(b)] = self.cub[tuple(a)]
        else:
            self.cub[front] = np.rot90(self.cub[front], k=1)
            self.cub[tuple(a)] = self.cub[tuple(b)]

    def F(self):
        self._rot90(0, self.fb, self.fa)
    def Fs(self):
        self._rot90(0, self.fb, self.fa, False)
    def B(self):
        self._rot90(1, self.bb, self.ba)
    def Bs(self):
        self._rot90(1, self.bb, self.ba, False)
    def R(self):
        self._rot90(2, self.rb, self.ra)
    def Rs(self):
        self._rot90(2, self.rb, self.ra, False)
    def L(self):
        self._rot90(3, self.lb, self.la)
    def Ls(self):
        self._rot90(3, self.lb, self.la, False)
    def U(self):
        self._rot90(4, self.ub, self.ua)
    def Us(self):
        self._rot90(4, self.ub, self.ua, False)
    def D(self):
        self._rot90(5, self.db, self.da)
    def Ds(self):
        self._rot90(5, self.db, self.da, False)
    def F2(self):
        self.F()
        self.F()
    def B2(self):
        self.B()
        self.B()
    def R2(self):
        self.R()
        self.R()
    def L2(self):
        self.L()
        self.L()
    def U2(self):
        self.U()
        self.U()
    def D2(self):
        self.D()
        self.D()
    def mix(self, iter=100):
        comands = [self.F, self.D, self.B, self.R, self.L, self.U,
                   self.F2, self.D2, self.B2, self.R2, self.L2, self.U2,
                   self.Fs, self.Ds, self.Bs, self.Rs,self.Ls, self.Us]
        for i in range(iter):
            comands[np.random.randint(0, len(comands))]()

    def rotate_by_name(self, name):
        comands = {"F":self.F, "D":self.D,     "B":self.B,  "R":self.R,    "L":self.L, "U":self.U,
                   "F2":self.F2, "D2":self.D2, "B2":self.B2, "R2":self.R2, "L2":self.L2, "U2":self.U2,
                   "F'":self.Fs, "D'":self.Ds, "B'":self.Bs, "R'":self.Rs, "L'":self.Ls, "U'":self.Us}
        f = comands.get(name)
        if f != None:
            f()

    def reset(self):
        self.cub = np.zeros((6, self.size, self.size), dtype='uint8')
        self.size = self.size
        for i, c in enumerate(self.cub):
            c += i





if __name__ == "__main__":
    r = rubic()
    # r.mix()
    # print(r.cub)
    r.rotate_by_name('F')
    print(r.cub)
    # x = np.array([[0, 1, 2],[3, 4, 5],[6, 7, 8],[9, 10, 11]])
    # rows = np.array([[0, 0],[3, 3]], dtype=np.intp)
    # columns = np.array([[0, 2],[0, 2]], dtype=np.intp)
    # print(x)
    # print(x[rows, columns])
    # rows = np.array([0, 3], dtype=np.intp)
    # columns = np.array([0, 2], dtype=np.intp)
    # print(x[rows[:, np.newaxis], columns])