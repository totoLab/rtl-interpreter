def printRegisters(registers):
    maxLen = 0
    for register in registers:
        if len(register) > maxLen:
            maxLen = len(register)

    for register in registers:
        spacing = " " * (maxLen - len(register))
        value = registers[register]
        print(f"{register}{spacing} | {value}")
def extractArgs(expr, operator):
    args = expr.split(operator)
    for i in range(len(args)):
        args[i] = args[i].strip()
    return args

def extractOperator(expr):
    operators = ["+", "-"]
    for operator in operators:
        if operator in expr:
            return operator

