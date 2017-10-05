
const EOF = "EOF"
const INTEGER = "INT"
const PLUS = "PLUS"
const MINUS = "MINUS"

function token(type, value) {
    return {
        type: type, 
        value: value
    }
}

text = "1+1"
pos = 0
currentChar = text[pos]
currentToken = null


function advance() {
    pos++
    currentChar = text.length -1 < pos ? null : text[pos]
}

function integer() {
    result = ""
    while (currentChar !== null && isNumeric(currentChar)) {
        result += currentChar
        advance()
    }
    return parseInt(result)
}

function skipWhitespace() {
    while (currentChar === " ")
        advance()    
}

function getNextToken() {
    while (currentChar !== null) {
        if (currentChar === " ") {
            skipWhitespace()
            continue
        }
        if (isNumeric(currentChar)) {
            return token(INTEGER, integer())
        }
        if (currentChar === "+") {
            advance()
            return token(PLUS, "+")
        }
        if (currentChar === "-") {
            advance()
            return token(MINUS, "-")
        }

        throw "Error"
    }

    return token(EOF, null)
}

function eat(type) {
    if (currentToken.type === type) {
        currentToken = getNextToken()
    }
    else {
        throw "Error"
    }
}

function expression() {
    currentToken = getNextToken()
    right = currentToken
    eat(INTEGER)
    var result = 0
    result = right.value

    while ([PLUS, MINUS].indexOf(currentToken.type) > -1)
    {
        if (currentToken.type === PLUS) {
            eat(PLUS)
            result += currentToken.value
        }
        else {
            eat(MINUS)
            result -= currentToken.value
        }

        eat(INTEGER)
    }

    return result
}

function isNumeric(n) {
    return !isNaN(parseInt(n)) && isFinite(n);
}



var stdin = process.openStdin();

stdin.addListener("data", function (d) {
    
    text = d.toString().trim()
    pos = 0
    currentChar = text[pos]
    currentToken = null
    output = expression()
    
    console.log(text)
    console.log(output)
});