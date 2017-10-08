
EOF = "EOF"
INTEGER = "INTEGER"
PLUS, MINUS, MUL, DIV = "PLUS", "MINUS", "MUL", "DIV"
OPERATORS = (PLUS, MINUS, MUL, DIV)


class Token(object):
    def __init__(self, type_, value):
        self.type = type_
        self.value = value


class Interpreter(object):
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_char = self.text[self.pos]
        self.current_token = None
        
    def advance(self):
        self.pos = self.pos + 1
        if self.pos > len(self.text) - 1:
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
                return Token(MUL, '*')
            if self.current_char == '/':
                self.advance()
                return Token(DIV, '/')
            
            raise Exception()
        
        return Token(EOF, None)
    
    def eat(self, type_):
        if self.current_token is not None and self.current_token.type == type_:
            self.current_token = self.get_next_token()
        else:
            raise Exception()
    
    def factor(self):
        token = self.current_token
        self.eat(INTEGER)
        return token.value

    def term(self):
        result = self.factor()
        
        while self.current_token.type in (MUL, DIV):
            token = self.current_token
            if token.type == MUL:
                self.eat(MUL)
                result *= self.factor()
            else:
                self.eat(DIV)
                result = int(result / self.factor())
        return result

    def expr(self):
        
        self.current_token = self.get_next_token()
        
        result = self.term()
        
        while self.current_token.type in (PLUS, MINUS):
            token = self.current_token
            if token.type == PLUS:
                self.eat(PLUS)
                result += self.term()
            else:
                self.eat(MINUS)
                result -= self.term()
            
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
        result = interpreter.expr()
        print(result)


if __name__ == '__main__':
    main()