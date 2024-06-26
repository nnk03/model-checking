import ply.lex as lex
import ply.yacc as yacc

# List of token names
tokens = (
    'TRUE',
    'FALSE',
    'PROP_VARIABLE',
    'AND',
    'OR',
    'NOT',
    'IMPLIES',
    'L_PAREN',
    'R_PAREN',
    'L_SQUARE',
    'R_SQUARE',
    'AX', 'EX',
    'AF', 'EF',
    'AG', 'EG',
    # 'AU', 'EU',   # ignoring AU and EU as of now 
    'E', 'A', 'U'
)

# Regular formula rules for simple tokens
t_TRUE = r'T'
t_FALSE = r'F'
t_AND = r'\&'
t_OR = r'\|'
t_NOT = r'\!'
t_L_PAREN = r'\('
t_R_PAREN = r'\)'
t_L_SQUARE = r'\['
t_R_SQUARE = r'\]'
t_IMPLIES = r'->'
t_AX = r'AX'
t_EX = r'EX'
t_AF = r'AF'
t_EF = r'EF'
t_AG = r'AG'
t_EG = r'EG'
t_U = r'U'
t_E = r'E'
t_A = r'A'
t_ignore = ' \t'

# Define a rule for variables
def t_PROP_VARIABLE(t):
    r'[a-z_][a-zA-Z_]*'    # only allowing single letters as propositional variables
    return t


# Error handling rule
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Define precedence and associativity
precedence = (
    ('left', 'OR'),
    ('left', 'AND'),
    ('right', 'NOT'),
    ('right', 'IMPLIES'),
    ('right', 'EX'),
    ('right', 'AX'),
    ('right', 'EF'),
    ('right', 'AF'),
    ('right', 'EG'),
    ('right', 'AG'),
    ('left', 'E'),
    ('right', 'A')
)

# Define the grammar rules
def p_formula_true(p):
    'formula : TRUE'
    p[0] = True


def p_formula_false(p):
    'formula : FALSE'
    p[0] = False

def p_formula_temporal_op(p):
    '''formula : AG formula
               | EG formula
               | AX formula
               | EX formula
               | AF formula
               | EF formula'''
    check = p[1]
    formula = p[2]
    result = (p[1], p[2])
    if check == 'AG':
        result = ('NOT', ('EU', True, ('NOT', formula)))
        pass
    elif check == 'EG':
        # *****
        result = ('EG', formula)
        pass
    elif check == 'AX':
        # AX phi = NOT (EX (NOT phi))
        result = ('NOT', ('EX', ('NOT', formula)))
        pass
    elif check == 'EX':
        # *****
        result = ('EX', formula)
        pass
    elif check == 'AF':
        # AF phi = NOT ( EG ( NOT phi ) )
        result = ('NOT', ('EG', ('NOT', formula)))
        pass
    elif check == 'EF':
        # EF phi = E [T U phi]
        result = ('EU', True, formula)
        pass

    p[0] = result
    # p[0] = (p[1], p[2])

def p_formula_bin_temporal_op(p):
    '''
    formula : E L_SQUARE formula U formula R_SQUARE
            | A L_SQUARE formula U formula R_SQUARE
    '''
    if p[1] == 'A':
        # in terms of minimal set, we need to convert *************
        # A [ a U b ] = NOT (E [(NOT b) U (NOT a AND NOT b)] OR (EG (NOT b)))
        a = p[3]
        b = p[5]
        not_a = ('NOT', a)
        not_b = ('NOT', b)
        and_not_a_not_b = ('&', not_a, not_b)
        eu_not_b_and = ('EU', not_b, and_not_a_not_b)
        eg_not_b = ('EG', not_b)
        or_eu_eg = ('|', eu_not_b_and, eg_not_b)
        result = ('NOT', or_eu_eg)
        # p[0] = ('AU', p[3], p[5])
        p[0] = result
    else:
        p[0] = ('EU', p[3], p[5])

def p_formula_prop_variable(p):
    'formula : PROP_VARIABLE'
    p[0] = p[1]

def p_formula_binop(p):
    '''formula : formula AND formula
                  | formula OR formula
                  | formula IMPLIES formula'''
    if p[2] == '->':
        # converting implies to NOT p OR q
        p[0] = ('|', ('NOT', p[1]), p[3])
    else:
        p[0] = (p[2], p[1], p[3])

def p_formula_not(p):
    'formula : NOT formula'
    p[0] = ('NOT', p[2])


def p_formula_group(p):
    'formula : L_PAREN formula R_PAREN'
    p[0] = p[2]


def p_error(p):
    if p:
        print("Syntax error at '%s'" % p.value)
    else:
        print("Syntax error at EOF")

# Build the parser
parser = yacc.yacc()

# Function to parse propositional formula
def parse_formula(formula):
    return parser.parse(formula)








