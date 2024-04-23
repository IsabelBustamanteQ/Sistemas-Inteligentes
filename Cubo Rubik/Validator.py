
import numpy as np
class Validator():
    def __init__(self,cube) -> None:
        self.cube=cube
    def valid_letters(self):
        allowed_letters = {'W', 'O', 'G', 'R', 'B', 'Y'}
        if np.all(np.isin(self.cube, list(allowed_letters))):
            print("El array contiene solo las letras permitidas.")
            return True
        else:
            print("El archivo contiene letras NO VALIDAS")
            return False
    def valid_letter_quantity(self):
        allowed_letters = {'W', 'O', 'G', 'R', 'B', 'Y'}
        for letter in allowed_letters:
            letter_quantity = np.count_nonzero(self.cube == letter)
            if not letter_quantity== 9:
                print("El archivo contiene ",letter_quantity, " letras ",letter)