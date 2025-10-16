# calculadora minimalista sem eval

from typing import List, Union

Token = Union[float, str]

def tokenize(expr: str) -> List[Token]:
    tokens: List[Token] = []
    num = ""
    for ch in expr:
        if ch.isdigit() or ch == ".":
            num += ch
        else:
            if num:
                tokens.append(float(num))
                num = ""
            if ch in "+-*/":
                tokens.append(ch)
            # ignora espacos e caracteres nao suportados
    if num:
        tokens.append(float(num))
    return tokens


def compute(tokens: List[Token]) -> float :
# primeira passagem: multiplicacao e divisao (maior precedencia)
    i = 0
    while i < len(tokens):
        tk = tokens[i]
        if tk == "*":
            tokens[i - 1 : i + 2] = [float(tokens[i - 1]) * float(tokens[i + 1])]
        elif tk == "/":
            tokens[i - 1 : i + 2] = [float(tokens[i - 1]) / float(tokens[i + 1])]
        else:
            i += 1

# segunda passagem: adicao e subtracao (esquerda->direita)
    result = float(tokens[0])
    i = 1
    while i < len(tokens):
        op = tokens[i]
        val = float(tokens[i + 1])
        if op == "+":
            result += val
        elif op == "-":
            result -= val
        i += 2
    return result


def evaluate(expr: str) -> float:
    return compute(tokenize(expr))


if __name__ == "__main__":
    expr = input("Expr: ")
    print(evaluate(expr))
