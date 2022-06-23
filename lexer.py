
def endsWith(line, string):
    len1 = len(line)
    len2 = len(string)
    if line[len1 - len2:] == string:
        return line[:len1 - len2]
    else:
        return line

def extract(path):
    if path == endsWith(path, ".rtl"):
        print("Invalid extension.")
        exit(1)
    with open(path, "r") as f:
        program = []
        for line in f.read().splitlines():
            line = line.strip()
            line = endsWith(line, ",")
            for command in line.split(","):
                command = command.strip()
                if ":" in command:
                    label, command = command.split(":")
                    label, command = label.strip(), command.strip()
                    if len(label) > 0:
                        program.append(label + ":")
                if len(command) > 0:
                    program.append(command)
    
    labels = {}
    for ip in range(len(program)):
        word = program[ip]
        if word != endsWith(word, ':'):
            labels[word[:-1]] = ip

    return program, labels