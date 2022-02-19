#Dakota Varnell
#Code Tokenizer that lists what each lexeme of code's equivalent token is


#Read from the file into a list
from operator import truediv


with open('Tokenizer Lab Repo\Main.jack', 'r') as f:
    file_contents = f.readlines()
 

symbols = ["(", ")", "{", "}", "[", "]", ",", ";","=", ".", "+", "-", "*", "/", "&", "|", "~", "<", ">"]
reserved_words = ["class", "constructor", "method", "function", "int", "boolean", "char", "void", "var", "static", "field", "let", "do", "if", "else", "while", "return", "true", "false", "null", "this"]

test = "string"

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

def constants(x):
    x = str(x)
    print(x)
    if x.startswith("\"") and x.endswith("\""):
        return True
    else:
        return False
    

def identifiers():
    print("Identifiers")

def determineType(x):
    print(x)

i = 1 

# #Iterate through our entire file
for lines in file_contents:
    #Check for the beginning and end of of a multi line comment in the same line
    if "/**" and "*/" in lines:
        print("start multi-line and end multi line on line: " + str(i))
        i+=1
    
    #Check for the ONLY the beginning of a multi line comment on a line
    elif "/**" in lines:
        print("start multi on one line on line: " + str(i))
        i+=1

    #Check whether ONLY the end of the multi-line is in any other line
    elif "*/" in lines:
        print("end multi-line on line: " + str(i))
        i+=1

    #Check for a single line comment
    elif "//" in lines:
        print("single line comment")
        i+=1

    #if its neither a multi line beginning or end, call our determineType function
    else:
        words = lines.split()
        determineType(words)

    
    
        
        

i +=1






            
           