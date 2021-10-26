"""
    Yacc example
"""

import ply.yacc as yacc

# get the token map from the lexer, this is required
from com.other_excise.ply_.token_rules import tokens


def p_expression_plus(p):
    """expression : expression PLUS term"""
    p[0] = p[1] + p[3]


def p_expression_minus(p):
    """expression : expression MINUS term"""
    p[0] = p[1] - p[3]


def p_expression_term(p):
    """expression : term"""
    p[0] = p[1]


def p_term_times(p):
    """term : term TIMES factor"""
    p[0] = p[1] * p[3]


def p_term_div(p):
    """term : term DIVIDE factor"""
    p[0] = p[1] / p[3]


def p_term_factor(p):
    """term : factor"""
    p[0] = p[1]

# how many NUMBER tokens had been encountered
num_count = 0


def p_factor_num(p):
    """factor : NUMBER"""
    global num_count
    num_count += 1
    p[0] = p[1]


def p_factor_expr(p):
    """factor : LPAREN expression RPAREN"""
    p[0] = p[2]


# Error rule for syntax errors
def p_error(p):
    print('Syntax error in input!')


# build the parser
parser = yacc.yacc(debug=True)

# parse the str
while True:
    try:
        str1 = input('calc > ')
    except Exception as e:
        break
    if not str1:
        continue
    print(parser.parse(str1))
    print(num_count)


