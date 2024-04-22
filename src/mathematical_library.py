## @file mathematical_library.py
#  @brief Implementation of mathematical functions.
#
#  This file contains the implementation of various mathematical functions,
#  such as addition, subtraction, multiplication, division, factorial, power,
#  square root and goniometric functions.
import math
import re
import sys

## @brief Function for adding two numbers.
#  @param x First enumerator.
#  @param y Second enumerator.
#  @return Sum of x and y
def scitanie(x, y):
    return x + y

## @brief Functions for subtracting two numbers.
#  @param x Minuend.
#  @param y Subtrahend.
#  @return The difference between x and y.
def odcitanie(x, y):
    return x - y

## @brief Functions for multiplying two numbers.
#  @param x First factor.
#  @param y Second factor.
#  @return The product of x and y.
def nasobenie(x, y):
    return x * y

## @brief Functions for dividing two numbers.
#  @param x Dividend.
#  @param y Divisor.
#  @return Podíl x a y.
#  @exception ValueError Throws an exception if the divisor is zero.
def delenie(x, y):
    if y == 0:
        raise ValueError("Math Error")
    return x / y

## @brief Functions for calculating the factorial.
#  @param x The value for which the factorial is to be calculated.
#  @return Factorial of the value of x.
#  @exception ValueError Throws an exception if the value is greater than the recursion limit.
def faktorial(x):
    if x >= 1000:
        raise ValueError("Math Error")
    if x == 0:
        return 1
    else:
        return x * faktorial(x-1)

## @brief Function to exponentiate a number by a specified power.
#  @param x Basis of power.
#  @param y Exponent.
#  @return Result of x to the power of y.
def mocnina(x, y):
    if x**y > sys.maxsize:
        raise ValueError("Math Error")
    return x ** y

## @brief Functions for calculating the square root of a number.
#  @param x Base square root
#  @param y Exponent (determining the degree of the square root)
#  @return The result of the square root of x with exponent y.
def odmocnina(x, y):
    return x ** (1/y)

## @brief Functions for calculating the sine of an angle in degrees.
#  @param x Angle in degrees.
#  @return Sine of angle x.
def sin(x):
    return math.sin(math.radians(x))

## @brief Functions for calculating the cosine of an angle in degrees.
#  @param x Angle in degrees.
#  @return Cosine of angle x.
def cos(x):
    return math.cos(math.radians(x))

## @brief Functions for calculating tangents from an angle in degrees.
#  @param x Angle in degrees.
#  @return Tangent of angle x.
#  @exception ValueError Throws an exception if the angle is divisible by 90 degrees (undefined values).
def tan(x):
    if x % 180 == 90:
         raise ValueError("Math Error")
    return math.tan(math.radians(x))

## @brief Functions for evaluating a mathematical expression.
#
#  This function accepts a mathematical expression as a string
#  and evaluates it without parentheses, respecting the order of the operators.
#
#  @param expr Mathematical expression
#  @return Evaluated expression as a string.
#  @exception ValueError Throws an exception if there is an error in the mathematical calculation.
def eval_expr(expr):
   
    try:
        # Definition of constants
        constants = {'π': math.pi, 'e': math.e}

        # Remove spaces from an expression
        expr = expr.replace(" ", "")

        # Splitting an expression into numbers and operators
        tokens = re.findall(r"\d+\.?\d*|[-+*/^!√]|sin|cos|tan|π|e", expr)

        # Converting numbers from strings to floats
        tokens = [float(token) if token.replace('.','',1).isdigit() else token for token in tokens]

        # Check for syntax errors
        for i in range(len(tokens) - 1):
            if (tokens[i] in ['sin', 'cos', 'tan']) and (i > 0 and isinstance(tokens[i-1], float)):
                raise SyntaxError("Syntax Error")
            if tokens[i] in ['+', '-', '*', '/', '^', '√'] and tokens[i+1] in ['+', '-', '*', '/', '^', '√']:
                raise SyntaxError("Syntax Error")
        
        # If the expression is of the form xpi or pix, a Syntax Error is thrown
        for i in range(len(tokens)):
            if tokens[i] == 'π':
                if i > 0 and tokens[i-1].isdigit():
                    raise SyntaxError("Syntax Error")
                if i < len(tokens) - 1 and tokens[i+1].isdigit():
                    raise SyntaxError("Syntax Error")

        # Processing goniometric functions, factorial, powers and square roots
        i = 0
        while i < len(tokens):
            if tokens[i] in ['sin', 'cos', 'tan']:
                if tokens[i] == 'sin':
                    result = sin(tokens[i+1]) 
                elif tokens[i] == 'cos':
                    result = cos(tokens[i+1])
                elif tokens[i] == 'tan':
                    result = tan(tokens[i+1])
                tokens[i:i+2] = [result] # Replacing i-1, i, i+1 with the result
            elif tokens[i] == '!':
                result = faktorial(tokens[i-1])
                tokens[i-1:i+1] = [result]
            elif tokens[i] == '^':
                if tokens[i+1] == 0:
                    result = 1
                elif tokens[i-1] > sys.maxsize ** (1 / tokens[i+1]):
                    raise ValueError("Math Error")
                result = mocnina(tokens[i-1], tokens[i+1])
                tokens[i-1:i+2] = [result]
            elif tokens[i] == '√':
                result = odmocnina(tokens[i+1], tokens[i-1])
                tokens[i-1:i+2] = [result]
            elif tokens[i] in constants:
                tokens[i] = constants[tokens[i]]
            i += 1

        # Processing multiplication and division
        i = 0
        while i < len(tokens):
            if tokens[i] in ['*', '/']:
                if tokens[i] == '*':
                    result = nasobenie(tokens[i-1], tokens[i+1])
                else:
                    result = delenie(tokens[i-1], tokens[i+1])
                tokens[i-1:i+2] = [result] 
                i -= 1 # Going back one step to check the new sequence
            i += 1

        # Processing of additions and subtractions
        i = 0
        while i < len(tokens):
            if tokens[i] in ['+', '-']:
                if tokens[i] == '+':
                    if i == 0:
                        result = scitanie(0, tokens[i+1])
                    else:
                        result = scitanie(tokens[i-1], tokens[i+1])
                else:
                    if i == 0:
                        result = odcitanie(0, tokens[i+1])
                    else:
                        result = odcitanie(tokens[i-1], tokens[i+1])
                if i > 0:
                    tokens[i-1:i+2] = [result]
                    i -= 1
                else:
                    tokens[i:i+2] = [result]
            i += 1

        # Returns the result as a string, if the number is integer, it is displayed without the decimal part
        result = round(tokens[0],6)
        if result > sys.maxsize:
            raise ValueError("Math Error")
        
        # If the number is very close to zero, the result is zero
        if abs(result) < 1e-6:
            result = 0
        return str(int(result) if result == int(result) else result)
    except ValueError as e:
        return str(e)
    except SyntaxError as e:
        return "Syntax Error"
    except Exception as e:
        return "Syntax Error"