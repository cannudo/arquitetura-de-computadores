def getWord():
    word = input()
    opcode = word[0:6]
    return word, opcode

def getType(opcode):
    if opcode == "000000":
        type = "R"
    elif opcode != "000000" and opcode[0:6] != "000001" and opcode[0:4] != "0100":
        type = "I"
    elif opcode[0:4] == "0100":
        type = "J"
    return type

def getDictionary(type):
    dictionary = {}
    constructor = open(type, "r")
    for line in constructor:
        function, code = line.split(";")
        dictionary[code] = function
    constructor.close()
    return dictionary

def getPrintable(type, word, dictionary):
    if type == "R":
        rs = int(word[6:11], 2)
        rt = int(word[11:16], 2)
        rd = int(word[16:21], 2)
        shamt = int(word[21:26], 2)
        funct = word[26:32]
        if funct + "\n" in dictionary.keys():
            key = dictionary[funct + "\n"]
            printable = "{} ${}, ${}, ${}, ${}".format(key, rs, rt, rd, shamt)
        else:
            printable = ""
    elif type == "I":
        funct = word[0:6]
        rs = int(word[6:11], 2)
        rt = int(word[11:16], 2)
        imm = int(word[16:32], 2)
        if funct + "\n" in dictionary.keys():
            key = dictionary[funct + "\n"]
            printable = "{} ${}, ${}, ${}".format(key, rs, rt, imm)
        else:
            printable = ""
    elif type == "J":
        funct = word[0:6]
        adress = word[6:32]
        if funct + "\n" in dictionary.keys():
            key = dictionary[funct + "\n"]
            printable = "{} ${}".format(key, adress)
        else:
            printable = ""
    return printable
