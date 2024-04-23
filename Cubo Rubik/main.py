from Rubik_cube import Rubik_cube
from Validator import Validator
from Solver import Solver
if __name__ == "__main__":
    rubik=Rubik_cube()
    rubik.load_cube("cube1.txt")
    # rubik.action("F")
    # rubik.action("L")
    # rubik.action("D'")
    # rubik.action("U'")
    # rubik.action("B")
    rubik.show_cube()
    print(rubik.sides.shape)
    val=Validator(rubik.sides)
    val.valid_letters()
    val.valid_letter_quantity()
    solver=Solver(rubik)
    # # print(rubik.mishattan_distance())
    solver.a_star_solve()
    


