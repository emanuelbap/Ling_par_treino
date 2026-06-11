import sys

# Preciso ter a Class Token para representar as unidades de entrada já identificadas.
class Token:
    '''
    The class token don't break anything, but, just, she only represents'''
    INT = 'INT'
    PLUS = 'PLUS'
    MINUS = "MINUS"
    EOF = 'EOF' # whitespace
    MULT = 'MULT'
    DIV = 'DIV'
    OPEN_PAR = 'OPEN_PAR'
    CLOSE_PAR = 'CLOSE_PAR'
    IDENTIFIER = "IDENTIFIER"
    ASSIGN = "ASSIGN"
    SEMICOLON = "SEMICOLON"
    PRINT = "PRINT"
    AND = "AND"
    OR = "OR"
    NOT = "NOT"

    EQ = "EQ"
    GT = "GT"
    LT = "LT"

    IF = "IF"
    ELSE = "ELSE"
    WHILE = "WHILE"

    READ = "READ"

    OPEN_BRA = "OPEN_BRA"
    CLOSE_BRA = "CLOSE_BRA"

    LET = "LET"
    MUT = "MUT"
    BOOL = "BOOL"
    STR = "STR"
    TYPE = "TYPE"
    COLON = "COLON"
    FUNC = "FUNC"
    RETURN = "RETURN"
    COMMA = "COMMA"
    ARROW = "ARROW"

    def __init__(self, type, value):
        self.type = type
        self.value = value



# I need to creat the Prepro class
class Prepro:
    @staticmethod
    def filter(source):
        # In this method, we'll remove the comments.
        result = ""
        i = 0

        while i < len(source):
            if i + 1 < len(source) and source[i] == "/" and source[i+1] == "/":
                while i < len(source) and source[i] != "\n":
                    i += 1

            else:
                result += source[i]
                i += 1
        
        return result



class Lexer:
    '''I need make the class Lexer for break the code in tokens'''
    def __init__(self, source):
        self.source = source
        self.position = 0
        self.next = None
        
    '''Now, I have make the function selectNext to separate into tokens'''
    def selectNext(self):
        # ignore whitespaces
        while self.position < len(self.source) and self.source[self.position].isspace():
            self.position += 1

        # break
        if self.position >= len(self.source):
            self.next = Token(Token.EOF, '')
            return

        current_char = self.source[self.position]

        # number (INT)
        '''I am going to use a Python function that determines if a char is an INT number'''
        if current_char.isdigit():
            number = ''

            while self.position < len(self.source) and self.source[self.position].isdigit():
                number += self.source[self.position]
                self.position += 1
            
            # Now, I am going classifying the number into tokens
            self.next = Token(Token.INT, int(number))
            return
        
        # Operators
        if current_char == '+':
            self.next = Token(Token.PLUS, '+')
            self.position += 1
            return
        
        if (current_char == '-' and self.position + 1 < len(self.source) and self.source[self.position + 1] == '>'):
            self.next = Token(Token.ARROW, "->")
            self.position += 2
            return
        
        if current_char == '-':
            self.next = Token(Token.MINUS, '-')
            self.position += 1 
            return
        
        if current_char == '*':
            self.next = Token(Token.MULT, '*')
            self.position += 1
            return
        
        if current_char == '/':
            self.next = Token(Token.DIV, '/')
            self.position += 1
            return
        
        if current_char == '(':
            self.next = Token(Token.OPEN_PAR, '(')
            self.position += 1
            return
        
        if current_char == ')':
            self.next = Token(Token.CLOSE_PAR, ')')
            self.position += 1
            return
        
        if (current_char == '=' and self.position + 1 < len(self.source) and self.source[self.position + 1] == '='):
            self.next = Token(Token.EQ, "==")
            self.position += 2
            return
        
        if current_char == '=':
            self.next = Token(Token.ASSIGN, '=')
            self.position += 1
            return
        
        if current_char == ';':
            self.next = Token(Token.SEMICOLON, ';')
            self.position += 1
            return
        
        if current_char == '{':
            self.next = Token(Token.OPEN_BRA, "{")
            self.position += 1
            return 
        
        if current_char == '}':
            self.next = Token(Token.CLOSE_BRA, "}")
            self.position += 1
            return
        
        if current_char == '<':
            self.next = Token(Token.LT, "<")
            self.position += 1
            return
        
        if current_char == '>':
            self.next = Token(Token.GT, ">")
            self.position += 1
            return
        
        if (current_char == '&' and self.position + 1 < len(self.source) and self.source[self.position + 1] == '&'):
            self.next = Token(Token.AND, "&&")
            self.position += 2
            return

        if (current_char == '|' and self.position + 1 < len(self.source) and self.source[self.position + 1] == '|'):
            self.next = Token(Token.OR, "||")
            self.position += 2
            return
        
        if current_char == "!":
            self.next = Token(Token.NOT, "!")
            self.position += 1
            return
        
        if current_char == ":":
            self.next = Token(Token.COLON, ":")
            self.position += 1
            return
        
        if current_char == ",":
            self.next = Token(Token.COMMA, ",")
            self.position += 1
            return
        
        if current_char == '"':
            self.position += 1

            string = ""

            while self.position < len(self.source) and self.source[self.position] != '"':
                string += self.source[self.position]
                self.position += 1

            self.position += 1

            self.next = Token(
                Token.STR,
                string
            )

            return
        


        
        # I need to make the lexer understand the identifiers.
        if current_char.isalpha():
            identifier = ""

            while self.position < len(self.source) and (self.source[self.position].isalnum() or self.source[self.position] == "_"):
                identifier += self.source[self.position]
                self.position += 1

            # Now, the identifier can be the "println"
            if identifier == "println" and self.position < len(self.source) and self.source[self.position] == "!":
                self.position += 1
                self.next = Token(Token.PRINT, "println!")
                return 
            
            if identifier == "if":
                self.next = Token(Token.IF, "if")
                return 
            
            if identifier == "else":
                self.next = Token(Token.ELSE, "else")
                return
            
            if identifier == "while":
                self.next = Token(Token.WHILE, "while")
                return
            
            if identifier == "fn":
                self.next = Token(Token.FUNC, "fn")
                return
            
            if identifier == "return":
                self.next = Token(Token.RETURN, "return")
                return
            
            if identifier == "let":
                self.next = Token(Token.LET, "let")
                return
            
            if identifier == "mut":
                self.next = Token(Token.MUT, "mut")
                return
            
            if identifier == "true":
                self.next = Token(Token.BOOL, True)
                return
            
            if identifier == "false":
                self.next = Token(Token.BOOL, False)
                return
            
            if identifier == "i32":
                self.next = Token(Token.TYPE, "i32")
                return
            
            if identifier == "str":
                self.next = Token(Token.TYPE, "str")
                return
            
            if identifier == "bool":
                self.next = Token(Token.TYPE, "bool")
                return
        
            
            if ((identifier == "scanln" or identifier == "readln") and self.position < len(self.source) and self.source[self.position] == "!"):
                self.position += 1 
                self.next = Token(Token.READ, identifier + "!")
                return
            

            
            self.next = Token(Token.IDENTIFIER, identifier)
            return

        # Lexical error
        raise Exception(f"[Lexer] invalid charcter: {current_char}")
    

## I'll create the AST classes
class Code:
    instructions = []

    @staticmethod
    def append(code):
        Code.instructions.append(code)

    @staticmethod
    def dump(filename):
        with open(filename, "w") as file:
            file.write(
"""section .data
  format_out: db "%d", 10, 0 ; format do printf
  format_in: db "%d", 0 ; format do scanf
  scan_int: dd 0; 32-bits integer

section .text
  extern printf ; usar _printf para Windows
  extern scanf ; usar _scanf para Windows
  ; extern _ExitProcess@4 ; usar para Windows
  global _start ; inicio do programa

_start:
  push ebp ; guarda o EBP
  mov ebp, esp ; zera a pilha

  ; aqui comeca o codigo gerado:

"""
            )

            file.write("\n".join(Code.instructions))

            file.write(
"""

  ; aqui termina o codigo gerado

  mov esp, ebp ; reestabelece a pilha
  pop ebp

  ; chamada da interrupcao de saida (Linux)
  mov eax, 1
  xor ebx, ebx
  int 0x80
  ; Para Windows:
  ; push dword 0
  ; call _ExitProcess@4
"""
            )


class Node:
    id = 0

    @staticmethod
    def newId():
        Node.id += 1
        return Node.id

    def __init__(self, value, children):
        self.value = value
        self.children = children
        self.id = Node.newId()

    def evaluate(self, st):
        pass

    def generate(self, st):
        pass

class Variable:
    def __init__(self, value, type, shift=None, is_function=False):
        self.value = value
        self.type = type
        self.shift = shift
        self.is_function = is_function


class IntVal(Node):
    def evaluate(self, st):
        return Variable(
            self.value,
            "i32"
        )

    def generate(self, st):
        Code.append(
            f"  mov eax, {self.value}"
        )

        return Variable(
            None,
            "i32"
        )
    
class BoolVal(Node):
    def evaluate(self, st):
        return Variable(
            self.value,
            "bool"
        )

    def generate(self, st):
        if self.value:
            value = 1
        else:
            value = 0

        Code.append(
            f"  mov eax, {value}"
        )

        return Variable(
            None,
            "bool"
        )
    
class StringVal(Node):
    def evaluate(self, st):
        return Variable(
            self.value,
            "str"
        )

    def generate(self, st):
        raise Exception(
            "[Code] String does not generate assembly in this roteiro"
        )

class UnOp(Node):
    # This class is for unary operations
    def evaluate(self, st):
        child = self.children[0].evaluate(st)

        if self.value == '+':
            return Variable(
                child.value,
                child.type
            )

        if self.value == '-':
            if child.type != "i32":
                raise Exception(
                    "[Semantic] Invalid types"
                )
            
            return Variable(
                -child.value,
                "i32"
            )

        if self.value == "!":
            if child.type != "bool":
                raise Exception(
                    "[Semantic] Invalid types"
                )
            
            return Variable(
                not child.value,
                "bool"
            )

    def generate(self, st):
        child = self.children[0].generate(st)

        if self.value == '+':
            return Variable(
                None,
                child.type
            )

        if self.value == '-':
            if child.type != "i32":
                raise Exception(
                    "[Semantic] Invalid types"
                )
            
            Code.append(
                "  neg eax"
            )

            return Variable(
                None,
                "i32"
            )

        if self.value == "!":
            if child.type != "bool":
                raise Exception(
                    "[Semantic] Invalid types"
                )
            
            Code.append(
                "  cmp eax, 0"
            )
            Code.append(
                "  mov eax, 0"
            )
            Code.append(
                "  mov ecx, 1"
            )
            Code.append(
                "  cmove eax, ecx"
            )

            return Variable(
                None,
                "bool"
            )
        
        
class BinOp(Node):
    # This class is for binary operations (+, -, *, /)
    def evaluate(self, st):
        left = self.children[0].evaluate(st)
        right = self.children[1].evaluate(st)

        if self.value == '+':
            if left.type != "i32" or right.type != "i32":
                raise Exception(
                    "[Semantic] Invalid types"
                )
            
            return Variable(
        left.value + right.value,
        "i32"
    )
        if self.value == '-':
            if left.type != "i32" or right.type != "i32":
                raise Exception(
                    "[Semantic] Invalid types"
                )
            
            return Variable(
        left.value - right.value,
        "i32"
    )
        if self.value == '*':
            if left.type != "i32" or right.type != "i32":
                raise Exception(
                    "[Semantic] Invalid types"
                )
            
            return Variable(
        left.value * right.value,
        "i32"
    )
        if self.value == '/':
            if left.type != "i32" or right.type != "i32":
                raise Exception(
                    "[Semantic] Invalid types"
                )
            
            return Variable(
        left.value // right.value,
        "i32"
    )
        
        if self.value == '<':
            if left.type != "i32" or right.type != "i32":
                raise Exception(
                    "[Semantic] Invalid types"
                )
            
            return Variable(
        left.value < right.value,
        "bool"
    )
        
        if self.value == '>':
            if left.type != "i32" or right.type != "i32":
                raise Exception(
                    "[Semantic] Invalid types"
                )
            
            return Variable(
        left.value > right.value,
        "bool"
    )
        
        if self.value == "==":
            if left.type != right.type:
                raise Exception(
                    "[Semantic] Invalid types"
                )
            return Variable(
        left.value == right.value,
        "bool"
    )
        
        if self.value == "&&":
            if left.type != "bool" or right.type != "bool":
                raise Exception(
                    "[Semantic] Invalid types"
                )
            
            return Variable(
        left.value and right.value,
        "bool"
    )
        
        if self.value == "||":
            if left.type != "bool" or right.type != "bool":
                raise Exception(
                    "[Semantic] Invalid types"
                )
            
            return Variable(
        left.value or right.value,
        "bool"
    )
        

        raise Exception(f"[Semantic] Unknown operator {self.value}")

    def generate(self, st):
        left = self.children[0].generate(st)

        Code.append(
            "  push eax"
        )

        right = self.children[1].generate(st)

        Code.append(
            "  pop ecx"
        )

        if self.value == '+':
            if left.type != "i32" or right.type != "i32":
                raise Exception(
                    "[Semantic] Invalid types"
                )
            
            Code.append(
                "  add eax, ecx"
            )

            return Variable(
                None,
                "i32"
            )

        if self.value == '-':
            if left.type != "i32" or right.type != "i32":
                raise Exception(
                    "[Semantic] Invalid types"
                )
            
            Code.append(
                "  sub ecx, eax"
            )
            Code.append(
                "  mov eax, ecx"
            )

            return Variable(
                None,
                "i32"
            )

        if self.value == '*':
            if left.type != "i32" or right.type != "i32":
                raise Exception(
                    "[Semantic] Invalid types"
                )
            
            Code.append(
                "  imul ecx"
            )

            return Variable(
                None,
                "i32"
            )

        if self.value == '/':
            if left.type != "i32" or right.type != "i32":
                raise Exception(
                    "[Semantic] Invalid types"
                )
            
            Code.append(
                "  push eax"
            )
            Code.append(
                "  mov eax, ecx"
            )
            Code.append(
                "  pop ecx"
            )
            Code.append(
                "  cdq"
            )
            Code.append(
                "  idiv ecx"
            )

            return Variable(
                None,
                "i32"
            )
        
        if self.value == '<':
            if left.type != "i32" or right.type != "i32":
                raise Exception(
                    "[Semantic] Invalid types"
                )
            
            Code.append(
                "  cmp ecx, eax"
            )
            Code.append(
                "  mov eax, 0"
            )
            Code.append(
                "  mov ecx, 1"
            )
            Code.append(
                "  cmovl eax, ecx"
            )

            return Variable(
                None,
                "bool"
            )
        
        if self.value == '>':
            if left.type != "i32" or right.type != "i32":
                raise Exception(
                    "[Semantic] Invalid types"
                )
            
            Code.append(
                "  cmp ecx, eax"
            )
            Code.append(
                "  mov eax, 0"
            )
            Code.append(
                "  mov ecx, 1"
            )
            Code.append(
                "  cmovg eax, ecx"
            )

            return Variable(
                None,
                "bool"
            )
        
        if self.value == "==":
            if left.type != right.type:
                raise Exception(
                    "[Semantic] Invalid types"
                )
            
            Code.append(
                "  cmp ecx, eax"
            )
            Code.append(
                "  mov eax, 0"
            )
            Code.append(
                "  mov ecx, 1"
            )
            Code.append(
                "  cmove eax, ecx"
            )

            return Variable(
                None,
                "bool"
            )
        
        if self.value == "&&":
            if left.type != "bool" or right.type != "bool":
                raise Exception(
                    "[Semantic] Invalid types"
                )
            
            Code.append(
                "  and eax, ecx"
            )

            return Variable(
                None,
                "bool"
            )
        
        if self.value == "||":
            if left.type != "bool" or right.type != "bool":
                raise Exception(
                    "[Semantic] Invalid types"
                )
            
            Code.append(
                "  or eax, ecx"
            )

            return Variable(
                None,
                "bool"
            )
        

        raise Exception(f"[Semantic] Unknown operator {self.value}")
    

class If(Node):
    def evaluate(self, st):
        condition = self.children[0].evaluate(st)

        if condition.type != "bool":
            raise Exception(
                "[Semantic] Invalid types"
            )

        if condition.value:
            result = self.children[1].evaluate(st)

            if isinstance(self.children[1], Return):
                return result
            
            if isinstance(self.children[1], If) or isinstance(self.children[1], While) or isinstance(self.children[1], Block):
                if result is not None:
                    return result

        elif len(self.children) == 3:
            result = self.children[2].evaluate(st)

            if isinstance(self.children[2], Return):
                return result
            
            if isinstance(self.children[2], If) or isinstance(self.children[2], While) or isinstance(self.children[2], Block):
                if result is not None:
                    return result

    def generate(self, st):
        condition = self.children[0].generate(st)

        if condition.type != "bool":
            raise Exception(
                "[Semantic] Invalid types"
            )

        Code.append(
            "  cmp eax, 0"
        )

        if len(self.children) == 3:
            Code.append(
                f"  je else_{self.id}"
            )

            self.children[1].generate(st)

            Code.append(
                f"  jmp exit_{self.id}"
            )
            Code.append(
                f"else_{self.id}:"
            )

            self.children[2].generate(st)

            Code.append(
                f"exit_{self.id}:"
            )
        
        else:
            Code.append(
                f"  je exit_{self.id}"
            )

            self.children[1].generate(st)

            Code.append(
                f"exit_{self.id}:"
            )


class While(Node):

    def evaluate(self, st):

        condition = self.children[0].evaluate(st)

        if condition.type != "bool":
            raise Exception(
                "[Semantic] Invalid types"
            )

        while condition.value:
            result = self.children[1].evaluate(st)

            if isinstance(self.children[1], Return):
                return result
            
            if isinstance(self.children[1], If) or isinstance(self.children[1], While) or isinstance(self.children[1], Block):
                if result is not None:
                    return result

            condition = self.children[0].evaluate(st)

            if condition.type != "bool":
                raise Exception(
                    "[Semantic] Invalid types"
                )

    def generate(self, st):
        Code.append(
            f"loop_{self.id}:"
        )

        condition = self.children[0].generate(st)

        if condition.type != "bool":
            raise Exception(
                "[Semantic] Invalid types"
            )

        Code.append(
            "  cmp eax, 0"
        )
        Code.append(
            f"  je exit_{self.id}"
        )

        self.children[1].generate(st)

        Code.append(
            f"  jmp loop_{self.id}"
        )
        Code.append(
            f"exit_{self.id}:"
        )

class VarDec(Node):
    def evaluate(self, st):
        identifier = self.children[0].value

        variable = Variable(
            None,
            self.value
        )

        st.create_variable(
            identifier,
            variable
        )

        if len(self.children) == 2:

            value = self.children[1].evaluate(st)
            if value.type != self.value:
                raise Exception(
                    "[Semantic] Type mismatch"
                )

            st.set(
                identifier,
                value
            )

    def generate(self, st):
        identifier = self.children[0].value

        if self.value == "str":
            raise Exception(
                "[Code] String does not generate assembly in this roteiro"
            )

        variable = Variable(
            None,
            self.value
        )

        st.create_variable(
            identifier,
            variable
        )

        Code.append(
            f"  sub esp, 4 ; var {identifier} {self.value} [EBP-{variable.shift}]"
        )

        if len(self.children) == 2:

            value = self.children[1].generate(st)
            if value.type != self.value:
                raise Exception(
                    "[Semantic] Type mismatch"
                )

            st.set(
                identifier,
                value
            )

            Code.append(
                f"  mov [ebp-{variable.shift}], eax ; {identifier} ="
            )


class SymbolTable:
    def __init__(self, parent=None):
        self.table = {}
        self.parent = parent

        if parent:
            self.offset = parent.offset
        else:
            self.offset = 0

    def get_root(self):
        root = self

        while root.parent:
            root = root.parent
        
        return root

    def get(self, name):
        if name not in self.table:
            if self.parent is not None:
                return self.parent.get(name)
            raise Exception(f"[Semantic] Variable {name} not defined")
    
        return self.table[name]

    def set(self, name, value):
        if name not in self.table:
            if self.parent is not None:
                self.parent.set(name, value)
                return
            raise Exception(
                    f"[Semantic] Variable {name} not declared")

        if self.table[name].is_function:
            raise Exception(
                "[Semantic] Function used as variable"
            )

        self.table[name] = Variable(
            value.value,
            value.type,
            self.table[name].shift,
            self.table[name].is_function
        )

    def create_variable(self, name, variable):
        if name in self.table:
            raise Exception(
            f"[Semantic] Variable {name} already exists"
        )

        if not variable.is_function:
            root = self.get_root()
            root.offset += 4
            self.offset = root.offset
            variable.shift = root.offset

        self.table[name] = variable

class Identifier(Node):
    def evaluate(self, st):
        variable = st.get(self.value)

        if variable.is_function:
            raise Exception(
                "[Semantic] Function used as variable"
            )

        return variable

    def generate(self, st):
        variable = st.get(self.value)

        if variable.is_function:
            raise Exception(
                "[Semantic] Function used as variable"
            )

        Code.append(
            f"  mov eax, [ebp-{variable.shift}] ; {self.value}"
        )

        return Variable(
            None,
            variable.type,
            variable.shift
        )

class Assignment(Node):
    def evaluate(self, st):
        var_name = self.children[0].value
        value = self.children[1].evaluate(st)

        current = st.get(var_name)

        if current.is_function:
            raise Exception(
                "[Semantic] Function used as variable"
            )

        if current.type != value.type:
            raise Exception(
                "[Semantic] Type mismatch"
            )

        st.set(var_name, value)

    def generate(self, st):
        var_name = self.children[0].value
        value = self.children[1].generate(st)

        current = st.get(var_name)

        if current.is_function:
            raise Exception(
                "[Semantic] Function used as variable"
            )

        if current.type != value.type:
            raise Exception(
                "[Semantic] Type mismatch"
            )

        st.set(var_name, value)

        Code.append(
            f"  mov [ebp-{current.shift}], eax ; {var_name} ="
        )


class Print(Node):
    def evaluate(self, st):
        value = self.children[0].evaluate(st)

        if value.type == "()":
            raise Exception(
                "[Semantic] Invalid types"
            )

        print(value.value)

    def generate(self, st):
        value = self.children[0].generate(st)

        if value.type == "str":
            raise Exception(
                "[Code] String does not generate assembly in this roteiro"
            )

        Code.append(
            "  push eax"
        )
        Code.append(
            "  push format_out"
        )
        Code.append(
            "  call printf"
        )
        Code.append(
            "  add esp, 8"
        )

class Return(Node):
    def evaluate(self, st):
        return self.children[0].evaluate(st)

    def generate(self, st):
        return self.children[0].generate(st)

class Block(Node):
    def evaluate(self, st):
        if self.value == "program":
            local_st = st
        else:
            local_st = SymbolTable(st)

        for child in self.children:
            result = child.evaluate(local_st)

            if isinstance(child, Return):
                return result
            
            if isinstance(child, If) or isinstance(child, While) or isinstance(child, Block):
                if result is not None:
                    return result

    def generate(self, st):
        if self.value == "program":
            local_st = st
        else:
            local_st = SymbolTable(st)

        for child in self.children:
            child.generate(local_st)

class NoOp(Node):
    def evaluate(self, st):
        pass

    def generate(self, st):
        pass

class Read(Node):
    def evaluate(self, st):
        return Variable(
            int(input()),
                "i32")

    def generate(self, st):
        Code.append(
            "  push scan_int"
        )
        Code.append(
            "  push format_in"
        )
        Code.append(
            "  call scanf"
        )
        Code.append(
            "  add esp, 8"
        )
        Code.append(
            "  mov eax, dword [scan_int]"
        )

        return Variable(
            None,
            "i32"
        )

class FuncDec(Node):
    def evaluate(self, st):
        identifier = self.children[0].value

        if identifier == "main":
            if len(self.children[1:-1]) != 0 or self.value != "()":
                raise Exception(
                    "[Semantic] Invalid main"
                )

        variable = Variable(
            self,
            self.value,
            is_function=True
        )

        st.create_variable(
            identifier,
            variable
        )

    def generate(self, st):
        self.evaluate(st)

        raise Exception(
            "[Code] Function generation does not happen in this roteiro"
        )


class FuncCall(Node):
    def evaluate(self, st):
        function = st.get(self.value)

        if not function.is_function:
            raise Exception(
                f"[Semantic] {self.value} is not a function"
            )

        func_dec = function.value
        parameters = func_dec.children[1:-1]
        block = func_dec.children[-1]

        if len(parameters) != len(self.children):
            raise Exception(
                "[Semantic] Wrong number of arguments"
            )

        root_st = st
        while root_st.parent is not None:
            root_st = root_st.parent

        new_st = SymbolTable(root_st)

        for i in range(len(parameters)):
            parameter = parameters[i]
            argument = self.children[i].evaluate(st)
            parameter_name = parameter.children[0].value

            if argument.type != parameter.value:
                raise Exception(
                    "[Semantic] Type mismatch"
                )

            new_st.create_variable(
                parameter_name,
                Variable(
                    None,
                    parameter.value
                )
            )

            new_st.set(
                parameter_name,
                argument
            )

        result = block.evaluate(new_st)

        if func_dec.value == "()":
            if result is not None:
                raise Exception(
                    "[Semantic] Type mismatch"
                )
            
            return Variable(
                None,
                "()"
            )
        
        if result is None:
            raise Exception(
                "[Semantic] Missing return"
            )
        
        if result.type != func_dec.value:
            raise Exception(
                "[Semantic] Type mismatch"
            )
        
        return result

    def generate(self, st):
        raise Exception(
            "[Code] Function generation does not happen in this roteiro"
        )
        


class Parser:
    '''Here, we will consume the tokens from the lexer.
    The expression must being with INT
    store the INT in result to perform the calculation'''
    def __init__(self, lexer):
        self.lexer = lexer
        self.inside_function = 0

    def eat(self, token_type):
        if self.lexer.next.type == token_type:
            self.lexer.selectNext()
        else:
            raise Exception(f"[Parser] Unexpected token {self.lexer.next.type}")
        

    def parseVarDec(self):
        self.eat(Token.LET)
        self.eat(Token.MUT)

        identifier = Identifier(
            self.lexer.next.value,
            []
        )

        self.eat(Token.IDENTIFIER)
        self.eat(Token.COLON)

        var_type = self.lexer.next.value
        self.eat(Token.TYPE)

        if self.lexer.next.type == Token.SEMICOLON:

            self.eat(Token.SEMICOLON)

            return VarDec(
                var_type,
                [
                    identifier
                ]
            )
            
        if self.lexer.next.type == Token.ASSIGN:

            self.eat(Token.ASSIGN)

            expression = self.parseBoolExpression()

            self.eat(Token.SEMICOLON)

            return VarDec(
                var_type,
                [
                    identifier,
                    expression
                ]
            )

        raise Exception(f"[Parser] Unexpected token {self.lexer.next.type}")
    
    def parseFuncCall(self, identifier):
        children = []

        self.eat(Token.OPEN_PAR)

        if self.lexer.next.type != Token.CLOSE_PAR:
            children.append(self.parseBoolExpression())

            while self.lexer.next.type == Token.COMMA:
                self.eat(Token.COMMA)
                children.append(self.parseBoolExpression())

        self.eat(Token.CLOSE_PAR)

        return FuncCall(
            identifier,
            children
        )
    
    def parseFuncDeclaration(self):
        self.eat(Token.FUNC)

        identifier = Identifier(
            self.lexer.next.value,
            []
        )

        self.eat(Token.IDENTIFIER)
        self.eat(Token.OPEN_PAR)

        children = [
            identifier
        ]

        if self.lexer.next.type != Token.CLOSE_PAR:
            parameter = Identifier(
                self.lexer.next.value,
                []
            )

            self.eat(Token.IDENTIFIER)
            self.eat(Token.COLON)

            parameter_type = self.lexer.next.value
            self.eat(Token.TYPE)

            children.append(
                VarDec(
                    parameter_type,
                    [
                        parameter
                    ]
                )
            )

            while self.lexer.next.type == Token.COMMA:
                self.eat(Token.COMMA)

                parameter = Identifier(
                    self.lexer.next.value,
                    []
                )

                self.eat(Token.IDENTIFIER)
                self.eat(Token.COLON)

                parameter_type = self.lexer.next.value
                self.eat(Token.TYPE)

                children.append(
                    VarDec(
                        parameter_type,
                        [
                            parameter
                        ]
                    )
                )

        self.eat(Token.CLOSE_PAR)

        return_type = "()"

        if self.lexer.next.type == Token.ARROW:
            self.eat(Token.ARROW)

            if self.lexer.next.type == Token.TYPE:
                return_type = self.lexer.next.value
                self.eat(Token.TYPE)
            
            elif self.lexer.next.type == Token.OPEN_PAR:
                self.eat(Token.OPEN_PAR)
                self.eat(Token.CLOSE_PAR)
                return_type = "()"
            
            else:
                raise Exception(f"[Parser] Unexpected token {self.lexer.next.type}")

        self.inside_function += 1
        try:
            block = self.parseBlock()
        finally:
            self.inside_function -= 1
        children.append(block)

        return FuncDec(
            return_type,
            children
        )
    
    def parse_func_declaration(self):
        return self.parseFuncDeclaration()
    
    def parserProgram(self):
        children = []

        while self.lexer.next.type != Token.EOF:
            if self.lexer.next.type == Token.FUNC:
                children.append(self.parseFuncDeclaration())
            
            elif self.lexer.next.type == Token.LET:
                children.append(self.parseVarDec())
            
            else:
                raise Exception(f"[Parser] Unexpected token {self.lexer.next.type}")
        
        main_found = False

        for child in children:
            if isinstance(child, FuncDec) and child.children[0].value == "main":
                main_found = True

                if len(child.children[1:-1]) != 0 or child.value != "()":
                    raise Exception(
                        "[Semantic] Invalid main"
                    )
        
        if not main_found:
            raise Exception(
                "[Semantic] main not defined"
            )
        
        children.append(
            FuncCall(
                "main",
                []
            )
        )
        
        return Block("program", children)
    

    def parserStatement(self):

        if self.lexer.next.type == Token.LET:
            return self.parseVarDec()
            

        if self.lexer.next.type == Token.IDENTIFIER:
            identifier = self.lexer.next.value
            Identifier_node = Identifier(identifier, [])

            #I need eat the tokens
            self.eat(Token.IDENTIFIER)

            if self.lexer.next.type == Token.ASSIGN:
                self.eat(Token.ASSIGN)

                expression_node = self.parseBoolExpression()

                self.eat(Token.SEMICOLON)

                return Assignment("=", [Identifier_node, expression_node])
            
            if self.lexer.next.type == Token.OPEN_PAR:
                func_call = self.parseFuncCall(identifier)

                self.eat(Token.SEMICOLON)

                return func_call
            
            raise Exception(f"[Parser] Unexpected token {self.lexer.next.type}")
        
        if self.lexer.next.type == Token.PRINT:
            self.eat(Token.PRINT)
            self.eat(Token.OPEN_PAR)

            expression_node = self.parseBoolExpression()

            self.eat(Token.CLOSE_PAR)
            self.eat(Token.SEMICOLON)

            return Print("println!", [expression_node])
        
        if self.lexer.next.type == Token.RETURN:
            if self.inside_function == 0:
                raise Exception(
                    "[Semantic] Return outside function"
                )

            self.eat(Token.RETURN)

            expression_node = self.parseBoolExpression()

            self.eat(Token.SEMICOLON)

            return Return(
                "return",
                [
                    expression_node
                ]
            )
        
        if self.lexer.next.type == Token.SEMICOLON:
            self.eat(Token.SEMICOLON)
            return NoOp(None, [])
        
        if self.lexer.next.type == Token.IF:
            self.eat(Token.IF)
            self.eat(Token.OPEN_PAR)
            
            condition = self.parseBoolExpression()

            self.eat(Token.CLOSE_PAR)

            if self.lexer.next.type == Token.OPEN_BRA:
                true_block = self.parseBlock()
            else:
                true_block = self.parserStatement()

            if self.lexer.next.type == Token.ELSE:
                self.eat(Token.ELSE)

                if self.lexer.next.type == Token.OPEN_BRA:
                    false_block = self.parseBlock()
                else:
                    false_block = self.parserStatement()

                return If(None,[condition, true_block, false_block])
            
            return If(None, [condition, true_block])
        
        if self.lexer.next.type == Token.WHILE:
            self.eat(Token.WHILE)
            self.eat(Token.OPEN_PAR)

            condition = self.parseBoolExpression()

            self.eat(Token.CLOSE_PAR)

            if self.lexer.next.type == Token.OPEN_BRA:
                block = self.parseBlock()
            else:
                block = self.parserStatement()

            return While(None, [condition, block])
        
        if self.lexer.next.type == Token.OPEN_BRA:
            return self.parseBlock()


        raise Exception(f"[Parser] Unexpected token {self.lexer.next.type}")

    
    def parseExpression(self):
        result = self.parseTerm()

        while self.lexer.next.type in (Token.PLUS, Token.MINUS):
            op = self.lexer.next.value
            self.eat(self.lexer.next.type)

            rhs = self.parseTerm()

            result = BinOp(op, [result, rhs])

        return result
    
    def parseRelExpression(self):
        result = self.parseExpression()

        while self.lexer.next.type in (Token.LT, Token.GT, Token.EQ):

            op = self.lexer.next.value
            self.eat(self.lexer.next.type)

            rhs = self.parseExpression()

            result = BinOp(op, [result, rhs])
        
        return result
    
    def parseBoolTerm(self):
        result = self.parseRelExpression()
        while self.lexer.next.type == Token.AND:

            op = self.lexer.next.value
            self.eat(Token.AND)

            rhs = self.parseRelExpression()

            result = BinOp(op, [result, rhs])

        return result
    
    def parseBoolExpression(self):
        result = self.parseBoolTerm()

        while self.lexer.next.type == Token.OR:
            op = self.lexer.next.value
            self.eat(Token.OR)

            rhs = self.parseBoolTerm()

            result = BinOp(op, [result, rhs])

        return result

            
    def parseFactor(self):

        if self.lexer.next.type == Token.NOT:
            self.eat(Token.NOT)

            return UnOp("!", [self.parseFactor()])
        
        if self.lexer.next.type == Token.READ:
            self.eat(Token.READ)
            self.eat(Token.OPEN_PAR)
            self.eat(Token.CLOSE_PAR)

            return Read(None, [])


        # Se for NUMBER
        if self.lexer.next.type == Token.INT:
            node = IntVal(self.lexer.next.value, [])  # peguei o valor do numero
            self.eat(Token.INT)

            return node
        
        # +- unário
        if self.lexer.next.type == Token.PLUS:
            self.eat(Token.PLUS)
            return UnOp('+', [self.parseFactor()])
        
        if self.lexer.next.type == Token.MINUS:
            self.eat(Token.MINUS)
            return UnOp('-', [self.parseFactor()])
        
        # Se for PARÊNTESES
        if self.lexer.next.type == Token.OPEN_PAR:
            self.eat(Token.OPEN_PAR)

            node = self.parseBoolExpression()

            self.eat(Token.CLOSE_PAR)

            return node
        
        if self.lexer.next.type == Token.BOOL:
            node = BoolVal(
                self.lexer.next.value,
                []
            )

            self.eat(Token.BOOL)

            return node
        
        if self.lexer.next.type == Token.STR:
            node = StringVal(
                self.lexer.next.value,
                []
            )

            self.eat(Token.STR)

            return node

        
        if self.lexer.next.type == Token.IDENTIFIER:
            identifier = self.lexer.next.value
            node = Identifier(identifier, [])
            self.eat(Token.IDENTIFIER)

            if self.lexer.next.type == Token.OPEN_PAR:
                return self.parseFuncCall(identifier)

            return node 
        
        else:
            raise Exception("Deu merda!")
        
        
    def parseBlock(self):
        children = []

        self.eat(Token.OPEN_BRA)

        while self.lexer.next.type != Token.CLOSE_BRA:
            children.append(self.parserStatement())

        self.eat(Token.CLOSE_BRA)

        return Block(None, children)


    # I need to creat a new function "parseTerm".
    def parseTerm(self):
        '''The function handles multiplication and division'''
        result = self.parseFactor()

        while self.lexer.next.type in (Token.MULT, Token.DIV):
            op = self.lexer.next.value
            self.eat(self.lexer.next.type)

            rhs = self.parseFactor()
            result = BinOp(op, [result, rhs])
    

        return result
    
    def run(self):
        self.lexer.selectNext()
        root = self.parserProgram()

        if self.lexer.next.type != Token.EOF:
            raise Exception (f"[Parser] Unexpected token {self.lexer.next.type}")
        
        return root
    

def main():
    filename = sys.argv[1]

    with open(filename, "r") as file:
        source = file.read()

    source = Prepro.filter(source)

    lexer = Lexer(source)
    parser = Parser(lexer)

    root = parser.run()

    st = SymbolTable()
    root.evaluate(st)

if __name__ == "__main__":
    main()
