# Esta funcion transforma coordenadas en 2D a 1D
def indicize(x, y):
    if not x in range(1, 10):
        raise Exception("X fuera de rango!")

    if not y in range(1, 10):
        raise Exception("Y fuera de rango!")

    return int(y-1) * 9 + int(x-1)


# Nuestra clase de tablero sudoku
class Sudoku:
    map = [0] * 9 * 9

    # Crea un tablero desde un array de 9x9 valores del 1 al 9
    def from_array(array):
        s = Sudoku()

        # Checar si la longitud del array es 9x9 (81)
        array_length = len(array)
        if array_length != (9 * 9):
            raise Exception(f"Entrada no tiene el tamaño correcto! (se experaba 81, es {array_length})")

        # Chequeamos si los valores estan entre 0 y 9
        for valor in array:
            if not val in range(0, 10):
                raise Exception("Valor fuera de rango!")

        s.map = array

        return s

    # Define el valor en X, Y a Val
    def set_at(self, x, y, val):
        if not val in range(0, 9):
            raise Exception("Valor fuera de rango!")

        index = indicize(x, y)

        self.map[index] = val

    # Obtiene el valor en X, Y
    def get_at(self, x, y):
        index = indicize(x, y)

        return self.map[index]

    # Renderiza el tablero
    def render(self):
        for a in range(0, 3):
            print("-" * 25)
            for b in range(0, 3):
                print("|", end=" ")
                for c in range(0, 3):
                    for d in range(0, 3):
                        index = (b + a*3) * 9 + (d + c*3) 
                        print(self.map[index], end=" ")
                    print("|", end=" ")
                print()

        print("-" * 25)
        
