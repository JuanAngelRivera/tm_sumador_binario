from tm_length_verification import tm_length_verification
from tm_sum import tm_sum
import sys

sys.setrecursionlimit(100000)

while True:
    original_input = input('Introduce la suma binaria {1, 0} de la forma \'...+...=\'\n')

    tm = tm_length_verification(original_input, 0)
    verification = tm.recognize()

    if verification == True:
        print('\nReconocido!\n\n')
        tm = tm_sum(original_input, 0, int(len(original_input) / 2 + 1))
        result = tm.recognize()

        if result != None:
            with open('accepted.data', 'a') as file:
                final = ''
                for char in result:
                    final = final + char
                print(f"Resultado:{final}\n El resultado se lee de derecha a izquierda")
                file.write("".join(final) + '\n')
        else:
            with open('rejeted.data', 'a') as file:
                file.write("".join(original_input) + '\n')
    else:
        print('Cadena no reconocida, los operandos deben de ser de la misma longitud')