from turing_machine import turing_machine

class tm_sum(turing_machine):
    def __init__(self, string_input : str, position : int, extra : int):
        self.string_input = list(string_input)
        self.string_input.insert(0, ' ')
        for i in range(extra):
            self.string_input.append(' ')
        self.position = position

    def print(self, state : str, string_input : list, position : int):
        print(f"{state}: {string_input}\n" + ("      " if len(state) == 2 else "       ") + f" " * 5 * position + '↑')

    def recognize(self):
        return self.q0(self.string_input, self.position)

    def q0(self, string_input : list, position : int):
        self.print('q0', string_input, position)
        if position >= len(string_input):
            return None
    
        char = string_input[position]

        if char == ' ':
            return self.q1(string_input, position + 1)
        else:
            return None
    
    def q1(self, string_input : list, position : int):
        self.print('q1', string_input, position)
        if position >= len(string_input):
            return None
    
        char = string_input[position]

        if char == '1' or char == '0':
            return self.q1(string_input, position + 1)
        elif char == '+':
            return self.q2(string_input, position - 1)
        else:
            return None
        
    def q2(self, string_input : list, position : int):
        self.print('q2', string_input, position)
        if position >= len(string_input):
            return None
    
        char = string_input[position]

        if char == 'x' or char == 'y':
            return self.q2(string_input, position - 1)
        elif char == '0':
            string_input[position] = 'x'
            return self.q3(string_input, position + 1)
        elif char == '1':
            string_input[position] = 'y'
            return self.q10(string_input, position + 1)
        elif char == ' ':
            return self.q26(string_input, position + 1)
        else:
            return None
        
    def q3(self, string_input : list, position : int):
        self.print('q3', string_input, position)
        if position >= len(string_input):
            return None
    
        char = string_input[position]

        if char == '0' or char == '1' or char == '+' or char == 'x' or char == 'y' or char == 'a' or char == 'b':
            return self.q3(string_input, position + 1)
        elif char == '=':
            return self.q4(string_input, position - 1)
        else:
            return None
        
    def q4(self, string_input : list, position : int):
        self.print('q4', string_input, position)
        if position >= len(string_input):
            return None
    
        char = string_input[position]

        if char == 'a' or char == 'b':
            return self.q4(string_input, position - 1)
        elif char == '0':
            string_input[position] = 'a'
            return self.q5(string_input, position + 1)
        elif char == '1':
            string_input[position] = 'b'
            return self.q8(string_input, position + 1)
        else:
            return None
        
    def q5(self, string_input : list, position : int):
        self.print('q5', string_input, position)
        if position >= len(string_input):
            return None
    
        char = string_input[position]

        if char == 'a' or char == 'b':
            return self.q5(string_input, position + 1)
        elif char == '=':
            return self.q6(string_input, position + 1)
        else:
            return None
        
    def q6(self, string_input : list, position : int):
        self.print('q6', string_input, position)
        if position >= len(string_input):
            return None
    
        char = string_input[position]

        if char == '0' or char == '1':
            return self.q6(string_input, position + 1)
        elif char == ' ':
            string_input[position] = '0'
            return self.q7(string_input, position - 1)
        else:
            return None
        
    def q7(self, string_input : list, position : int):
        self.print('q7', string_input, position)
        if position >= len(string_input):
            return None
    
        char = string_input[position]

        if char == '0' or char == '1' or char == 'a' or char == 'b' or char == '=' or char == '+':
            return self.q7(string_input, position - 1)
        elif char == 'x' or char == 'y':
            return self.q1(string_input, position + 1)
        else:
            return None
        
    def q8(self, string_input : list, position : int):
        self.print('q8', string_input, position)
        if position >= len(string_input):
            return None
    
        char = string_input[position]
        
        if char == 'a' or char == 'b':
            return self.q8(string_input, position + 1)
        elif char == '=':
            return self.q9(string_input, position + 1)
        else:
            return None
        
    def q9(self, string_input : list, position : int):
        self.print('q9', string_input, position)
        if position >= len(string_input):
            return None
    
        char = string_input[position]

        if char == '0' or char == '1':
            return self.q9(string_input, position + 1)
        elif char == ' ':
            string_input[position] = '1'
            return self.q7(string_input, position - 1)
        
    def q10(self, string_input : list, position : int):
        self.print('q10', string_input, position)
        if position >= len(string_input):
            return None
    
        char = string_input[position]

        if char == '0' or char == '1' or char == '+' or char == 'x' or char == 'y' or char == 'a' or char == 'b':
            return self.q10(string_input, position + 1)
        elif char == '=':
            return self.q11(string_input, position - 1)
        else:
            return None
        
    def q11(self, string_input : list, position : int):
        self.print('q11', string_input, position)
        if position >= len(string_input):
            return None
    
        char = string_input[position]

        if char == 'a' or char == 'b':
            return self.q11(string_input, position - 1)
        elif char == '0':
            string_input[position] = 'a'
            return self.q12(string_input, position + 1)
        elif char == '1':
            string_input[position] = 'b'
            return self.q14(string_input, position + 1)
        else:
            return None
        
    def q12(self, string_input : list, position : int):
        self.print('q12', string_input, position)
        if position >= len(string_input):
            return None
    
        char = string_input[position]

        if char == 'a' or char == 'b':
            return self.q12(string_input, position + 1)
        elif char == '=':
            return self.q13(string_input, position + 1)
        else:
            return None
    
    def q13(self, string_input : list, position : int):
        self.print('q13', string_input, position)
        if position >= len(string_input):
            return None
    
        char = string_input[position]

        if char == '0' or char == '1':
            return self.q13(string_input, position + 1)
        elif char == ' ':
            string_input[position] = '1'
            return self.q7(string_input, position - 1)
        else:
            return None
        
    def q14(self, string_input : list, position : int):
        self.print('q14', string_input, position)
        if position >= len(string_input):
            return None
    
        char = string_input[position]

        if char == 'x' or char == 'y':
            return self.q14(string_input, position + 1)
        elif char == '=':
            return self.q15(string_input, position + 1)
        else:
            return None
        
    def q15(self, string_input : list, position : int):
        self.print('q15', string_input, position)
        if position >= len(string_input):
            return None
    
        char = string_input[position]

        if char == '0' or char == '1':
            return self.q15(string_input, position + 1)
        elif char == ' ':
            string_input[position] = '0'
            return self.q16(string_input, position - 1)
        else:
            return None
        
    def q16(self, string_input : list, position : int):
        self.print('q16', string_input, position)
        if position >= len(string_input):
            return None
    
        char = string_input[position]

        if char == '0' or char == '1' or char == 'a' or char == 'b' or char == '=' or char == '+':
            return self.q16(string_input, position - 1)
        elif char == 'x' or char == 'y':
            return self.q17(string_input, position + 1)
        else:
            return None
        
    def q17(self, string_input : list, position : int):
        self.print('q17', string_input, position)
        if position >= len(string_input):
            return None
    
        char = string_input[position]

        if char == '0' or char == '1':
            return self.q17(string_input, position + 1)
        elif char == '+':
            return self.q18(string_input, position - 1)
        else:
            return None
        
    def q18(self, string_input : list, position : int):
        self.print('q18', string_input, position)
        if position >= len(string_input):
            return None
    
        char = string_input[position]

        if char == 'x' or char == 'y':
            return self.q18(string_input, position - 1)
        elif char == '0':
            string_input[position] = 'x'
            return self.q19(string_input, position + 1)
        elif char == '1':
            string_input[position] = 'y'
            return self.q21(string_input, position + 1)
        elif char == ' ':
            return self.q25(string_input, position + 1)
        else:
            return None
        
    def q19(self, string_input : list, position : int):
        self.print('q19', string_input, position)
        if position >= len(string_input):
            return None
    
        char = string_input[position]

        if char == '0' or char == '1':
            return self.q19(string_input, position + 1)
        elif char == '=':
            return self.q20(string_input, position - 1)
        else:
            return None
        
    def q20(self, string_input : list, position : int):
        self.print('q20', string_input, position)
        if position >= len(string_input):
            return None
    
        char = string_input[position]

        if char == 'a' or char == 'b':
            return self.q20(string_input, position - 1)
        elif char == '0':
            string_input[position] = 'a'
            return self.q8(string_input, position + 1)
        elif char == '1':
            string_input[position] = 'b'
            return self.q5(string_input, position + 1)
        else:
            return None
        
    def q21(self, string_input : list, position : int):
        self.print('q21', string_input, position)
        if position >= len(string_input):
            return None
    
        char = string_input[position]

        if char == 'x' or char == 'y' or char == '+' or char == '1' or char == '0' or char == 'a' or char =='b':
            return self.q21(string_input, position + 1)
        elif char == '=':
            return self.q22(string_input, position - 1)
        else:
            return None
        
    def q22(self, string_input : list, position : int):
        self.print('q22', string_input, position)
        if position >= len(string_input):
            return None
    
        char = string_input[position]

        if char == 'a' or char == 'b':
            return self.q22(string_input, position - 1)
        elif char == '0':
            string_input[position] = 'a'
            return self.q14(string_input, position + 1)
        elif char == '1':
            string_input[position] = 'b'
            return self.q23(string_input, position + 1)
        else:
            return None
        
    def q23(self, string_input : list, position : int):
        self.print('q23', string_input, position)
        if position >= len(string_input):
            return None
    
        char = string_input[position]

        if char == 'a' or char == 'b':
            return self.q23(string_input, position + 1)
        elif char == '=':
            return self.q24(string_input, position + 1)
        else:
            return None
        
    def q24(self, string_input : list, position : int):
        self.print('q24', string_input, position)
        if position >= len(string_input):
            return None
    
        char = string_input[position]

        if char == '0' or char == '1':
            return self.q24(string_input, position + 1)
        elif char == ' ':
            string_input[position] = '1'
            return self.q16(string_input, position - 1)
        else:
            return None
        
    def q25(self, string_input : list, position : int):
        self.print('q25', string_input, position)
        if position >= len(string_input):
            return None
    
        char = string_input[position]

        if char == 'x' or char == 'a':
            string_input[position] = '0'
            return self.q25(string_input, position + 1)
        elif char == 'y' or char == 'b':
            string_input[position] = '1'
            return self.q25(string_input, position + 1)
        elif char == '+' or char == '=':
            return self.q25(string_input, position + 1)
        elif char == '0' or char == '1':
            return self.q25(string_input, position + 1)
        elif char == ' ':
            string_input[position] = '1'
            return string_input
        else:
            return None
        
    def q26(self, string_input : list, position : int):
        self.print('q26', string_input, position)
        if position >= len(string_input):
            return None
    
        char = string_input[position]

        if char == 'x' or char == 'a':
            string_input[position] = '0'
            return self.q26(string_input, position + 1)
        elif char == 'y' or char == 'b':
            string_input[position] = '1'
            return self.q26(string_input, position + 1)
        elif char == '+' or char == '=':
            return self.q26(string_input, position + 1)
        elif char == '0' or char == '1':
            return self.q26(string_input, position + 1)
        elif char == ' ':
            return string_input
        else:
            return None