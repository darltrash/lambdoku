# Para ejecutar este programa en local, como cualquier programa

from src.sudoku import Sudoku

# Itera hasta obtener un numero del usuario
def get_number(name):
    v = 0
    while 1:
        s = input(f"{name}? ")
        if s.isnumeric():
            v = int(s)
            break

    return v


# Creamos una instancia
puzzle = Sudoku()

while 1:
    puzzle.render()
    val = input("[E]scribir, [R]esolver, [S]alir, [N]uevo > ").lower().strip(" ")

    if val=="e":
        # Obtenemos posicion y 
        x = get_number("X")
        y = get_number("Y")
        v = get_number("Valor")

        # Y ultimamente, insertamos el Valor en X, Y
        try:
            puzzle.set_at(x, y, v) 
        except Exception as e:
            print(f"ERROR! {e}")

        input("Presione intro para continuar")

    elif val=="r":
        print("TODO")

    elif val=="s":
        print("Bye!")
        break

    elif val=="n":
        print("Regenerando...")
        sudoku = Sudoku()

    else:
        print(f"Opcion '{val}' no es reconocida!")

    print()