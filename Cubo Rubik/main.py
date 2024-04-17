import numpy as np
from collections import deque
import copy
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
    
    def e_clockwise(self):
        sides=[1,2,3,4]
        self.row_motion(sides,1)
    
    def e_inverted(self):
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
        self.row_and_column_motion(sides,line_number,True)
        self.roll_right(2)
        
    def front_inverted(self):
        sides=[0,3,5,1]
        line_number=[-1,0,0,-1]
        self.row_and_column_motion(sides,line_number,False)
        self.roll_left(2)
    
    def back_clockwise(self):
        sides=[0,3,5,1]
        line_number=[0,-1,-1,0]
        self.row_and_column_motion(sides,line_number,False)
        self.roll_right(4)
        
    def back_inverted(self):
        sides=[0,1,5,3]
        line_number=[0,0,-1,-1]
        self.row_and_column_motion(sides,line_number,True)
        self.roll_left(4)

    def s_clockwise(self):
        sides=[0,1,5,3]
        line_number=[1,1,1,1]
        self.row_and_column_motion(sides,line_number,True)
    
    def s_inverted(self):
        sides=[0,3,5,1]
        line_number=[1,1,1,1]
        self.row_and_column_motion(sides,line_number,False)
    
    def row_and_column_motion(self,sides,line_number,right):
        # Right false para F'
        first_line=(self.sides[sides[3]][:,line_number[-1]]).copy()
        for position in range(len(sides)-1):
            if position%2==0: #si es fila
                line=self.sides[sides[position]][line_number[position]]
                line=self.flip_line(line,not right)
                self.sides[sides[position-1]][:,line_number[position-1]]=line
            else:#si es columna
                line=self.sides[sides[position]][:,line_number[position]]
                self.sides[sides[position-1]][line_number[position-1]]=self.flip_line(line,right)
        self.sides[sides[2]][line_number[2]]=self.flip_line(first_line,right)
    def flip_line(self,line,right):
        if right:
            return np.flip(line)
        return line
    def right_clockwise(self):
        sides=[0,2,5,4]
        columns=[-1,-1,-1,0]
        self.column_motion(sides,columns,True)
        self.roll_right(3)
    
    def right_inverted(self):
        sides=[0,4,5,2]
        columns=[-1,0,-1,-1]
        self.column_motion(sides,columns,False)
        self.roll_left(3)
    
    def left_clockwise(self):
        sides=[0,4,5,2]
        columns=[0,-1,0,0]
        self.column_motion(sides,columns,False)
        self.roll_right(1)
   
    def left_inverted(self):
        sides=[0,2,5,4]
        columns=[0,0,0,-1]
        self.column_motion(sides,columns,True)
        self.roll_left(1)
    
    def m_clockwise(self):
        sides=[0,2,5,4]
        columns=[1,1,1,1]
        self.column_motion(sides,columns,True)

    def m_inverted(self):
        sides=[0,4,5,2]
        columns=[1,1,1,1]
        self.column_motion(sides,columns,False)
    def column_motion(self,sides, columns,right):
        first_line=self.sides[sides[-1]][:,columns[-1]].copy()
        for position in range(len(sides)-1):
            line=self.sides[sides[position]][:,columns[position]]
            if position==0:
                line=self.flip_line(line,right)
            else:
                line=self.flip_line(line,not right)
            self.sides[sides[position-1]][:,columns[position-1]]=line
        self.sides[sides[2]][:,columns[2]]=self.flip_line(first_line,right)

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
        for side in range(len(self.sides)-1):
            if not self.side_is_finished(side):
                return False
        return True
    def action(self,action):
        match action:
            case "U":
                self.up_clockwise()
            case "U'":
                self.up_inverted()
            case "D":
                self.down_clockwise()
            case "D'":
                self.down_inverted()
            case "F":
                self.front_clockwise()
            case "F'":
                self.front_inverted()
            case "B":
                self.back_clockwise()
            case "B'":
                self.back_inverted()
            case "R":
                self.right_clockwise()
            case "R'":
                self.right_inverted()
            case "L":
                self.left_clockwise()
            case "L'":
                self.left_inverted()
            case "E":
                self.e_clockwise()
            case "E'":
                self.e_inverted()
            case "S":
                self.s_clockwise()
            case "S'":
                self.s_inverted()
            case "M":
                self.m_clockwise()
            case "M'":
                self.m_inverted()
    
if __name__ == "__main__":
    rubik=Rubik_cube()
    rubik.action("")
    rubik.show_cube()
    



