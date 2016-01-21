import ply.lex as lex
import ply.yacc as yacc

tokens = (
    "SYMBOL",
    "COUNT"
)

t_SYMBOL = (
    r"C[laroudsemf]?|Os?|N[eaibdpos]?|S[icernbmg]?|P[drmtboau]?|"
    r"H[eofgas]?|A[lrsgutcm]|B[eraik]?|Dy|E[urs]|F[erm]?|G[aed]|"
    r"I[nr]?|Kr?|L[iaur]|M[gnodt]|R[buhenaf]|T[icebmalh]|"
    r"U|V|W|Xe|Yb?|Z[nr]"
)

def t_COUNT(t):
    r"\d+"
    t.value = int(t.value)
    return t

def t_error(t):
    raise TypeError("Unknown text '{:s}'".format(t.value,))

lex.lex()

lex.input("CH3COOH")

for tok in iter(lex.token, None):
    print((repr(tok.type), repr(tok.value)))

# yacc

class Atom(object):
    def __init__(self, symbol, count):
        self.symbol = symbol
        self.count = count
    def __repr__(self):
        return ("Atom(%r, %r)" % (self.symbol, self.count))

# When parsing starts, try to make a "chemical_equation" because it's
# the name on left-hand side of the first p_* function definition.
def p_species_list(p):
    "chemical_equation :  chemical_equation species"
    print('p_single_species', p.__dict__)
    p[0] = p[1] + [p[2]]

def p_species(p):
    "chemical_equation : species"
    print('p_species', p.__dict__)
    p[0] = [p[1]]

def p_single_species(p):
    """
    species : SYMBOL
    species : SYMBOL COUNT
    """
    print('p_single_species', p.__dict__)
    if len(p) == 2:
        p[0] = Atom(p[1], 1)
    elif len(p) == 3:
        p[0] = Atom(p[1], p[2])
        
def p_error(p):
    print("Syntax error at '%s'" % p.value)
    
yacc.yacc()

print('\nH2SO4')
for e in yacc.parse("H2SO4"):
    print(e)