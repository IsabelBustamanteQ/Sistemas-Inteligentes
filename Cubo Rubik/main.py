import numpy as np
class Rubik_cube():
    def __init__(self):
        self.sides=np.array([
            [
                        ["W","W","W"],
                        ["w","W","W"],
                        ["W1","W2","W3"],
            ],
            [
                        ["O","O","O1"],
                        ["O","O","O2"],
                        ["O","O","O3"],
            ],
            [
                        ["G","G","G"],
                        ["G","G","G"],
                        ["G","G","G"],
            ],
            [
                        ["R1","R","R"],
                        ["R2","R","R"],
                        ["R3","R","R"],
            ],
            [
                        ["B","B","B"],
                        ["B","B","B"],
                        ["B","B","B"],
            ],
            [
                        ["Y1","Y2","Y3"],
                        ["Y","Y","Y"],
                        ["Y","Y","Y"],
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
    
    def up_inverted(self):
        sides=[4,3,2,1]
        self.row_motion(sides,0)
    
    def down_clockwise(self):
        sides=[4,3,2,1]
        self.row_motion(sides,-1)
        
    
    def down_inverted(self):
        sides=[1,2,3,4]
        self.row_motion(sides,-1)

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
        self.column_motion(sides,line_number)
        
    def front_inverted(self):
        sides=[0,3,5,1]
        line_number=[-1,0,0,-1]
        self.column_motion(sides,line_number)
        
    def column_motion(self,sides,line_number):
        first_line=(self.sides[sides[3]][:,line_number[-1]]).copy()
        print("Primera línea:",first_line)
        for position in range(len(sides)-1):
            print(position)
            if position%2==0: #si es fila
                line=self.sides[sides[position]][line_number[position]]
                print(line)
                self.sides[sides[position-1]][:,line_number[position-1]]=line
            else:#si es columna
                line=self.sides[sides[position]][:,line_number[position]]
                self.sides[sides[position-1]][line_number[position-1]]=line
                print(line)
        print("Primera línea:",first_line)
        self.sides[sides[2]][line_number[2]]=first_line

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
    rubik.front_clockwise()
    # rubik.front_inverted()
    rubik.show_cube()




