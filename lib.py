def printRegisters(registers):
    maxLen = 0
    for register in registers:
        if len(register) > maxLen:
            maxLen = len(register)

    for register in registers:
        spacing = " " * (maxLen - len(register))
        value = registers[register]
        print(f"{register}{spacing} | {value}")