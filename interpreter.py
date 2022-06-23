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
def transferOperands(command):
    source, destination = command.split("->")
    source, destination = source.strip(), destination.strip()
    return source, destination

def transfer(source, destination): #? ->
    if source.isnumeric():
        value = int(source)
    elif any(ext in source for ext in ["+", "-"]): 
        value = int(ALU(source))
    else:  
        if available(destination, True):
            if available(source):
                if source in registers:
                    value = registers[source]

    registers[destination] = value
    else:
        print(destionation + " is not a register.")

def main(Testing):
    path = sys.argv[1]
    program, labels = lexer.extract(path)

    ip = 0
    while ip < len(program):
        command = program[ip]
        if "->" in command:
            source, destination = transferOperands(command)
            transfer(source, destination)
        #TODO finish implementing syntax

        if Testing: print(registers)

        ip += 1

    lib.printRegisters(registers)

hardware = set(["ACC", "T1", "T2", "T3", "T4", "MAR", "MBR", "A", "B"])

registers = {}

main(Testing=False)