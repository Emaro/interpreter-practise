# EOF means End-Of-File
INTEGER, PLUS, EOF = 'INTEGER', 'PLUS', 'EOF'
MINUS = 'MINUS'
MULTIPLY = 'MULTIPLY'
DIVIDE = 'DIVIDE'

OPERATORS = [PLUS, MINUS, MULTIPLY, DIVIDE]

class Token(object):
    def __init__(self, type, value):
        # token type = INTEGER, PLUS or EOF
        self.type = type
        
        self.value = value
    
    def __str__(self):
        return 'Token({type}, {value})'.format(type=self.type, value=repr(self.value))
    
    def __repr__(self):
        return self.__str__()


class Interpreter(object):
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.currentToken = None
        self.current_char = self.text[self.pos]
    
    def error(self):
        raise Exception('Error parsing input')
    
    def advance(self):
        self.pos += 1
        if self.pos > len(self.text) -1:
            self.current_char = None
        else:
            self.current_char = self.text[self.pos]
    
    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()
    
    def integer(self):
        result = ''
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        return int(result)
    
    def get_next_token(self):
        
        while self.current_char is not None:
            
            if self.current_char.isspace():
                self.skip_whitespace()
                continue
        
            if self.current_char.isdigit():
                return Token(INTEGER, self.integer())
            
            if self.current_char == '+':
                self.advance()
                return Token(PLUS, '+')
            
            if self.current_char == '-':
                self.advance()
                return Token(MINUS, '-')
            
            if self.current_char == '*':
                self.advance()
                return Token(MULTIPLY, '*')
            
            if self.current_char == '/':
                self.advance()
                return Token(DIVIDE, '/')
        
            self.error()
        
        return Token(EOF, None)
    
    def eat(self, token_type):
        if self.currentToken.type == token_type:
            self.currentToken = self.get_next_token()
        else:
            self.error()
    
    def expression(self):
        # INTEGER PLUS INTEGER
        self.currentToken = self.get_next_token()
        
        left = self.currentToken
        self.eat(INTEGER)
        
        result = left.value
        
        op = self.currentToken
        while op.type in OPERATORS:
            self.eat(op.type)
            
            next_int = self.currentToken
            self.eat(INTEGER)

            if op.type == PLUS:
                result = result + next_int.value
            elif op.type == MINUS:
                result = result - next_int.value
            elif op.type == MULTIPLY:
                result = result * next_int.value
            else:
                result = result / next_int.value
                
            op = self.currentToken
        
        return result


def main():
    while True:
        try:
            text = input('calc>')
        except EOFError:
            break
        if not text:
            continue
        interpreter = Interpreter(text)
        result = interpreter.expression()
        print(result)


if __name__ == '__main__':
    main()
