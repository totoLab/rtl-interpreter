def printRegisters(registers, ram):
    maxLen = 0
    for register in registers:
        if len(register) > maxLen:
            maxLen = len(register)

    for register in registers:
        spacing = " " * (maxLen - len(register))
        value = registers[register]
        print(f"{register}{spacing} | {value}")

    print("RAM:")
    if len(ram) == 0:
        print("Unused.")
    else:
        for addr in ram:
            spacing = " " * (8 - len(addr))
            value = ram[addr]
            print(f"{addr}{spacing} | {value}")
    print("-------")


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

