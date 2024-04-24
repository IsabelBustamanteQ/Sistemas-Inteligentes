
import numpy as np
from Validator import Validator 
class Rubik_cube():
    def __init__(self):
        self.moves=[]
        self.sides=np.array([
            [
                        ["W","W","W"],
                        ["W","W","W"],
                        ["W","W","W"]
            ],
            [
                        ["O","O","O"],
                        ["O","O","O"],
                        ["O","O","O"]
            ],
            [
                        ["G","G","G"],
                        ["G","G","G"],
                        ["G","G","G"]
            ],
            [
                        ["R","R","R"],
                        ["R","R","R"],
                        ["R","R","R"]
            ],
            [
                        ["B","B","B"],
                        ["B","B","B"],
                        ["B","B","B"]
            ],
            [
                        ["Y","Y","Y"],
                        ["Y","Y","Y"],
                        ["Y","Y","Y"]
            ]
        ])
        
    def print_side(self, side):
        for line in side:
            print(" ".join(line))
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
    def is_goal_state(self):
        return np.all(self.sides[0] == self.sides[0][1][1]) and \
               np.all(self.sides[1] == self.sides[1][1][1]) and \
               np.all(self.sides[2] == self.sides[2][1][1]) and \
               np.all(self.sides[3] == self.sides[3][1][1]) and \
               np.all(self.sides[4] == self.sides[4][1][1]) and \
               np.all(self.sides[5] == self.sides[5][1][1])

    def valid_moves(self):
        return ["U", "U'", "D", "D'", "F", "F'", "B", "B'", "R", "R'", "L", "L'"
                # ,"S","S'","E","E'","M","M'"
                ]

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
    
    def add_move(self,move):
        self.moves.append(move)

    def misplaced_pieces(self):
        not_in_correct_place=sum(1 for side in self.sides for row in side for element in row if element!=side[1][1])
        return not_in_correct_place
    def manhattan_distance(self):
        distance = 0
        goal_state = np.array([
            [['W','W','W'], ['W','W','W'], ['W','W','W']],
            [['O','O','O'], ['O','O','O'], ['O','O','O']],
            [['G','G','G'], ['G','G','G'], ['G','G','G']],
            [['R','R','R'], ['R','R','R'], ['R','R','R']],
            [['B','B','B'], ['B','B','B'], ['B','B','B']],
            [['Y','Y','Y'], ['Y','Y','Y'], ['Y','Y','Y']]
        ])

        for side in range(6):
            distance += np.sum(np.abs(np.where(self.sides[side] != goal_state[side])))
        
        return distance
    def combined_heuristic(self):
        manhattan_dist = self.manhattan_distance()
        misplaced = self.misplaced_pieces()

        combined_cost = manhattan_dist + misplaced

        return combined_cost
    def __lt__(self,other):
        return self.combined_heuristic()<other.combined_heuristic()
    
    def load_cube(self,file_path):
        try:
            with open(file_path, 'r') as file:
                    lines = file.readlines()
                    cube = []
                    side=[]
                    if len(lines)!=18:
                        print("El archivo debe contener 18 lineas, tiene ",len(lines), " lineas")
                        return False
                    for line in lines:
                        array=line.split()
                        if len(side)<3:
                            side.append(array)
                        if len(side)==3:    
                            cube.append(side)
                            side=[]
                    possible_cube=np.array(cube)
                    validator=Validator(possible_cube)
                    if validator.all_validations():
                        self.sides=possible_cube
                        return True
        except FileNotFoundError:
            print("El archivo no se encuentra")
            return False

                