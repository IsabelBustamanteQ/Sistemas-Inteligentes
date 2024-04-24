
import numpy as np
class Validator():
    def __init__(self,cube) -> None:
        self.cube=cube
    def valid_letters(self):
        allowed_letters = {'W', 'O', 'G', 'R', 'B', 'Y'}
        if np.all(np.isin(self.cube, list(allowed_letters))):
            return True
        else:
            print("El archivo contiene letras NO VALIDAS")
            return False
    def valid_letter_quantity(self):
        allowed_letters = {'W', 'O', 'G', 'R', 'B', 'Y'}
        result=True
        for letter in allowed_letters:
            letter_quantity = np.count_nonzero(self.cube == letter)
            if not letter_quantity== 9:
                print("El archivo contiene ",letter_quantity, " letras ",letter) 
                result=False
        return result   
    def valid_edges(self):
        oposites_colors={
            "W":"Y",
            "O":"R",
            "G":"B",
            "R":"O",
            "B":"R",
            "Y":"W"
        }        
        if self.cube[4][1][2]!=oposites_colors[self.cube[0][0][0]]:
            print("Esquina bien")   
        else:
            print("Error en las esquinas")   
    def all_validations(self):
        if self.valid_letters() and self.valid_letter_quantity():
            print("El cubo es Valido")
            return True
        print("No pasó las validaciones")
        return False
