import math
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

def faktorial(x):
    if x == 0:
        return 1
    else:
        return x * faktorial(x-1)

def mocnina(x, y):
    return x ** y

def odmocnina(x, y):
    return x ** (1/y)

def sin(x):
    return math.sin(math.radians(x))

def cos(x):
    return math.cos(math.radians(x))

def tan(x):
    return math.tan(math.radians(x))

def cot(x):
    return 1 / math.tan(math.radians(x))

def eval_expr(expr):
    """
    Evaluates a mathematical expression provided as a string without parentheses.
    The expression respects the precedence of operators.
    """
    # Definice konstant
    constants = {'π': math.pi, 'e': math.e}

    # Odstránenie medzier z výrazu
    expr = expr.replace(" ", "")

    # Rozdelenie výrazu na čísla a operátory
    tokens = re.findall(r"\d+\.?\d*|[-+*/^!√]|sin|cos|tan|cot|π|e", expr)

    # Konverzia čísel z reťazcov na floaty
    tokens = [float(token) if token.replace('.','',1).isdigit() else token for token in tokens]

    # Spracovani goniometrickych funkcii, faktorialu, mocnin a odmocnin
    i = 0
    while i < len(tokens):
        if tokens[i] in ['sin', 'cos', 'tan', 'cot']:
            if tokens[i] == 'sin':
                result = sin(tokens[i+1])
            elif tokens[i] == 'cos':
                result = cos(tokens[i+1])
            elif tokens[i] == 'tan':
                result = tan(tokens[i+1])
            elif tokens[i] == 'cot':
                result = cot(tokens[i+1])
            tokens[i:i+2] = [result]
        elif tokens[i] == '!':
            result = faktorial(tokens[i-1])
            tokens[i-1:i+1] = [result]
        elif tokens[i] == '^':
            result = mocnina(tokens[i-1], tokens[i+1])
            tokens[i-1:i+2] = [result]
        elif tokens[i] == '√':
            result = odmocnina(tokens[i+1], tokens[i-1])
            tokens[i-1:i+2] = [result]
        elif tokens[i] in constants:
            tokens[i] = constants[tokens[i]]
        i += 1

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

    # Vraciame vysledok ako string, ak je celé číslo, zobrazuje bez desatinnej časti
    result = tokens[0]
    return str(int(result) if result == int(result) else result)

print(eval_expr("2√4 + sin30 * 5 - 3! + cot45 + e - 2^8"))

