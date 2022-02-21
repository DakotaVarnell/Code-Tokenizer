#Dakota Varnell
#Code Tokenizer that lists what each lexeme of code's equivalent token is


#Read from the file into a list
with open('Tokenizer Lab Repo\Main.jack', 'r') as f:
    file_contents = f.readlines()
with open("tokenizer_output.xml", "w") as out:

    symbols_dict = ["(", ")", "{", "}", "[", "]", ",", ";","=", ".", "+", "-", "*", "/", "&", "|", "~", "<", ">"]
    reserved_words_dict = ["class", "constructor", "method", "function", "int", "boolean", "char", "void", "var", "static", "field", "let", "do", "if", "else", "while", "return", "true", "false", "null", "this","Main"]

    #Check if the word is a symbol
    def symbols(x):
        if x in symbols_dict:
            return True
        else:
            return False

    #Check if the word is a reserved word
    def reservedWords(x):
        
        x = str(x)
        x = x.replace(";", "")
        
        if x in reserved_words_dict:
            return True
        else:
            return False

    #Check if the word is a string constant
    def Stringconstant(x):
        x = str(x)
        if x.startswith("\"") and x.endswith("\""):
            return True
        else:
            return False

    #Check if the word is an integer constant
    def Integerconstant(x):
        x = str(x)
        x = x.replace(";", "")
        if x.isdigit():
            return True
        else:
            return False

    #Check if the word is a boolean constant
    def Booleanconstant(x):
        x = str(x)
        if x == "True" or x == "False":
            return True
        else:
            return False

    for lines in file_contents:
        #Check for the beginning and end of of a multi line comment in the same line
        if "/**" and "*/" in lines:
            # print("start multi-line and end multi line on line: " + str(i))
            # i+=1
            continue
        
        #Check for the ONLY the beginning of a multi line comment on a line
        elif "/**" in lines:
            # print("start multi on one line on line: " + str(i))
            # i+=1
            continue

        #Check whether ONLY the end of the multi-line is in any other line
        elif "*/" in lines:
            # print("end multi-line on line: " + str(i))
            # i+=1
            continue

        #Check for a single line comment
        elif "//" in lines:
            # print("single line comment")
            # i+=1
            continue

        #if its neither a multi line beginning or end, call our functions to determineType
        else:

            #Convert the inputted lines into a string 
            #x = str(x)

            #Split the leftover string into words
            words = lines.split()
            #Iterate through every word within the list of words
            for word in words:
            #if the current word is a symbol return true and then write to the file the symbol
                if symbols(word) == True:
                    print("Symbol: " + word)
                    out.write("<Symbol> " + word + " <Symbol>" + "\n")
                elif reservedWords(word) == True:
                    print("Reserved Word: " + word)
                    out.write("<Reserved_Word> " + word + " <Reserved_Word>"+ "\n")
                #if the current word is a string constant, return true and then write the string const to the file
                elif Stringconstant(word) == True:
                    print("Constant: " + word)
                    out.write("<Constant> " + word + " <Constant>"+ "\n")
                #if the current word is an Int const, return true and then write it to the file
                elif Integerconstant(word) == True:
                    print("Constant: " + word.replace(";", ""))
                    out.write("<Constant> " + word + " <Constant>"+ "\n")
                #if boolean constant retrun true and then write to file
                elif Booleanconstant(word) == True:
                    print("Constant: " + word)
                    out.write("<Constant> " + word + " <Constant>"+ "\n")
                #if its anything else just throw it in as an identifier
                else:
                    print("Identifier: " + word)
                    out.write("<Identifier> " + word + " <Identifier>"+ "\n")







            
           