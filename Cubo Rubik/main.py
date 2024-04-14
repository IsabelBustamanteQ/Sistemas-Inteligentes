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
        self.up_wise(sides,0)
        
    
    def up_inverted(self):
        sides=[4,3,2,1]
        self.up_wise(sides,0)

    def up_wise(self, sides_list, row):
        sides=sides_list
        first_side_line=self.sides[sides[-1]][row]
        print(first_side_line)
        for position in range(len(sides)-1):
            print(position)
            first_line=self.sides[sides[position]][row]
            self.sides[sides[position-1]][row]=first_line
            print(first_line)
        self.sides[sides[2]][row]=first_side_line

if __name__ == "__main__":
    rubik=Rubik_cube()
    print("Up clockwise")
    rubik.up_clockwise()
    # print("Up inverted")
    # rubik.up_inverted()
    rubik.show_cube()
    


