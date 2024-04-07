import re

# Definícia funkcií
def scitanie(x, y):
    return x + y

def odcitanie(x, y):
    return x - y

def nasobenie(x, y):
    return x * y

def delenie(x, y):
    if y == 0:
        raise ValueError("Nulou delit nemozno")
    return x / y

def eval_expr(expr):
    """
    Evaluates a mathematical expression provided as a string without parentheses.
    The expression respects the precedence of operators.
    """
    # Odstránenie medzier z výrazu
    expr = expr.replace(" ", "")

    # Rozdelenie výrazu na čísla a operátory
    tokens = re.findall(r"\d+\.?\d*|[-+*/]", expr)

    # Konverzia čísel z reťazcov na floaty
    tokens = [float(token) if token.replace('.','',1).isdigit() else token for token in tokens]

    # Spracovanie násobenia a delenia
    i = 0
    while i < len(tokens):
        if tokens[i] in ['*', '/']:
            if tokens[i] == '*':
                result = nasobenie(tokens[i-1], tokens[i+1])
            else:
                result = delenie(tokens[i-1], tokens[i+1])
            tokens[i-1:i+2] = [result]  # Nahradenie i-1, i, i+1 výsledkom
            i -= 1  # Vráť sa o jeden krok, aby sme skontrolovali novú sekvenciu
        i += 1

    # Spracovanie sčítania a odčítania
    i = 0
    while i < len(tokens):
        if tokens[i] in ['+', '-']:
            if tokens[i] == '+':
                result = scitanie(tokens[i-1], tokens[i+1])
            else:
                result = odcitanie(tokens[i-1], tokens[i+1])
            tokens[i-1:i+2] = [result]
            i -= 1
        i += 1

    return tokens[0]

