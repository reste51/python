"""
    将一个字符文本  切割成一组 token, 并标注词性； 展示 lexer.py 是如何工作的

    一个 数字和 +,-,*,/ 的简单表达式解析器的 分词器

"""
import ply.lex as lex

# token 的列表
tokens = (
    'EQUAL',
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN'

)

# 简单token 的表达式
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_EQUAL= r'='

# A regular expression rule with some action code
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t


# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

    # A string containing ignored characters (spaces and tabs)


t_ignore = ' \t'


# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# Build the lexer
lexer = lex.lex()

# Test it out
data = '''
 3 + 4 * 10
   + -20 *2 = 90
 '''

# Give the lexer some input
lexer.input(data)

while True:
     tok = lexer.token()
     if not tok:
         break      # No more input
     print(tok)












