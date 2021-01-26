import sys
import random

#            00 01 02      
#         B  03 04 05      
#            06 07 08     
#    L          U          R          D
# 10 11 12  20 21 22  30 31 32  40 41 42
# 13 14 15  23 24 25  33 34 35  43 44 45
# 16 17 18  26 27 28  36 37 38  46 47 48
#
#           50 51 52      
#         F 53 54 55      
#           56 57 58      





class cube:
    B = ( 0, 1, 2, 3, 4, 5, 6, 7, 8) 
    L = (10,11,12,13,14,15,16,17,18) 
    U = (20,21,22,23,24,25,26,27,28) 
    R = (30,31,32,33,34,35,36,37,38) 
    D = (40,41,42,43,44,45,46,47,48) 
    F = (50,51,52,53,54,55,56,57,58) 
    def __p(self,p):
        if 0 <= p <= 8:
            return 'B' + str(p)
        if 10 <= p <= 18:
            return 'L' + str(p-10)
        if 20 <= p <= 28:
            return 'U' + str(p-20)
        if 30 <= p <= 38:
            return 'R' + str(p-30)
        if 40 <= p <= 48:
            return 'D' + str(p-40)
        if 50 <= p <= 58:
            return 'F' + str(p-50)

    def __str__(self):
        p = self.__p
        s  = "          {} {} {}\n".format(p(self.B[0]),p(self.B[1]),p(self.B[2]),)
        s += "          {} {} {}\n".format(p(self.B[3]),p(self.B[4]),p(self.B[5]),)
        s += "          {} {} {}\n\n".format(p(self.B[6]),p(self.B[7]),p(self.B[8]),)

        s += "{} {} {}  {} {} {}  {} {} {}  {} {} {}\n".format(p(self.L[0]),p(self.L[1]),p(self.L[2]), p(self.U[0]),p(self.U[1]),p(self.U[2]), p(self.R[0]),p(self.R[1]),p(self.R[2]), p(self.D[0]),p(self.D[1]),p(self.D[2]),)
        s += "{} {} {}  {} {} {}  {} {} {}  {} {} {}\n".format(p(self.L[3]),p(self.L[4]),p(self.L[5]), p(self.U[3]),p(self.U[4]),p(self.U[5]), p(self.R[3]),p(self.R[4]),p(self.R[5]), p(self.D[3]),p(self.D[4]),p(self.D[5]),)
        s += "{} {} {}  {} {} {}  {} {} {}  {} {} {}\n\n".format(p(self.L[6]),p(self.L[7]),p(self.L[8]), p(self.U[6]),p(self.U[7]),p(self.U[8]), p(self.R[6]),p(self.R[7]),p(self.R[8]), p(self.D[6]),p(self.D[7]),p(self.D[8]),)
 
        s += "          {} {} {}\n".format(p(self.F[0]),p(self.F[1]),p(self.F[2]),)
        s += "          {} {} {}\n".format(p(self.F[3]),p(self.F[4]),p(self.F[5]),)
        s += "          {} {} {}\n\n".format(p(self.F[6]),p(self.F[7]),p(self.F[8]),)
        return s

    def to_array(self):
        return [self.B[0],self.B[1],self.B[2],self.B[3],self.B[4],self.B[5],self.B[6],self.B[7],self.B[8],
                self.L[0],self.L[1],self.L[2],self.L[3],self.L[4],self.L[5],self.L[6],self.L[7],self.L[8],
                self.U[0],self.U[1],self.U[2],self.U[3],self.U[4],self.U[5],self.U[6],self.U[7],self.U[8],
                self.R[0],self.R[1],self.R[2],self.R[3],self.R[4],self.R[5],self.R[6],self.R[7],self.R[8],
                self.D[0],self.D[1],self.D[2],self.D[3],self.D[4],self.D[5],self.D[6],self.D[7],self.D[8],
                self.F[0],self.F[1],self.F[2],self.F[3],self.F[4],self.F[5],self.F[6],self.F[7],self.F[8]]
    def from_array(self,a):
        self.B = (a[0],a[1],a[2],a[3],a[4],a[5],a[6],a[7],a[8],)
        self.L = (a[9],a[10],a[11],a[12],a[13],a[14],a[15],a[16],a[17],)
        self.U = (a[18],a[19],a[20],a[21],a[22],a[23],a[24],a[25],a[26],)
        self.R = (a[27],a[28],a[29],a[30],a[31],a[32],a[33],a[34],a[35],)
        self.D = (a[36],a[37],a[38],a[39],a[40],a[41],a[42],a[43],a[44],)
        self.F = (a[45],a[46],a[47],a[48],a[49],a[50],a[51],a[52],a[53],)
    def is_resolved(self):
        if self.B != ( 0, 1, 2, 3, 4, 5, 6, 7, 8):
            return False
        if self.L != (10,11,12,13,14,15,16,17,18): # Red
            return False
        if self.U != (20,21,22,23,24,25,26,27,28): # White
            return False
        if self.R != (30,31,32,33,34,35,36,37,38): # Orange
            return False
        if self.D != (40,41,42,43,44,45,46,47,48): # Yellow
            return False
        if self.F != (50,51,52,53,54,55,56,57,58): # Blue
            return False
        return True
    def diff(self):
        count = 0
        for a in self.B:
            if 0 <= a <= 8:
                count += 1
        for a in self.L:
            if 10 <= a <= 18:
                count += 1
        for a in self.U:
            if 20 <= a <= 28:
                count += 1
        for a in self.R:
            if 30 <= a <= 38:
                count += 1
        for a in self.D:
            if 40 <= a <= 48:
                count += 1
        for a in self.F:
            if 50 <= a <= 58:
                count += 1
        return 54-count # error counts
         
    def move_U(self):
        B = self.B[:]
        L = self.L[:]
        U = self.U[:]
        R = self.R[:]
        #D = self.D[:]
        F = self.F[:]

        self.B = (B[0],B[1],B[2],B[3],B[4],B[5],L[8],L[5],L[2],)
        self.U = (U[6],U[3],U[0],U[7],U[4],U[1],U[8],U[5],U[2],)
        self.L = (L[0],L[1],F[0],L[3],L[4],F[1],L[6],L[7],F[2],)
        self.R = (B[6],R[1],R[2],B[7],R[4],R[5],B[8],R[7],R[8],)
        #self.D = (D[0],D[1],D[2],D[3],D[4],D[5],D[6],D[7],D[8],)
        self.F = (R[6],R[3],R[0],F[3],F[4],F[5],F[6],F[7],F[8],)

    def move_R(self):
        B = self.B[:]
        #L = self.L[:]
        U = self.U[:]
        R = self.R[:]
        D = self.D[:]
        F = self.F[:]

        self.B = (B[0],B[1],U[2],B[3],B[4],U[5],B[6],B[7],U[8],)
        #self.L = (L[0],L[1],L[2],L[3],L[4],L[5],L[6],L[7],L[8],)
        self.U = (U[0],U[1],F[2],U[3],U[4],F[5],U[6],U[7],F[8],)
        self.R = (R[6],R[3],R[0],R[7],R[4],R[1],R[8],R[5],R[2],)
        self.D = (B[8],D[1],D[2],B[5],D[4],D[5],B[2],D[7],D[8],)
        self.F = (F[0],F[1],D[6],F[3],F[4],D[3],F[6],F[7],D[0],)

    def move_Uprime(self):
        B = self.B[:]
        L = self.L[:]
        U = self.U[:]
        R = self.R[:]
        #D = self.D[:]
        F = self.F[:]

        self.B = (B[0],B[1],B[2],B[3],B[4],B[5],R[0],R[3],R[6],)
        self.L = (L[0],L[1],B[8],L[3],L[4],B[7],L[6],L[7],B[6],)
        self.U = (U[2],U[5],U[8],U[1],U[4],U[7],U[0],U[3],U[6],)
        self.R = (F[2],R[1],R[2],F[1],R[4],R[5],F[0],R[7],R[8],)
        #self.D = (D[0],D[1],D[2],D[3],D[4],D[5],D[6],D[7],D[8],)
        self.F = (L[2],L[5],L[8],F[3],F[4],F[5],F[6],F[7],F[8],)

    def move_Rprime(self):
        B = self.B[:]
        #L = self.L[:]
        U = self.U[:]
        R = self.R[:]
        D = self.D[:]
        F = self.F[:]

        self.B = (B[0],B[1],D[6],B[3],B[4],D[3],B[6],B[7],D[0],)
        #self.L = (L[0],L[1],L[2],L[3],L[4],L[5],L[6],L[7],L[8],)
        self.U = (U[0],U[1],B[2],U[3],U[4],B[5],U[6],U[7],B[8],)
        self.R = (R[2],R[5],R[8],R[1],R[4],R[7],R[0],R[3],R[6],)
        self.D = (F[8],D[1],D[2],F[5],D[4],D[5],F[2],D[7],D[8],)
        self.F = (F[0],F[1],U[2],F[3],F[4],U[5],F[6],F[7],U[8],)

    def move_L(self):
        B = self.B[:]
        L = self.L[:]
        U = self.U[:]
        #R = self.R[:]
        D = self.D[:]
        F = self.F[:]

        self.B = (D[8],B[1],B[2], 
                  D[5],B[4],B[5], 
                  D[2],B[7],B[8],)
        self.L = (L[6],L[3],L[0], 
                  L[7],L[4],L[1], 
                  L[8],L[5],L[2],)
        self.U = (B[0],U[1],U[2], 
                  B[3],U[4],U[5], 
                  B[6],U[7],U[8],)
        #self.R = (R[0],R[1],R[2] ,R[3],R[4],R[5] ,R[6],R[7],R[8],)
        self.D = (D[0],D[1],F[6], 
                  D[3],D[4],F[3], 
                  D[6],D[7],F[0],)
        self.F = (U[0],F[1],F[2], 
                  U[3],F[4],F[5], 
                  U[6],F[7],F[8],)

    def move_Lprime(self):
        B = self.B[:]
        L = self.L[:]
        U = self.U[:]
        #R = self.R[:]
        D = self.D[:]
        F = self.F[:]

        self.B = (U[0],B[1],B[2],
                  U[3],B[4],B[5],
                  U[6],B[7],B[8],)
        self.L = (L[2],L[5],L[8],
                  L[1],L[4],L[7],
                  L[0],L[3],L[6],)
        self.U = (F[0],U[1],U[2],
                  F[3],U[4],U[5],
                  F[6],U[7],U[8],)
        #self.R = (R[0],R[1],R[2],R[3],R[4],R[5],R[6],R[7],R[8],)
        self.D = (D[0],D[1],B[6],
                  D[3],D[4],B[3],
                  D[6],D[7],B[0],)
        self.F = (D[8],F[1],F[2],
                  D[5],F[4],F[5],
                  D[2],F[7],F[8],)

    def move_D(self):
        B = self.B[:]
        L = self.L[:]
        # U = self.U[:]
        R = self.R[:]
        D = self.D[:]
        F = self.F[:]

        self.B = (R[2],R[5],R[8], 
                  B[3],B[4],B[5], 
                  B[6],B[7],B[8],)
        self.L = (B[2],L[1],L[2], 
                  B[1],L[4],L[5], 
                  B[0],L[7],L[8],)
        # self.U = (U[0],U[1],U[2], 
        #           U[3],U[4],U[5], 
        #           U[6],U[7],U[8],)
        self.R = (R[0],R[1],F[8], 
                  R[3],R[4],F[7], 
                  R[6],R[7],F[6],)
        self.D = (D[6],D[3],D[0], 
                  D[7],D[4],D[1], 
                  D[8],D[5],D[2],)
        self.F = (F[0],F[1],F[2], 
                  F[3],F[4],F[5], 
                  L[0],L[3],L[6],)

    def move_Dprime(self):
        B = self.B[:]
        L = self.L[:]
        # U = self.U[:]
        R = self.R[:]
        D = self.D[:]
        F = self.F[:]

        self.B = (L[6],L[3],L[0], 
                  B[3],B[4],B[5], 
                  B[6],B[7],B[8],)
        self.L = (F[6],L[1],L[2], 
                  F[7],L[4],L[5], 
                  F[8],L[7],L[8],)
        # self.U = (U[0],U[1],U[2], 
        #           U[3],U[4],U[5], 
        #           U[6],U[7],U[8],)
        self.R = (R[0],R[1],B[0], 
                  R[3],R[4],B[1], 
                  R[6],R[7],B[2],)
        self.D = (D[2],D[5],D[8], 
                  D[1],D[4],D[7], 
                  D[0],D[3],D[6],)
        self.F = (F[0],F[1],F[2], 
                  F[3],F[4],F[5], 
                  R[8],R[5],R[2],)

    def move_F(self):
        # B = self.B[:]
        L = self.L[:]
        U = self.U[:]
        R = self.R[:]
        D = self.D[:]
        F = self.F[:]

        # self.B = (B[0],B[1],B[2], 
        #           B[3],B[4],B[5], 
        #           B[6],B[7],B[8],)
        self.L = (L[0],L[1],L[2], 
                  L[3],L[4],L[5], 
                  D[6],D[7],D[8],)
        self.U = (U[0],U[1],U[2], 
                  U[3],U[4],U[5], 
                  L[6],L[7],L[8],)
        self.R = (R[0],R[1],R[2], 
                  R[3],R[4],R[5], 
                  U[6],U[7],U[8],)
        self.D = (D[0],D[1],D[2], 
                  D[3],D[4],D[5], 
                  R[6],R[7],R[8],)
        self.F = (F[6],F[3],F[0], 
                  F[7],F[4],F[1], 
                  F[8],F[5],F[2],)

    def move_Fprime(self):
        # B = self.B[:]
        L = self.L[:]
        U = self.U[:]
        R = self.R[:]
        D = self.D[:]
        F = self.F[:]

        # self.B = (B[0],B[1],B[2], 
        #           B[3],B[4],B[5], 
        #           B[6],B[7],B[8],)
        self.L = (L[0],L[1],L[2], 
                  L[3],L[4],L[5], 
                  U[6],U[7],U[8],)
        self.U = (U[0],U[1],U[2], 
                  U[3],U[4],U[5], 
                  R[6],R[7],R[8],)
        self.R = (R[0],R[1],R[2], 
                  R[3],R[4],R[5], 
                  D[6],D[7],D[8],)
        self.D = (D[0],D[1],D[2], 
                  D[3],D[4],D[5], 
                  L[6],L[7],L[8],)
        self.F = (F[2],F[5],F[8], 
                  F[1],F[4],F[7], 
                  F[0],F[3],F[6],)

    def move_B(self):
        B = self.B[:]
        L = self.L[:]
        U = self.U[:]
        R = self.R[:]
        D = self.D[:]
        # F = self.F[:]

        self.B = (B[6],B[3],B[0], 
                  B[7],B[4],B[1], 
                  B[8],B[5],B[2],)
        self.L = (U[0],U[1],U[2], 
                  L[3],L[4],L[5], 
                  L[6],L[7],L[8],)
        self.U = (R[0],R[1],R[2], 
                  U[3],U[4],U[5], 
                  U[6],U[7],U[8],)
        self.R = (D[0],D[1],D[2], 
                  R[3],R[4],R[5], 
                  R[6],R[7],R[8],)
        self.D = (L[0],L[1],L[2], 
                  D[3],D[4],D[5], 
                  D[6],D[7],D[8],)
        # self.F = (F[0],F[1],F[2], 
        #           F[3],F[4],F[5], 
        #           F[6],F[7],F[8],)

    def move_Bprime(self):
        B = self.B[:]
        L = self.L[:]
        U = self.U[:]
        R = self.R[:]
        D = self.D[:]
        # F = self.F[:]

        self.B = (B[2],B[5],B[8], 
                  B[1],B[4],B[7], 
                  B[0],B[3],B[6],)
        self.L = (D[0],D[1],D[2], 
                  L[3],L[4],L[5], 
                  L[6],L[7],L[8],)
        self.U = (L[0],L[1],L[2], 
                  U[3],U[4],U[5], 
                  U[6],U[7],U[8],)
        self.R = (U[0],U[1],U[2], 
                  R[3],R[4],R[5], 
                  R[6],R[7],R[8],)
        self.D = (R[0],R[1],R[2], 
                  D[3],D[4],D[5], 
                  D[6],D[7],D[8],)
        # self.F = (F[0],F[1],F[2], 
        #           F[3],F[4],F[5], 
        #           F[6],F[7],F[8],)

    def move_X(self):
        B = self.B[:]
        L = self.L[:]
        U = self.U[:]
        R = self.R[:]
        D = self.D[:]
        F = self.F[:]

        self.B = (B[0],B[1],B[2], 
                  B[3],B[4],B[5], 
                  B[6],B[7],B[8],)
        self.L = (L[0],L[1],L[2], 
                  L[3],L[4],L[5], 
                  L[6],L[7],L[8],)
        self.U = (U[0],U[1],U[2], 
                  U[3],U[4],U[5], 
                  U[6],U[7],U[8],)
        self.R = (R[0],R[1],R[2], 
                  R[3],R[4],R[5], 
                  R[6],R[7],R[8],)
        self.D = (D[0],D[1],D[2], 
                  D[3],D[4],D[5], 
                  D[6],D[7],D[8],)
        self.F = (F[0],F[1],F[2], 
                  F[3],F[4],F[5], 
                  F[6],F[7],F[8],)

    def sexy(self):
        self.move_R()
        self.move_U()
        self.move_Rprime()
        self.move_Uprime()

    def left_sexy(self):
        self.move_Lprime()
        self.move_Uprime()
        self.move_L()
        self.move_U()

    def generate_scramble(self):
        s = []
        x = ['B','L','U','R','D','F']
        moves = []
        for m in x:
            moves.append(m)
            moves.append(m + "'")
            moves.append(m + "2")
        previous = 'X'
        for i in range(21):
            while True:
                n = random.randint(0,17)
                next = moves[n]
                if next[0] != previous[0]:
                    s.append(next)
                    previous = next
                    break
        return s
    def scramble_string(self,scr):
        s = ""
        for m in scr:
            s += m + ' '
        return s

    def apply_move(self,m):
        if m == 'B':
            self.move_B()
        if m == 'L':
            self.move_L()
        if m == 'U':
            self.move_U()
        if m == 'R':
            self.move_R()
        if m == 'D':
            self.move_D()
        if m == 'F':
            self.move_F()

        if m == "B'":
            self.move_Bprime()
        if m == "L'":
            self.move_Lprime()
        if m == "U'":
            self.move_Uprime()
        if m == "R'":
            self.move_Rprime()
        if m == "D'":
            self.move_Dprime()
        if m == "F'":
            self.move_Fprime()

        if m == 'B2':
            self.move_B()
            self.move_B()
        if m == 'L2':
            self.move_L()
            self.move_L()
        if m == 'U2':
            self.move_U()
            self.move_U()
        if m == 'R2':
            self.move_R()
            self.move_R()
        if m == 'D2':
            self.move_D()
            self.move_D()
        if m == 'F2':
            self.move_F()
            self.move_F()
    def scramble(self,scr):
        for m in scr:
            self.apply_move(m)

if __name__ == "__main__":
    print("Resolved")
    c = cube()
    print(c)

    print("U Uprime move")
    c = cube()
    c.move_U()
    c.move_Uprime()
    print(c)
    if c.is_resolved():
        print("Cube is Resolved :-)")
    else:
        print("Cube is NOT Resolved :-( " + str(c.diff()))
        sys.exit(0)

    print("R Rprime move")
    c = cube()
    c.move_Rprime()
    c.move_R()
    print(c)
    if c.is_resolved():
        print("Cube is Resolved :-)")
    else:
        print("Cube is NOT Resolved :-( " + str(c.diff()))
        sys.exit(0)

    print("6 Sexy")
    c = cube()
    c.sexy()
    c.sexy()
    c.sexy()
    c.sexy()
    c.sexy()
    c.sexy()
    print(c)
    if c.is_resolved():
        print("Cube is Resolved :-)")
    else:
        print("Cube is NOT Resolved :-( " + str(c.diff()))
        sys.exit(0)

    print("L Lprime move")
    c = cube()
    c.move_Lprime()
    c.move_L()
    print(c)
    if c.is_resolved():
        print("Cube is Resolved :-)")
    else:
        print("Cube is NOT Resolved :-( " + str(c.diff()))
        sys.exit(0)

    print("6 left sexy")
    c = cube()
    c.left_sexy()
    c.left_sexy()
    c.left_sexy()
    c.left_sexy()
    c.left_sexy()
    c.left_sexy()
    print(c)
    if c.is_resolved():
        print("Cube is Resolved :-)")
    else:
        print("Cube is NOT Resolved :-( " + str(c.diff()))
        sys.exit(0)

    print("D Dprime move")
    c = cube()
    c.move_D()
    c.move_Dprime()
    print(c)
    if c.is_resolved():
        print("Cube is Resolved :-)")
    else:
        print("Cube is NOT Resolved :-( " + str(c.diff()))
        sys.exit(0)

    print("F Fprime move")
    c = cube()
    c.move_F()
    c.move_Fprime()
    print(c)
    if c.is_resolved():
        print("Cube is Resolved :-)")
    else:
        print("Cube is NOT Resolved :-( " + str(c.diff()))
        sys.exit(0)

    print("B Bprime move")
    c = cube()
    c.move_B()
    c.move_Bprime()
    print(c)
    if c.is_resolved():
        print("Cube is Resolved :-)")
    else:
        print("Cube is NOT Resolved :-( " + str(c.diff()))
        sys.exit(0)


    print("All cases OK.")

    scr = c.generate_scramble()
    print(c.scramble_string(scr))
    c.scramble(scr)
    print(c)
    print("Cube is NOT Resolved :-( " + str(c.diff()))
