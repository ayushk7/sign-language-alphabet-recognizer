from enum import Enum, auto
import logging
last_sequence: str = ""

program_stack: list[str] = []

my_program: str = ""

variables = {}

program_string = ""


# # class BetaString(str):
# #     def __init__(self) -> None:
# #         super().__init__()
    
# #     def add(self, ch):
# #         self += ch
    



class CState(Enum):
    EMPTY=0
    PRINT=1
    FOR_LOOP=2
    IF=3
    ELIF=4
    ELSE=5
    DECLARE=6


class SState(Enum):
    BRACKET_OPEN=0
    STRING_OPEN=1

# class TypeValues(Enum):
#     NUMBER = 0
#     QUOTED_STRING = 1
#     STRING = 2
#     EXPRESSION = 3
#     BLOCK = 4


# class LDeclaration(object):
#     def get_parts(self):
#         yield 'var'
#         yield TypeValues.STRING
#         yield ' = '
#         yield TypeValues.EXPRESSION

# class LExpression(object):
#     def get_parts(self):
#         yield


# class LPrint(object):
#     def get_parts(self):
#         yield 'print('
#         yield TypeValues.EXPRESSION
#         yield ');\n'
    
#     def get_input_counts(self):
#         return 1

#     def get_default_values(self):
#         yield "Hello World"
    
# class LIfBlock(object):
#     def get_parts(self):
#         yield 'if('
#         yield TypeValues.EXPRESSION
#         yield '){\n'
#         yield TypeValues.BLOCK
#         yield '}\n'
#         yield 'else{'
#         yield TypeValues.BLOCK
#         yield '}\n'

#     def get_input_counts(self):
#         return 3
    
#     def get_default_values(self):
#         yield 'true'
#         yield ''
#         yield ''

# class LWhileLoop(object):
#     def get_parts(self):
#         yield 'while('
#         yield TypeValues.EXPRESSION
#         yield '){\n'
#         yield TypeValues.BLOCK
#         yield '}\n'

#     def get_input_counts(self):
#         return 3
    
#     def get_default_values(self):
#         yield 'true'
#         yield ''


# construct_state = CState.EMPTY

import logging



def do_program(sequence: str):
    global construct_state, last_sequence, my_program, program_string
    if len(sequence) > len(last_sequence):
        last_sequence = sequence
        curr_char = sequence[-1].upper()
        print(f'current_char is:{curr_char!r}')
    else:
        return

    if curr_char == ' ':
        if len(program_stack):
            if program_stack[-1] == SState.BRACKET_OPEN:
                program_stack.pop()
                my_program += '}\n'
            elif program_stack[-1] == SState.STRING_OPEN:
                program_stack.pop()
                if construct_state == CState.DECLARE:
                    my_program += f'{program_string}\n'
                else:
                    my_program += f'{program_string!r};'
    
    elif len(program_stack) and program_stack[-1] == SState.STRING_OPEN:
        program_string += curr_char

    elif curr_char == 'P':
        # Print Node
        # inp = '"hello world"'
        program_stack.append(SState.STRING_OPEN)
        my_program += f'print();\n'
    
    elif curr_char == 'I':
        inp = 'true'
        # program_stack.append('if(')
        my_program += f'if({inp}){{\n'
        program_stack.append(SState.BRACKET_OPEN)
    
    elif curr_char == 'E':
        my_program += 'else{\n'
        program_stack.append(SState.BRACKET_OPEN)

    elif curr_char == 'L':
        inp = 'true'
        my_program += f'while({inp}){{\n'
        program_stack.append(SState.BRACKET_OPEN)


    
    elif curr_char == 'D':
         my_program += 'var '
         program_stack.append(SState.STRING_OPEN)
         construct_state = CState.DECLARE
         program_string = ""

    else:
        
        logging.warning(f'NO construct mapping {curr_char!r}')
    
    print(my_program)


# def test():
#     seq = 'Dhello LIPI EP E   '
#     b_seq = ''
#     for ch in seq:
#         b_seq += ch
#         do_program(b_seq)

# test()

# from enum import Enum

# class Constructs(Enum):
#     START = 1
#     LOOP = 2
#     IF_ELSE = 3
#     PRINT = 4
#     DECLARATION = 5

# class ValueTypes(Enum):
#     NUMBER = 6
#     EXPRESSION = 7
#     STRING = 8

# class Modes(Enum):
#     BEGIN = 0
#     EXPRESSION = 1
#     STRING = 2
#     NUMBER = 3
#     IF_ELSE = 4


# class Program(object):
#     def __init__(self) -> None:
#         self.stack = [Modes.BEGIN]
#         self.program = []
#         # \#     if len(sequence) > len(last_sequence):
# #         last_sequence = sequence
# #         curr_char = sequence[-1].upper()
# #         print(f'current_char is:{curr_char!r}')
#         self.last_seq = ''
#         self.current_construct = Constructs.START

#         self.string_mode_string = ''
#         self.expression_mode_expression = ''
#         self.number_mode_number = ''

    
#     def main(self, seq):
#         if len(seq) > len(self.last_seq):
#             self.last_seq = seq
#             self.curr_char = seq[-1].lower()
#         else:
#             return
        
#         if self.curr_char == ' ':
#             mode = self.stack.pop()
#             if mode == Modes.STRING:
#                 self.program.append(self.string_mode_string)
#                 self.string_mode_string = ''
#             elif mode == Modes.NUMBER:
#                 self.program.append(self.number_mode_number)
#                 self.number_mode_number = ''
#             elif mode == Modes.IF_ELSE:
#                 self.program.append('}\n')

#         if len(self.stack):
#             if self.stack[-1] == Modes.EXPRESSION: # Expression Mode
#                 self.expression_evaluator()
#             elif self.stack[-1] == Modes.NUMBER: # Number Mode
#                 self.number_evaluator()
#             elif self.stack[-1] == Modes.STRING:  # String Mode
#                 self.string_evaluator()
#             elif self.stack[-1] == Modes.IF_ELSE: # If-else mode
#                 self.if_else_evaluator()
#             elif self.stack[-1] == Modes.BEGIN: # Begin Mode
#                 self.next_mode_evaluator()


    
#     def expression_evaluator(self):
#         ...
    
#     def number_evaluator(self):
#         ...
    
#     def string_evaluator(self):
#         self.string_mode_string += self.curr_char
    
#     def next_mode_evaluator(self):
#         if self.curr_char == 'I':
#             self.stack.append(Modes.IF_ELSE)
#         elif self.curr_char == 'E':
#             self.stack.append(Modes.EXPRESSION)
#         elif self.curr_char == 'N':
#             self.stack.append(Modes.NUMBER)
#         elif self.curr_char == 'S':
#             self.stack.append(Modes.STRING)
    
#     def if_else_evaluator(self):
#         self.program.append('if(')
#         self.stack.append(Modes.EXPRESSION)

_exhausted = object()

from enum import Enum

class GenModes(Enum):
    IF_ELSE_GENERATOR = 0
    BEGIN_GENERATOR = 1
    NUMBER_GENERATOR = 2


SPACE = ' '

def program_generator(attr_value):
    def decorator(generator):
        def wrapper(*args, **kwargs):
            gen = generator(*args, **kwargs)
            # setattr(gen, 'mode', attr_value)
            gen.mode = attr_value
            return gen
        return wrapper
    return decorator



class Program(object):
    def __init__(self) -> None:
        self.curr_char = None
        self.generator_stack = [self.begin_generator()]
        self.program = []
        self.last_seq = ''

    def main(self, seq: str):
        if len(seq) > len(self.last_seq):
            self.last_seq = seq
            self.curr_char = seq[-1].upper()
        else:
            return
        
        # for value in self.generator_stack[-1]():
        #     if value
        #     self.program.append(value)
        if len(self.generator_stack):
            value = next(self.generator_stack[-1], _exhausted)
            # print(self.generator_stack[-1].mode)
            if value is not _exhausted:
                # print(self.generator_stack[-1])
                # print('_SPACE_' if self.curr_char == SPACE else self.curr_char)
                # print(self.generator_stack.__len__())
                self.program.append(value)
            else:
                self.generator_stack.pop()

    # @program_generator(GenModes.NUMBER_GENERATOR)
    def number_generator(self):
        while self.curr_char != SPACE:
            yield self.curr_char
        self.generator_stack.pop()

    
    # @program_generator(GenModes.IF_ELSE_GENERATOR)
    def if_else_generator(self):
        self.generator_stack.append(self.number_generator())
        yield 'if('
        self.generator_stack.append(self.begin_generator())
        yield '){\n'
        yield '}\n'
    
    # @program_generator(GenModes.BEGIN_GENERATOR)
    def begin_generator(self):
        if self.curr_char == 'I':
            self.generator_stack.append(self.if_else_generator())
        elif self.curr_char == 'N':
            self.generator_stack.append(self.number_generator())
        yield '// Begin Generator\n'

# pr = Program()

# ss = 'IN456'
# ch = ''
# for ik in ss:
#     ch += ik
#     pr.main(ch)
#     print("".join(pr.program))