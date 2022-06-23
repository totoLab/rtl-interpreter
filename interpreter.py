import sys
import lexer
import lib

def transferOperands(command):
    source, destination = command.split("->")
    source, destination = source.strip(), destination.strip()
    return source, destination

def transfer(source, destination): #? ->
    if destination in registers:
        if source in registers:
            value = registers[source]
        elif source.isnumeric():
            value = int(source)

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

ram = {} #TODO

registers = {
    "ACC": 0,
    "T1": 0,
    "T2": 0,
    "T3": 0,
    "T4": 0,
    "MAR": 0,
    "MBR": 0
}

main(Testing=False)