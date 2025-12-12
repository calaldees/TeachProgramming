import sys
import enum
from typing import NamedTuple, Self, Callable, Protocol, Any
from collections.abc import Sequence,  MutableSequence, Mapping
from functools import cached_property
from pprint import pprint as pp
import functools
import logging
from pathlib import Path

log = logging.getLogger(__name__)

# https://filestore.aqa.org.uk/resources/computing/AQA-8525-NG-PC.PDF

# https://www.geeksforgeeks.org/compiler-design/recursive-descent-parser/
# https://craftinginterpreters.com/parsing-expressions.html




class TokenType(enum.StrEnum):
    IDENTIFIER = enum.auto()
    STRING = enum.auto()
    NUMBER = enum.auto()
    EOF = enum.auto()

    BANG_EQUAL = '!='
    EQUAL_EQUAL = '=='
    LESS_EQUAL = '<='
    GREATER_EQUAL = '>='

    LEFT_PAREN = '('
    RIGHT_PAREN = ')'
    LEFT_BRACE = '{'
    RIGHT_BRACE = '}'
    COMMA = ','
    DOT = '.'
    MINUS = '-'
    PLUS = '+'
    SEMICOLON = ';'
    STAR = '*'
    BANG = '!'
    GREATER = '>'
    LESS = '<'
    EQUAL = '='
    SLASH = '/'

    AND = enum.auto()
    CLASS = enum.auto()
    ELSE = enum.auto()
    FALSE = enum.auto()
    FOR = enum.auto()
    IF = enum.auto()
    NIL = enum.auto()
    OR = enum.auto()
    PRINT = enum.auto()
    RETURN = enum.auto()
    SUPER = enum.auto()
    THIS = enum.auto()
    TRUE = enum.auto()
    VAR = enum.auto()
    WHILE = enum.auto()

KEYWORDS = frozenset((
    TokenType.AND,
    TokenType.CLASS,
    TokenType.ELSE,
    TokenType.FALSE,
    TokenType.FOR,
    TokenType.IF,
    TokenType.NIL,
    TokenType.OR,
    TokenType.PRINT,
    TokenType.RETURN,
    TokenType.SUPER,
    TokenType.THIS,
    TokenType.TRUE,
    TokenType.VAR,
    TokenType.WHILE,
))
OPERATORS_NUMERICAL = frozenset((
    TokenType.MINUS,
    TokenType.SLASH,
    TokenType.STAR,
    TokenType.PLUS,
    TokenType.GREATER,
    TokenType.GREATER_EQUAL,
    TokenType.LESS,
    TokenType.LESS_EQUAL,
))

# ------------------------------------------------------------------------------

class TextLocation(NamedTuple):
    line: int
    col: int
    def __str__(self) -> str:
        return f'Line: {self.line} Col: {self.col}'
class Token(NamedTuple):
    location: TextLocation
    lexeme: str
    type: TokenType
    literal: str
class TokenError(NamedTuple):
    location: TextLocation
    message: str
class MutableTextLocation():
    line: int = 0
    col: int = 0
    @property
    def immutable(self) -> TextLocation:
        return TextLocation(self.line, self.col)
    def __str__(self) -> str:
        return str(self.immutable)
    def newLine(self):
        self.line += 1
        self.col = 0

type wasConsumed = bool | None
TokenHandler = Callable[['Scanner'], wasConsumed]

class Scanner():
    def __init__(self, source: str, token_handlers: Sequence[TokenHandler]):
        assert source
        assert token_handlers
        self.source = source
        self.token_handlers = token_handlers
        self.location = MutableTextLocation()
        self.index_start: int = 0
        self.index_current: int = 0
        self._tokens: MutableSequence[Token] = []
        self._errors: MutableSequence[TokenError] = []
    @property
    def isAtEnd(self) -> bool:
        return self.index_current >= len(self.source)
    def advance(self, inc=1) -> None:
        self.index_current += inc
        self.location.col += inc
    def match(self, expected: str) -> bool:
        if expected != self.peek(len(expected)): return False
        self.advance(len(expected))
        return True
    def peek(self, offset:int=1) -> str:
        return self.source[self.index_current : min(self.index_current+offset, len(self.source))]
    def addToken(self, type: TokenType, literal: str = '') -> None:
        self._tokens.append(Token(
            location=self.location.immutable,
            lexeme=self.source[self.index_start:self.index_current],
            type=type,
            literal=literal
        ))
    @cached_property
    def tokens(self) -> Sequence[Token]:
        while not self.isAtEnd:
            self.index_start = self.index_current
            if not any(token_handler(self) for token_handler in self.token_handlers):
                self._errors.append(TokenError(self.location.immutable, f"Unexpected character {self.peek()}"))
        self.addToken(TokenType.EOF, '')
        return self._tokens




def white_space(s: Scanner) -> wasConsumed:
    return any((s.match(i) for i in (' ', '\t', '\r')))

def new_line(s: Scanner) -> wasConsumed:
    if s.match('\n'):
        s.location.newLine()
        return True

def comment(s: Scanner) -> wasConsumed:
    if s.match('#'):
        while (s.peek() not in ('\n', '')):
            s.advance()

def string(s: Scanner) -> wasConsumed:
    if s.match('"'):
        while s.peek() != '"' and not s.isAtEnd:
            s.advance()
            if s.peek() == '\n': s.location.newLine()
        s.advance()
        if s.isAtEnd:
            s._errors.append(TokenError(s.location.immutable, 'Unterminated string'))
        s.addToken(TokenType.STRING, s.source[s.index_start+1:s.index_current-1])

def number(s: Scanner) -> wasConsumed:
    if s.peek().isdigit():
        while s.peek().isdigit(): s.advance()
        peek = s.peek(2)
        if len(peek)==2 and peek[0] == '.' and peek[1].isdigit():
            s.advance()  # consume the '.'
            while s.peek().isdigit(): s.advance()
        s.addToken(TokenType.NUMBER, s.source[s.index_start:s.index_current])

def identifier(s: Scanner) -> wasConsumed:
    if s.peek().isalpha():
        while s.peek().isalnum(): s.advance()
        text = s.source[s.index_start:s.index_current]
        s.addToken(TokenType(text) if text in KEYWORDS else TokenType.IDENTIFIER, text)

def createDefaultTokenHandlerFor(t: str) -> TokenHandler:
    def _t(s: Scanner) -> wasConsumed:
        if s.match(t):
            s.addToken(TokenType(t), t)
            return True
    return _t

DEFAULT_TOKEN_HANDLERS: Sequence[TokenHandler] = (
    white_space,
    new_line,
    comment,
    string,
    number,
    identifier,
    *map(createDefaultTokenHandlerFor, ('!=', '==', '<=', '>=', '(', ')', '{', '}', ',', '.', '-', '+', ';', '*', '!', '>', '<', '=', '/'))
)

scanner: Callable[[str], Scanner] = functools.partial(Scanner, token_handlers=DEFAULT_TOKEN_HANDLERS)

def test_scanner():
    tokens = scanner('thing = ("test" + 1.23) # This is a comment').tokens
    token_types = tuple(t.type for t in tokens)
    assert token_types == (
        TokenType.IDENTIFIER,
        TokenType.EQUAL,
        TokenType.LEFT_PAREN,
        TokenType.STRING,
        TokenType.PLUS,
        TokenType.NUMBER,
        TokenType.RIGHT_PAREN,
        TokenType.EOF,
    )


# ------------------------------------------------------------------------------

#class (Protocol):


type Number = int|float
type PrimitiveValue = str|bool|None|Number
class Literal():
    def __init__(self, value: PrimitiveValue):
        self.value = value
    def __str__(self) -> str:
        return str(self.value)
class Unary():
    def __init__(self, operator: Token, expression: 'Expr'):
        self.operator = operator
        self.expression = expression
    def __str__(self) -> str:
        return f'{self.operator.type.value}{self.expression}'
class Binary():
    def __init__(self, expression1: 'Expr', operator: Token, expression2: 'Expr'):
        self.expression1 = expression1
        self.operator = operator
        self.expression2 = expression2
    def __str__(self) -> str:
        return ''.join(map(str, (self.expression1, self.operator.type.value, self.expression2)))
class Grouping():
    def __init__(self, expression: 'Expr'):
        self.expression = expression
    def __str__(self) -> str:
        return f'({self.expression})'

Expr = Literal | Unary | Binary | Grouping


class Parser():
    class ParseError(BaseException): ...

    def __init__(self, tokens: Sequence[Token]):
        self.tokens = tokens
        self.index_current: int = 0

    @property
    def parse(self) -> Expr | None:
        try:
            return self.expression()
        except self.ParseError as pe:
            log.exception('ParseError: TODO')
            return None

    @property
    def peek(self) -> Token:
        return self.tokens[self.index_current]
    @property
    def previous(self) -> Token:
        return self.tokens[self.index_current - 1]
    @property
    def advance(self) -> Token:
        if not self.isAtEnd: self.index_current += 1
        return self.previous
    @property
    def isAtEnd(self) -> bool:
        return self.peek.type == TokenType.EOF
    def check(self, type: TokenType) -> bool:
        if self.isAtEnd: return False
        return self.peek.type == type
    def match(self, *types: TokenType) -> Token | None:
        for t in types:
            if self.check(t):
                return self.advance
    def consume(self, type: TokenType, error_message: str) -> Token:
        if self.check(type): return self.advance
        raise self.error(self.peek, error_message)

    def error(self, token: Token, error_message: str) -> 'Parser.ParseError':
        log.error(f'{token.location} - {token.lexeme} - {error_message}')
        return self.ParseError()
    def synchronize(self) -> None:
        # humm ... sure this can be python-ed and simplified
        self.advance
        while not self.isAtEnd:
            if self.previous.type == TokenType.SEMICOLON: return
            match self.peek.type:
                case (TokenType.CLASS, TokenType.VAR, TokenType.FOR, TokenType.IF, TokenType.WHILE, TokenType.PRINT, TokenType.RETURN):
                    return
            self.advance
    """
    expression     → equality ;
    equality       → comparison ( ( "!=" | "==" ) comparison )* ;
    comparison     → term ( ( ">" | ">=" | "<" | "<=" ) term )* ;
    term           → factor ( ( "-" | "+" ) factor )* ;
    factor         → unary ( ( "/" | "*" ) unary )* ;
    unary          → ( "!" | "-" ) unary | primary ;
    primary        → NUMBER | STRING | "true" | "false" | "nil" | "(" expression ")" ;
    """
    def expression(self) -> Expr:
        return self.equality()
    def equality(self) -> Expr:
        expr = self.comparison()
        while operator := self.match(TokenType.BANG_EQUAL, TokenType.EQUAL_EQUAL):
            expr = Binary(expr, operator, self.comparison())
        return expr
    def comparison(self) -> Expr:
        expr = self.term()
        while operator := self.match(TokenType.GREATER, TokenType.GREATER_EQUAL, TokenType.LESS, TokenType.LESS_EQUAL):
            expr = Binary(expr, operator, self.term())
        return expr
    def term(self) -> Expr:
        expr = self.factor()
        while operator := self.match(TokenType.MINUS, TokenType.PLUS):
            expr = Binary(expr, operator, self.factor())
        return expr
    def factor(self) -> Expr:
        expr = self.unary()
        while operator := self.match(TokenType.SLASH, TokenType.STAR):
            expr = Binary(expr, operator, self.unary())
        return expr
    def unary(self) -> Expr:
        if operator := self.match(TokenType.BANG, TokenType.MINUS):
            return Unary(operator, self.unary())
        return self.primary()
    def primary(self) -> Expr:
        if self.match(TokenType.FALSE): return Literal(False)
        if self.match(TokenType.TRUE): return Literal(True)
        if self.match(TokenType.NIL): return Literal(None)
        if token := self.match(TokenType.NUMBER, TokenType.STRING): return Literal(token.literal)
        if self.match(TokenType.LEFT_PAREN):
            expr = self.expression()
            self.consume(TokenType.RIGHT_PAREN, "Expect ')' after expression.")
            return Grouping(expr)
        raise self.error(self.peek, "Expect expression.")


def test_parser():
    tokens = Scanner('12.3 * (45 - "test") >= !10', DEFAULT_TOKEN_HANDLERS).tokens
    expr = Parser(tokens).parse
    assert str(expr) == '12.3*(45-test)>=!10'


# ------------------------------------------------------------------------------


class Interpreter():

    class RuntimeError(BaseException):
        token: Token
        def __init__(self, token: Token, message: str):
            super().__init__(message)
            self.token = token
        @property
        def message(self) -> str: return self.args[0]


    def stringify(self, obj: Any) -> str:
        if obj == None: return 'nil'
        if isinstance(obj, (float,)):
            text = str(obj)
            if text.endswith(".0"):
                #text = text.substring(0, text.length() - 2)
                pass # TODO
            return text
        return str(obj)

    def isEqual(self, a: Any, b: Any) -> bool:
        if (a == None and b == None): return True
        if (a == None): return False
        return a == b

    def isTruthy(self, obj: Any) -> bool:
        match obj:
            case None:
                return False
            case bool():
                return obj
            case _:
                return True

    def checkNumberOperand(self, operator: Token, operand: Any):
        if isinstance(object, (float,)): return
        raise RuntimeError(operator, "Operand must be a number.")
    def checkNumberOperands(self, operator: Token, left: Any, right: Any):
        if isinstance(left, (float,)) and isinstance(right, (float,)): return
        raise RuntimeError(operator, "Operands must be numbers.")

    def evaluateUnary(self, expr: Unary) -> PrimitiveValue:
        right = self.evaluate(expr.expression)
        match expr.operator.type:
            case TokenType.MINUS:
                self.checkNumberOperand(expr.operator, right)
                return -float(right)
            case TokenType.BANG:
                return not self.isTruthy(right)
        raise NotImplementedError()

    def evaluateBinary(self, expr: Binary) -> PrimitiveValue:
        left = self.evaluate(expr.expression1)
        right = self.evaluate(expr.expression2)

        match expr.operator.type:
            case TokenType.PLUS:
                if isinstance(left,(float,)) and isinstance(right, (float,)):
                    return left + right
                if isinstance(left, str) and isinstance(right, str):
                    return ''.join((left, right))
                raise RuntimeError(expr.operator, "Operands must be two numbers or two strings.")
            case TokenType.MINUS:
                self.checkNumberOperands(expr.operator, left, right)
                return float(left) - float(right)
            case TokenType.SLASH:
                self.checkNumberOperands(expr.operator, left, right)
                return float(left) / float(right)
            case TokenType.STAR:
                self.checkNumberOperands(expr.operator, left, right)
                return float(left) * float(right)
            case TokenType.GREATER:
                self.checkNumberOperands(expr.operator, left, right)
                return float(left) > float(right)
            case TokenType.GREATER_EQUAL:
                self.checkNumberOperands(expr.operator, left, right)
                return float(left) >= float(right)
            case TokenType.LESS:
                self.checkNumberOperands(expr.operator, left, right)
                return float(left) < float(right)
            case TokenType.LESS_EQUAL:
                self.checkNumberOperands(expr.operator, left, right)
                return float(left) <= float(right)

            case TokenType.BANG_EQUAL:
                return not self.isEqual(left, right)
            case TokenType.EQUAL_EQUAL:
                return self.isEqual(left, right)

            case _:
                raise NotImplementedError()


    def evaluate(self, expr: Expr) -> PrimitiveValue:
        match expr:
            case Literal():
                return expr.value
            case Grouping():
                return self.evaluate(expr.expression)
            case Unary():
                return self.evaluateUnary(expr)
            case Binary():
                return self.evaluateBinary(expr)

    def interpret(self, expression: Expr) -> None:
        try:
            value = self.evaluate(expression)
            print(str(value))
        except RuntimeError as error:
            log.exception('RuntimeError - MORE TODO HERE')


def test_interperet_evaluate_expression():
    expr_str = '5 * 5'
    value = Interpreter().evaluate(Parser(Scanner(expr_str, DEFAULT_TOKEN_HANDLERS).tokens).parse)
    assert value == 10


# ------------------------------------------------------------------------------


class Lox:

    def __init__(self):
        self.interpreter = Interpreter()
        self.hadError = False
        self.hadRuntimeError = False

    def report(self, message: str, location: TextLocation):
        log.warning(f'[{location}] {message}')
        self.hadError = True

    def runtimeError(self, error: Interpreter.RuntimeError) -> None:
        log.error(f"{error.message}\n[line {error.token.location}]")
        self.hadRuntimeError = True

    def run(self, source: str) -> None:
        tokens = scanner(source).tokens
        expr = Parser(tokens).parse
        self.interpreter.evaluate(expr)


if __name__ == '__main__':
    lox = Lox()
    if len(sys.argv) == 2 and (file := Path(sys.argv[1])):
        lox.run(file.read_text())
    else:
        print('Lox REPL')
        while _input := input('> '):
            lox.run(_input)
    if lox.hadError: sys.exit(65)
    if lox.hadRuntimeError: sys.exit(75)
