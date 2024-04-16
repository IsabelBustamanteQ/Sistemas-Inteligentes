import numpy as np
class Rubik_cube():
    def __init__(self):
        self.sides=np.array([
            [
                        ["W1","W2","W3"],
                        ["W4","W5","W6"],
                        ["W7","W8","W9"],
            ],
            [
                        ["O1","O2","O3"],
                        ["O4","O5","O6"],
                        ["O7","O8","O9"],
            ],
            [
                        ["G1","G2","G3"],
                        ["G4","G5","G6"],
                        ["G7","G8","G9"],
            ],
            [
                        ["R1","R2","R3"],
                        ["R4","R5","R6"],
                        ["R7","R8","R9"],
            ],
            [
                        ["B1","B2","B3"],
                        ["B4","B5","B6"],
                        ["B7","B8","B9"],
            ],
            [
                        ["Y1","Y2","Y3"],
                        ["Y4","Y5","Y6"],
                        ["Y7","Y8","Y9"],
            ]
        ])
        
    def print_side(self, side):
        str=""
        for line in side:
            for piece in line:
                str=str+piece+" "
            print(str) 
            str=""      
    def show_cube(self):
        for side in self.sides:
            self.print_side(side)
            print("------")

    def up_clockwise(self):
        sides=[1,2,3,4]
        self.row_motion(sides,0)
        self.roll_right(0)
    
    def up_inverted(self):
        sides=[4,3,2,1]
        self.row_motion(sides,0)
        self.roll_left(0)
    
    def down_clockwise(self):
        sides=[4,3,2,1]
        self.row_motion(sides,-1)
        self.roll_right(5)
    
    def down_inverted(self):
        sides=[1,2,3,4]
        self.row_motion(sides,-1)
        self.roll_left(5)
    
    def E_clockwise(self):
        sides=[1,2,3,4]
        self.row_motion(sides,1)
    
    def E_inverted(self):
        sides=[4,3,2,1]
        self.row_motion(sides,1)

    def row_motion(self, sides_list, row):
        sides=sides_list
        first_line=self.sides[sides[-1]][row].copy()
        for position in range(len(sides)-1):
            line=self.sides[sides[position]][row]
            self.sides[sides[position-1]][row]=line
        self.sides[sides[2]][row]=first_line
    
    def front_clockwise(self):
        sides=[0,1,5,3]
        line_number=[-1,-1,0,0]
        self.row_and_column_motion(sides,line_number)
        self.roll_right(2)
        
    def front_inverted(self):
        sides=[0,3,5,1]
        line_number=[-1,0,0,-1]
        self.row_and_column_motion(sides,line_number)
        self.roll_left(2)
    
    def back_clockwise(self):
        sides=[0,3,5,1]
        line_number=[0,-1,-1,0]
        self.row_and_column_motion(sides,line_number)
        self.roll_right(4)
        
    def back_inverted(self):
        sides=[0,1,5,3]
        line_number=[0,0,-1,-1]
        self.row_and_column_motion(sides,line_number)
        self.roll_left(4)

    def S_clockwise(self):
        sides=[0,1,5,3]
        line_number=[1,1,1,1]
        self.row_and_column_motion(sides,line_number)
    
    def S_inverted(self):
        sides=[0,3,5,1]
        line_number=[1,1,1,1]
        self.row_and_column_motion(sides,line_number)
    
    def row_and_column_motion(self,sides,line_number):
        first_line=(self.sides[sides[3]][:,line_number[-1]]).copy()
        for position in range(len(sides)-1):
            if position%2==0: #si es fila
                line=self.sides[sides[position]][line_number[position]]
                self.sides[sides[position-1]][:,line_number[position-1]]=line
            else:#si es columna
                line=self.sides[sides[position]][:,line_number[position]]
                self.sides[sides[position-1]][line_number[position-1]]=line
        self.sides[sides[2]][line_number[2]]=first_line

    def right_clockwise(self):
        sides=[0,2,5,4]
        columns=[-1,-1,-1,0]
        self.column_motion(sides,columns)
        self.roll_right(3)
    
    def right_inverted(self):
        sides=[0,4,5,2]
        columns=[-1,0,-1,-1]
        self.column_motion(sides,columns)
        self.roll_left(3)
    
    def left_clockwise(self):
        sides=[0,4,5,2]
        columns=[0,-1,0,0]
        self.column_motion(sides,columns)
        self.roll_right(1)
   
    def left_inverted(self):
        sides=[0,2,5,4]
        columns=[0,0,0,-1]
        self.column_motion(sides,columns)
        self.roll_left(1)
    
    def M_clockwise(self):
        sides=[0,2,5,4]
        columns=[1,1,1,1]
        self.column_motion(sides,columns)

    def M_inverted(self):
        sides=[0,4,5,2]
        columns=[1,1,1,1]
        self.column_motion(sides,columns)
    def column_motion(self,sides, columns):
        first_line=self.sides[sides[-1]][:,columns[-1]].copy()
        for position in range(len(sides)-1):
            line=self.sides[sides[position]][:,columns[position]]
            self.sides[sides[position-1]][:,columns[position-1]]=line
        self.sides[sides[2]][:,columns[2]]=first_line

    def roll_right(self,side):
        self.roll_side(side,1)
    
    def roll_left(self,side):
        self.roll_side(side,0)    
    
    def roll_side(self,side,rotation):
        side_trans=np.transpose(self.sides[side])
        self.sides[side]=np.flip(side_trans,axis = rotation)
    def side_is_finished(self,side):
        return np.all(self.sides[side]==self.sides[side][1][1])
    def is_terminal(self):
        # print(len(self.sides))
        for side in range(len(self.sides)-1):
            # state=self.side_is_finished(side)
            if not self.side_is_finished(side):
                return False
        return True
if __name__ == "__main__":
    rubik=Rubik_cube()
    # print("Up clockwise")
    # rubik.up_clockwise()
    # print("Up inverted")
    # rubik.up_inverted()
    # print("down Clockwise")
    # rubik.down_clockwise()
    # print("down inverted")
    # rubik.down_inverted()
    # rubik.front_clockwise()
    # rubik.front_inverted()
    # rubik.back_clockwise()
    # rubik.back_inverted()
    # rubik.right_clockwise()
    # rubik.right_inverted()
    # rubik.left_clockwise()
    # rubik.left_inverted()
    # rubik.E_clockwise()
    # rubik.E_inverted()
    # rubik.S_clockwise()
    # rubik.S_inverted()
    # rubik.M_clockwise()
    rubik.M_inverted()
    rubik.show_cube()
    
    # print(rubik.is_finished(0))
    # print(rubik.is_terminal())




