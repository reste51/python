"""
    build tokenizer from these rules
"""
from ply import lex
import com.other_excise.ply_.token_rules as token_rules

lexer = lex.lex(module=token_rules)
lexer.input('10 / \n'
            ' ( \n'
            '1 + 2)')


# 输出 token
while True:
    token = lexer.token()
    if token:
        print(token)
    else:
        break


ll = lexer.clone()
print(ll.lexdata, ll.lexpos, ll.lexmatch)

