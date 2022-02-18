#Dakota Varnell
#Code Tokenizer that lists what each lexeme of code's equivalent token is


#Read from the file into a list
from string import whitespace


with open('Tokenizer Lab Repo\Main.jack', 'r') as f:
    file_contents = f.readlines()


symbols = ["(", ")", "{", "}", "[", "]", ",", ";","=", ".", "+", "-", "*", "/", "&", "|", "~", "<", ">"]
reserved_words = ["class", "constructor", "method", "function", "int", "boolean", "char", "void", "var", "static", "field", "let", "do", "if", "else", "while", "return", "true", "false", "null", "this"]



def whiteSpace_comments():
    print("Comment")

def symbols(x):
    if x in symbols:
        return True
    else:
        return False

def reservedWords(x):
    if x in reserved_words:
        return True
    else:
        return False

def constants():
    print("Constants")

def identifiers():
    print("Identifiers")

i = 0
#Read by each word seperated by whitespace
for file in file_contents:
    #split the file into lines
    line = file.split()
    
    #Split the lines into words
    # for word in line:
    #     print(word)

    #if the line is empty we skip that line
    if len(line) == 0:
        continue

    #if we find a single line comment at the start of the line we skip
    elif line[0].startswith("//"):
        print("Comment/WhiteSpace")
        continue
    
    #if we find a multi line comment at the beginning of the line iterate through each line and each word of those lines until we find the end of it
    # elif line[0].startswith("/**"):
        # go = True
        # while go:
        #     if line[i] == "*/":
        #         print(line[i])
        #         go = False
        #     i += 1
    else:
        print("Not Comment")
            
           