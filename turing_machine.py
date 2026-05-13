from abc import ABC, abstractmethod

class turing_machine(ABC):
    language = ['0', '1', 'x', 'y', 'a', 'b', '+', '=', ' ']
        
    @abstractmethod
    def recognize(self):
        pass