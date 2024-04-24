from Rubik_cube import Rubik_cube
from Validator import Validator
from Solver import Solver
import subprocess
if __name__ == "__main__":
    rubik=Rubik_cube()
    while True:
        
        print("MENÚ DE OPCIONES:")
        print("1. Leer cubo de archivo")
        print("2. Mostrar cubo actual")
        print("3. Resolver cubo")
        print("0. Salir")
        option=input()
        match option:
            case "0":
                break
            case "1":
                file_name=input("introduce el nombre del archivo que contiene el cubo rubik: ")

                success=rubik.load_cube(file_name)
                # rubik.show_cube()
                if success:
                    print("El cubo fue cargado exitósamente")
                else:
                    print("El cubo no pudo cargarse, se usa el cubo armado por defecto")
            case "2":
                rubik.show_cube()
            case "3":
                print("Buscando solución....")
                solver=Solver(rubik)
                response=solver.a_star_solve()
                if not response:
                    print("Noo se encontró la solucion")
        wait=input("Presiona enter para continuar")
        subprocess.call(["cmd.exe", "/C", "cls"])
