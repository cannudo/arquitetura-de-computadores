import functions

word, opcode = functions.getWord()
type = functions.getType(opcode)
dictionary = functions.getDictionary(type)
printable = functions.getPrintable(type, word, dictionary)
print(printable)
