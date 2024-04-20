## @file math_functions.py
#  @brief Implementace matematických funkcí.
#
#  Tento soubor obsahuje implementaci různých matematických funkcí,
#  jako je sčítání, odčítání, násobení, dělení, faktoriál, mocnina,
#  odmocnina a goniometrické funkce.
import math
import re
import sys

## @brief Funkce pro sčítání dvou čísel.
#  @param x První sčítanec.
#  @param y Druhý sčítanec.
#  @return Součet x a y.
def scitanie(x, y):
    return x + y

## @brief Funkce pro odčítání dvou čísel.
#  @param x Menšenec.
#  @param y Menšitel.
#  @return Rozdíl x a y.
def odcitanie(x, y):
    return x - y

## @brief Funkce pro násobení dvou čísel.
#  @param x První činitel.
#  @param y Druhý činitel.
#  @return Součin x a y.
def nasobenie(x, y):
    return x * y

## @brief Funkce pro dělení dvou čísel.
#  @param x Dělenec.
#  @param y Dělitel.
#  @return Podíl x a y.
#  @exception ValueError Vyhazuje výjimku, pokud je dělitel roven nule.
def delenie(x, y):
    if y == 0:
        raise ValueError("Math Error")
    return x / y

## @brief Funkce pro výpočet faktoriálu.
#  @param x Hodnota, pro kterou se má vypočítat faktoriál.
#  @return Faktoriál hodnoty x.
#  @exception ValueError Vyhazuje výjimku, pokud je hodnota větší nebo rovna 1000.
def faktorial(x):
    if x >= 1000:
        raise ValueError("Math Error")
    if x == 0:
        return 1
    else:
        return x * faktorial(x-1)

## @brief Funkce pro umocnění čísla na zadanou mocninu.
#  @param x Základ mocniny.
#  @param y Exponent.
#  @return Výsledek umocnění x na y.
def mocnina(x, y):
    if x**y > sys.maxsize:
        raise ValueError("Math Error")
    return x ** y

## @brief Funkce pro výpočet odmocniny z čísla.
#  @param x Základ odmocniny.
#  @param y Exponent (určující stupeň odmocniny).
#  @return Výsledek odmocniny z x s exponentem y.
def odmocnina(x, y):
    return x ** (1/y)

## @brief Funkce pro výpočet sinus z úhlu ve stupních.
#  @param x Úhel ve stupních.
#  @return Sinus úhlu x.
def sin(x):
    return math.sin(math.radians(x))

## @brief Funkce pro výpočet kosinu z úhlu ve stupních.
#  @param x Úhel ve stupních.
#  @return Kosinus úhlu x.
def cos(x):
    return math.cos(math.radians(x))

## @brief Funkce pro výpočet tangens z úhlu ve stupních.
#  @param x Úhel ve stupních.
#  @return Tangens úhlu x.
#  @exception ValueError Vyhazuje výjimku, pokud je úhel dělitelný 90 stupni.
def tan(x):
    if x % 180 == 90:
         raise ValueError("Math Error")
    return math.tan(math.radians(x))

## @brief Funkce pro výpočet cotangens z úhlu ve stupních.
#  @param x Úhel ve stupních.
#  @return Cotangens úhlu x.
def cot(x):
    return 1 / math.tan(math.radians(x))

## @brief Funkce pro vyhodnocení matematického výrazu.
#
#  Tato funkce přijímá matematický výraz jako řetězec a vyhodnocuje ho
#  bez závorek, respektující pořadí operátorů.
#
#  @param expr Matematický výraz.
#  @return Vyhodnocený výraz jako řetězec.
#  @exception ValueError Vyhazuje výjimku, pokud dojde k chybě při matematickém výpočtu.
def eval_expr(expr):
    """
    Evaluates a mathematical expression provided as a string without parentheses.
    The expression respects the precedence of operators.
    """
    try:
        # Definice konstant
        constants = {'π': math.pi, 'e': math.e}

        # Odstranění mezer z výrazu
        expr = expr.replace(" ", "")

        # Rozdělení výrazu na čísla a operátory
        tokens = re.findall(r"\d+\.?\d*|[-+*/^!√]|sin|cos|tan|cot|π|e", expr)

        # Konverze čísel z řetězců na floaty
        tokens = [float(token) if token.replace('.','',1).isdigit() else token for token in tokens]

        # Check for syntax errors
        for i in range(len(tokens) - 1):
            if (tokens[i] in ['sin', 'cos', 'tan', 'cot']) and (i > 0 and isinstance(tokens[i-1], float)):
                raise SyntaxError("Syntax Error")
            if tokens[i] in ['+', '-', '*', '/', '^', '√'] and tokens[i+1] in ['+', '-', '*', '/', '^', '√']:
                raise SyntaxError("Syntax Error")
        
        # Pokud je výraz ve tvaru xpi nebo pix, tak se vyhodí Syntax Error
        for i in range(len(tokens)):
            if tokens[i] == 'π':
                if i > 0 and tokens[i-1].isdigit():
                    raise SyntaxError("Syntax Error")
                if i < len(tokens) - 1 and tokens[i+1].isdigit():
                    raise SyntaxError("Syntax Error")

        # Zpracování goniometrických funkcí, faktoriálu, mocnin a odmocnin
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
                tokens[i:i+2] = [result] # Nahrazení i-1, i, i+1 výsledkem
            elif tokens[i] == '!':
                result = faktorial(tokens[i-1])
                tokens[i-1:i+1] = [result]
            elif tokens[i] == '^':
                if tokens[i-1] > sys.maxsize ** (1 / tokens[i+1]):
                    raise ValueError("Math Error")
                result = mocnina(tokens[i-1], tokens[i+1])
                tokens[i-1:i+2] = [result]
            elif tokens[i] == '√':
                result = odmocnina(tokens[i+1], tokens[i-1])
                tokens[i-1:i+2] = [result]
            elif tokens[i] in constants:
                tokens[i] = constants[tokens[i]]
            i += 1

        # Zpracování násobení a dělení
        i = 0
        while i < len(tokens):
            if tokens[i] in ['*', '/']:
                if tokens[i] == '*':
                    result = nasobenie(tokens[i-1], tokens[i+1])
                else:
                    result = delenie(tokens[i-1], tokens[i+1])
                tokens[i-1:i+2] = [result] 
                i -= 1 # Vrácení se o jeden krok, abychom zkontrolovali novou sekvenci
            i += 1

        # Zpracování sčítání a odčítání
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

        # Vracíme výsledek jako string, když je číslo celé, zobrazuje se bez desatinné části
        result = round(tokens[0],6)
        if result > sys.maxsize:
            raise ValueError("Math Error")
        
        #Pokud je čísle velmi blízké nule, výsledek je nula
        if abs(result) < 1e-6:
            result = 0
        return str(int(result) if result == int(result) else result)
    except ValueError as e:
        return str(e)
    except SyntaxError as e:
        return "Syntax Error"
    except Exception as e:
        return "Syntax Error"