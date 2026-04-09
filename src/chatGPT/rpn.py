"""
Calculadora RPN (Reverse Polish Notation)

Evalúa expresiones matemáticas utilizando una pila.
Incluye operaciones, funciones, constantes, memoria y manejo de errores.
"""

import math
import sys


class RPNError(Exception):
    """Excepción para errores en la calculadora RPN"""

    pass


def num(t):
    """Convierte un token a número si es posible"""
    try:
        return float(t)
    except ValueError:
        return None


def evaluar(expr):
    """Evalúa una expresión en notación polaca inversa"""

    # ---------------- INICIALIZACIÓN ----------------
    # Se crea la pila principal y las memorias disponibles (00 a 09)
    s = []
    mem = {f"{i:02}": 0.0 for i in range(10)}

    # ---------------- DEFINICIÓN DE OPERACIONES ----------------
    # Diccionario que define operaciones binarias (+, -, *, /, potencia)
    ops = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "*": lambda a, b: a * b,
        "/": lambda a, b: (
            a / b if b != 0 else (_ for _ in ()).throw(RPNError("División por cero"))
        ),
        "yx": lambda a, b: a**b,
    }

    # ---------------- FUNCIONES MATEMÁTICAS ----------------
    # Diccionario con funciones unarias (log, sqrt, trigonométricas, etc.)
    funcs = {
        "sqrt": lambda x: math.sqrt(x),
        "log": lambda x: math.log10(x),
        "ln": lambda x: math.log(x),
        "ex": lambda x: math.exp(x),
        "10x": lambda x: 10**x,
        "1/x": lambda x: (
            1 / x if x != 0 else (_ for _ in ()).throw(RPNError("División por cero"))
        ),
        "+/-": lambda x: -x,
        "sin": lambda x: math.sin(math.radians(x)),
        "cos": lambda x: math.cos(math.radians(x)),
        "tg": lambda x: math.tan(math.radians(x)),
        "asin": lambda x: math.degrees(math.asin(x)),
        "acos": lambda x: math.degrees(math.acos(x)),
        "atg": lambda x: math.degrees(math.atan(x)),
    }

    # ---------------- CONSTANTES ----------------
    # Valores matemáticos predefinidos (pi, e, phi)
    const = {
        "p": math.pi,
        "e": math.e,
        "j": (1 + math.sqrt(5)) / 2,
    }

    # ---------------- PROCESAMIENTO DE TOKENS ----------------
    # Se recorre la expresión separada en tokens
    for t in expr.split():
        n = num(t)

        # ---------------- MANEJO DE NÚMEROS ----------------
        # Si el token es numérico, se agrega a la pila
        if n is not None:
            s.append(n)

        # Si es una constante, se agrega su valor
        elif t in const:
            s.append(const[t])

        # ---------------- MANEJO DE OPERACIONES ----------------
        # Se aplican operaciones binarias utilizando la pila
        elif t in ops:
            if len(s) < 2:
                raise RPNError("Pila insuficiente")
            b, a = s.pop(), s.pop()
            s.append(ops[t](a, b))

        # ---------------- MANEJO DE FUNCIONES ----------------
        # Se aplican funciones matemáticas sobre el último valor
        elif t in funcs:
            if not s:
                raise RPNError("Pila vacía")
            s.append(funcs[t](s.pop()))

        # ---------------- COMANDOS DE PILA ----------------
        # Operaciones sobre la pila: duplicar, intercambiar, eliminar, limpiar
        elif t == "dup":
            if not s:
                raise RPNError("Pila vacía")
            s.append(s[-1])

        elif t == "swap":
            if len(s) < 2:
                raise RPNError("Pila insuficiente")
            s[-1], s[-2] = s[-2], s[-1]

        elif t == "drop":
            if not s:
                raise RPNError("Pila vacía")
            s.pop()

        elif t == "clear":
            s.clear()

        # ---------------- MANEJO DE MEMORIA ----------------
        # Permite guardar (STO) y recuperar (RCL) valores
        elif t == "STO":
            if len(s) < 2:
                raise RPNError("Uso: valor índice STO")
            i = str(int(s.pop())).zfill(2)
            if i not in mem:
                raise RPNError("Memoria inválida")
            mem[i] = s.pop()

        elif t == "RCL":
            if not s:
                raise RPNError("Uso: índice RCL")
            i = str(int(s.pop())).zfill(2)
            if i not in mem:
                raise RPNError("Memoria inválida")
            s.append(mem[i])

        # Si el token no es reconocido
        else:
            raise RPNError(f"Token inválido: {t}")

    # ---------------- VALIDACIÓN FINAL ----------------
    # Se verifica que quede exactamente un valor en la pila
    if len(s) != 1:
        raise RPNError("Resultado inválido")

    return s[0]


def main():
    """Punto de entrada del programa"""
    try:
        expr = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else input("RPN> ")
        print(evaluar(expr))
    except RPNError as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
