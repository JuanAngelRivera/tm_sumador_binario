from turing_machine import turing_machine

class tm_length_verification(turing_machine):
    def __init__(self, string_input : str, position : int):
        self.string_input = list(string_input)
        self.string_input.insert(0, ' ')
        self.position = position

    def print(self, state : str, string_input : list, position : int):
        print(f"{state}: {string_input}\n      " + f" " * 5 * position + '↑')

    def recognize(self):
        return self.q0(self.string_input, self.position)

    def q0(self, string_input : list, position : int):
        # self.print('q0', string_input, position)
        if position >= len(string_input):
            return False
    
        char = string_input[position]

        if char == ' ':
            return self.q1(string_input, position + 1)
        else:
            return False

    def q1(self, string_input : list, position : int):
        # self.print('q1', string_input, position)
        if position >= len(string_input):
            return False
        
        char = string_input[position]

        if char == '1' or char == '0':
            string_input[position] = 'x'
            return self.q2(string_input, position + 1)
        else:
            return False
    
    def q2(self, string_input : list, position : int):
        # self.print('q2', string_input, position)
        if position >= len(string_input):
            return False
        
        char = string_input[position]

        if char == '1' or char == '0':
            return self.q2(string_input, position + 1)
        elif char == '+':
            return self.q3(string_input, position + 1)
        else:
            return False
        
    def q3(self, string_input : list, position : int):
        # self.print('q3', string_input, position)
        if position >= len(string_input):
            return False
        
        char = string_input[position]

        if char == 'x':
            return self.q3(string_input, position + 1)
        elif char == '0' or char == '1':
            string_input[position] = 'x'
            return self.q4(string_input, position - 1)
        else:
            return False
    
    def q4(self, string_input : list, position : int):
        # self.print('q4', string_input, position)
        if position >= len(string_input):
            return False
        char = string_input[position]

        if char == '1' or char == '0' or char == '+' or char == 'x':
            return self.q4(string_input, position - 1)
        elif char == ' ':
            return self.q5(string_input, position + 1)
        else:
            return False

    def q5(self, string_input : list, position : int):
        # self.print('q5', string_input, position)
        if position >= len(string_input):
            return False
        
        char = string_input[position]

        if char == '1' or char == '0':
            string_input[position] = 'x'
            return self.q2(string_input, position + 1)
        elif char == '+':
            return self.q6(string_input, position + 1)
        elif char == 'x':
            return self.q5(string_input, position + 1)
        else:
            return False
        
    def q6(self, string_input : list, position : int):
        # self.print('q6', string_input, position)
        if position >= len(string_input):
            return False
        
        char = string_input[position]

        if char == 'x':
            return self.q6(string_input, position + 1)
        elif char == '=':
            return True
        else:
            return False