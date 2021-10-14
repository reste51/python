"""
    token- rule

    the module just contain the lexing rules
"""
# List of token names( tuple ), this is always required
tokens = (
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN'
)

# Regular expression rules for simple tokens
t_PLUS = r'\+'
t_MINUS = r'\-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'


# Regular expression rules  with action code
# 该函数用于修改已生成的LexToken(value,type, lineno, linepos)
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)  # 将字符串的数值转为 int
    return t


# define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    # t.lexer.lineno += len(t.value)
    t.lexer.lineno += 1


# a string containing ignored characters(space and tab)
t_ignore = ' \t'


# error handling rule
def t_error(t):
    print(f'Illegal character is {t.value[0]}')
    t.lexer.skip(1)
