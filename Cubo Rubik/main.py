class Rubik_cube():
    def __init__(self):
        self.sides=[
            [
                        ["W","W","W"],
                        ["W","W","W"],
                        ["W","W","W"],
            ],
            [
                        ["O","O","O"],
                        ["O","O","O"],
                        ["O","O","O"],
            ],
            [
                        ["G","G","G"],
                        ["G","G","G"],
                        ["G","G","G"],
            ],
            [
                        ["R","R","R"],
                        ["R","R","R"],
                        ["R","R","R"],
            ],
            [
                        ["B","B","B"],
                        ["B","B","B"],
                        ["B","B","B"],
            ],
            [
                        ["Y","Y","Y"],
                        ["Y","Y","Y"],
                        ["Y","Y","Y"],
            ]
        ]
        
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
        first_line=self.sides[sides[-1]][row]
        for position in range(len(sides)-1):
            line=self.sides[sides[position]][row]
            self.sides[sides[position-1]][row]=line
        self.sides[sides[2]][row]=first_line

if __name__ == "__main__":
    rubik=Rubik_cube()
    # print("Up clockwise")
    # rubik.up_clockwise()
    # print("Up inverted")
    # rubik.up_inverted()
    # print("down Clockwise")
    # rubik.down_clockwise()
    print("down inverted")
    rubik.down_inverted()
    rubik.show_cube()
    


