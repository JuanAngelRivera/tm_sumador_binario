from tm_length_verification import tm_length_verification
from tm_sum import tm_sum

while True:
    original_input = input('Introduce la suma binaria {1, 0} de la forma \'...+...=\'\n')

    tm = tm_length_verification(original_input, 0)
    verification = tm.recognize()

    if verification == True:
        print('\nReconocido!\n\n')
        tm = tm_sum(original_input, 0, int(len(original_input) / 2 + 1))
        result = tm.recognize()

        if result != None:
            print(result)
    else:
        print('Cadena no reconocida, los operandos deben de ser de la misma longitud')