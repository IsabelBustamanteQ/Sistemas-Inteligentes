from Rubik_cube import Rubik_cube
from Validator import Validator
from Solver import Solver
if __name__ == "__main__":
    rubik=Rubik_cube()
    rubik.load_cube("invalid_cube2.txt")
    # rubik.show_cube()
    # val=Validator(rubik.sides)
    # val.valid_letters()
    # val.valid_letter_quantity()
    # val.valid_edges()
    # solver=Solver(rubik)
    # solver.a_star_solve()
    


