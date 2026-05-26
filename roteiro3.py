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

    def __init__(self, type, value):
        self.type = type
        self.value = value

class Lexer:
    '''I need make the class Lexer for break the code in tokens'''
    def __init__(self, source):
        self.source = source
        self.position = 0
        self.next = None
        
    '''Now, I have make the function selectNext to separate into tokens'''
    def selectNext(self):
        # ignore whitespaces
        while self.position < len(self.source) and self.source[self.position] == ' ':
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

        # Lexical error
        raise Exception(f"[Lexer] invalid charcter: {current_char}")

class Parser:
    '''Here, we will consume the tokens from the lexer.
    The expression must being with INT
    store the INT in result to perform the calculation'''
    def __init__(self, lexer):
        self.lexer = lexer

    def eat(self, token_type):
        if self.lexer.next.type == token_type:
            self.lexer.selectNext()
        else:
            raise Exception(f"[Parser] Unexpected token {self.lexer.next.type}")
    
    def parseExpression(self):
        result = self.parseTerm()

        while self.lexer.next.type in (Token.PLUS, Token.MINUS):
            op = self.lexer.next.type
            self.eat(op)

            rhs = self.parseTerm()

            if op == Token.PLUS:
                result += rhs

            elif op == Token.MINUS:
                result -= rhs

        return result
            
    def parseFactor(self):
        # Se for NUMBER
        if self.lexer.next.type == Token.INT:
            result = self.lexer.next.value  # peguei o valor do numero
            self.eat(Token.INT)

            return result
        
        # +- unário
        if self.lexer.next.type == Token.PLUS:
            self.eat(Token.PLUS)
            return self.parseFactor()
        
        if self.lexer.next.type == Token.MINUS:
            self.eat(Token.MINUS)
            return -self.parseFactor()
        
        # Se for PARÊNTESES
        if self.lexer.next.type == Token.OPEN_PAR:
            self.eat(Token.OPEN_PAR)

            result = self.parseExpression()

            self.eat(Token.CLOSE_PAR)

            return result
        
        else:
            raise Exception("Deu merda!")


    # I need to creat a new function "parseTerm".
    def parseTerm(self):
        '''The function handles multiplication and division'''
        result = self.parseFactor() # peguei o primeiro valor

        while self.lexer.next.type in (Token.MULT, Token.DIV):
            op = self.lexer.next.type

            self.eat(op)

            rhs = self.parseFactor() # pega o proximo valor

            if op == Token.MULT:
                result *= rhs

            if op == Token.DIV:
                result /= rhs
    

        return result
    
    def run(self):
        self.lexer.selectNext()
        result = self.parseExpression()

        if self.lexer.next.type != Token.EOF:
            raise Exception (f"[Parser] Unexpected token {self.lexer.next.type}")
        
        return result
    

def main():
    source = sys.argv[1] #peguei a entrada

    lexer = Lexer(source) #criar o lexer

    parser = Parser(lexer)

    result = parser.run()

    print(result)

if __name__ == "__main__":
    main()

