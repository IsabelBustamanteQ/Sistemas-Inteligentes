from queue import PriorityQueue
import numpy as np
from collections import deque
import copy
class Rubik_cube():
    def __init__(self):
        # self.sides=np.array([
        #     [
        #                 ["W","W","W"],
        #                 ["W","W","W"],
        #                 ["W","W","W"]
        #     ],
        #     [
        #                 ["O","O","O"],
        #                 ["O","O","O"],
        #                 ["O","O","O"]
        #     ],
        #     [
        #                 ["G","G","G"],
        #                 ["G","G","G"],
        #                 ["G","G","G"]
        #     ],
        #     [
        #                 ["R","R","R"],
        #                 ["R","R","R"],
        #                 ["R","R","R"]
        #     ],
        #     [
        #                 ["B","B","B"],
        #                 ["B","B","B"],
        #                 ["B","B","B"]
        #     ],
        #     [
        #                 ["Y","Y","Y"],
        #                 ["Y","Y","Y"],
        #                 ["Y","Y","Y"]
        #     ]
        # ])
        self.sides=np.array([
            [['O', 'G', 'W'], ['R', 'O', 'B'], ['Y', 'O', 'B']
            ],
            [['G', 'G', 'R'], ['G', 'G', 'G'], ['G', 'Y', 'B']
            ],
            [['G', 'Y', 'R'], ['Y', 'W', 'O'], ['R', 'B', 'W']
            ],
            [['Y', 'R', 'O'], ['W', 'B', 'W'], ['O', 'B', 'O'],
            ],
            [['G', 'W', 'Y'], ['R', 'Y', 'O'], ['Y', 'R', 'R']
            ],
            [['W', 'O', 'B'], ['B', 'R', 'W'], ['W', 'Y', 'B']
            ]
        ])
#         self.cubo2 = {
#             'U': np.array([['B', 'R', 'R'], ['B', 'W', 'W'], ['B', 'W', 'W']]),  # Upper (arriba)
#             'D': np.array([['Y', 'Y', 'O'], ['Y', 'Y', 'O'], ['G', 'G', 'G']]),  # Down (abajo)
#             'F': np.array([['R', 'G', 'G'], ['W', 'G', 'G'], ['R', 'R', 'Y']]),  # Front (frente)
#             'B': np.array([['B', 'B', 'O'], ['B', 'B', 'Y'], ['O', 'O', 'O']]),  # Back (atrás)
#             'L': np.array([['W', 'W', 'W'], ['O', 'O', 'O'], ['W', 'G', 'G']]),  # Left (izquierda)
#             'R': np.array([['R', 'R', 'Y'], ['R', 'R', 'Y'], ['B', 'B', 'Y']])   # Right (derecha)
#         }
# self.cubo2 = {
#             'U': np.array([['O', 'G', 'W'], ['R', 'O', 'B'], ['Y', 'O', 'B']]),  # Upper (arriba)
#             'D': np.array([['W', 'O', 'B'], ['B', 'R', 'W'], ['W', 'Y', 'B']]),  # Down (abajo)
#             'F': np.array([['G', 'Y', 'R'], ['Y', 'W', 'O'], ['R', 'B', 'W']]),  # Front (frente)
#             'B': np.array([['G', 'W', 'Y'], ['R', 'Y', 'O'], ['Y', 'R', 'R']]),  # Back (atrás)
#             'L': np.array([['G', 'G', 'R'], ['G', 'G', 'G'], ['G', 'Y', 'B']]),  # Left (izquierda)
#             'R': np.array([['Y', 'R', 'O'], ['W', 'B', 'W'], ['O', 'B', 'O']])   # Right (derecha)
#         }
        
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
    
    def bfs_solve(self):
        queue = deque([(self, [])])
        while queue:
            current_cube, moves = queue.popleft()
            print(moves)
            if current_cube.is_goal_state():
                return moves
            for move in self.valid_moves():
                new_cube = copy.deepcopy(current_cube)
                new_cube.action(move)
                queue.append((new_cube, moves + [move]))
        return None
    def heuristic(self):
        not_in_correct_place=sum(1 for side in self.sides for row in side for element in row if element!=side[1][1])
        return not_in_correct_place
class State():
    def __init__(self,cube):
        self.cube=cube
        self.moves=[]
    def __lt__(self,other):
        return self.cube.heuristic()<other.cube.heuristic()
    def add_move(self,move):
        self.moves.append(move)

class Solver():
    def __init__(self,state):
        self.state=state
    def heuristic(self,state):
        not_in_correct_place=sum(1 for side in state.cube.sides for row in side for element in row if element!=side[1][1])
        return not_in_correct_place

    def a_star_solve(self):
        start_state=copy.deepcopy(self.state)
        open=PriorityQueue()
        closed=set()
        f_initial=self.heuristic(start_state)
        open.put((f_initial,start_state))
        while not open.empty():
            current_cost,current_state=open.get()
            closed.add(current_state)
            print(current_state.moves)
            if current_state.cube.is_goal_state():
                # Devolver camino
                print("camino encontrado")
                print(current_state.moves)
                return True
            for move in current_state.cube.valid_moves():
                new_state=copy.deepcopy(current_state)
                new_state.cube.action(move)
                new_state.add_move(move)
                new_cost=current_cost+self.heuristic(new_state)
                if new_state not in closed:                
                    open.put((new_cost,new_state))
                    closed.add(new_state)
        return False
if __name__ == "__main__":
    rubik=Rubik_cube()
    # rubik.action("M")
    rubik.action("F")
    rubik.action("L")
    # solution = rubik.bfs_solve()
    # solution=rubik.a_star_solve()
    # if solution:
    #     print("Solución encontrada en {} movimientos:".format(len(solution)))
    #     print(solution)
    # else:
    #     print("No se encontró solución.")
    rubik.show_cube()
    # rubik.heuristic()
    state=State(rubik)
    solver=Solver(state)
    print(solver.heuristic(solver.state))
    solver.a_star_solve()



