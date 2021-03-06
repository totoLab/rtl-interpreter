import sys
import lexer
import lib

def available(register, overrideInit=False):
    if register in hardware:
        if register in registers:
            return True
        else:
            if overrideInit:
                return True
            raise(RuntimeError(register + " is not initialized."))
    else:
        raise(RuntimeError(register + " is not a register."))

def extractOperator(expr):
    for operator in operatorsALU:
        if operator in expr:
            return operator

def evaluateExpr(args, operator):
    result = -1000
    if len(args) == 1:
        args = int(args[0])
        if operator == "OR":
            result = 0 if args == 0 else 1
        elif operator == "AND":
            result = 0 if args == 0 else 1
    elif len(args) == 2:
        arg1, arg2 = tuple(args)
        if operator == "+":
            result = arg1 + arg2
        elif operator == "-":
            result = arg1 - arg2
        elif operator == "OR":
            result = 1 if any(arg for arg in args if arg != 0) else 0
        elif operator == "AND":
            result = arg1 and arg2
    else:
        raise(RuntimeError("Too many arguments."))

    return result

def ALU(expr):
    operator = extractOperator(expr)
    args = lib.extractArgs(expr, operator)
    for i in range(len(args)):
        if args[i].isnumeric():
            args[i] = int(args[i])
        elif available(args[i]):
            args[i] = registers[args[i]]
    return evaluateExpr(args, operator)

def transferOperands(command):
    source, destination = command.split("->")
    source, destination = source.strip(), destination.strip()
    return source, destination

def extractCondition(expr):
    passrip(), destination.strip()
    if len(operands) != 2:
        raise(RuntimeError(f"Missing operand/s in command: {command}"))
    return operands

def transfer(source, destination): #? ->
    if source.isnumeric():
        value = int(source)
    elif any(ext in source for ext in operatorsALU): 
        value = int(ALU(source))
    else:  
        if available(destination, True):
            if available(source):
                if source in registers:
                    value = registers[source]

    registers[destination] = value

def main(Testing):
    if Testing:
        path = "/home/toto/vscode/uni/rtl/rtl-interpreter/test.rtl"
    else: 
        path = sys.argv[1]
    program, labels = lexer.extract(path)

    ip = 0
    while ip < len(program):
        command = program[ip]
        if "->" in command:
            source, destination = transferOperands(command)
            transfer(source, destination)
            ip += 1
        elif "if" in command and "then" in command:
            condition = extractCondition(command)
            result = ALU(condition)
            if (not result):
                ip = gotoElse()
            else:
                ip += 1
        elif "goto" in command:
            label = extractLabel()
            ip = labels[label]
        elif "0/" in command:
            ip += 1
        else:
            raise(RuntimeError(f"Symbol not recognized: {command}"))

        if Testing: lib.printRegisters(registers, ram)

    lib.printRegisters(registers, ram)

hardware = set(["ACC", "T1", "T2", "T3", "T4", "MAR", "MBR", "A", "B"])
operatorsALU =  ["+", "-", "OR", "AND"]
registers = {}
ram = {}
main(Testing=True)