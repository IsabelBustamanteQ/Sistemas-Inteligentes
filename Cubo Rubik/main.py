class Rubik_cube():
    def __init__(self):
        self.up_side=[
                        ["W","W","W"],
                        ["W","W","W"],
                        ["W","W","W"],
        ]
        self.front_side=[
                        ["G","G","G"],
                        ["G","G","G"],
                        ["G","G","G"],
        ]
        self.down_side=[
                        ["Y","Y","Y"],
                        ["Y","Y","Y"],
                        ["Y","Y","Y"],
        ]
        self.left_side=[
                        ["O","O","O"],
                        ["O","O","O"],
                        ["O","O","O"],
        ]
        self.right_side=[
                        ["R","R","R"],
                        ["R","R","R"],
                        ["R","R","R"],
        ]
        self.back_side=[
                        ["B","B","B"],
                        ["B","B","B"],
                        ["B","B","B"],
        ]
        
    def print_side(self, side):
        str=""
        for line in side:
            for piece in line:
                str=str+piece+" "
            print(str) 
            str=""      
    def show_cube(self):
        self.print_side(self.up_side)
        self.print_side(self.left_side)
        self.print_side(self.front_side)
        self.print_side(self.right_side)
        self.print_side(self.back_side)
        self.print_side(self.down_side)
    
if __name__ == "__main__":
    rubik=Rubik_cube()
    rubik.show_cube()

