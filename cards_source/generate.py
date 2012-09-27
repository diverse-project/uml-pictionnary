import random

#number of cards in a row in the document
nbCardsPerRow = 4

#the text files that contains the descriptions that are to guess
txtFiles = [open('use_cases_diagrams.txt', 'r'),
            open('class_diagrams.txt', 'r'),
            open('sequence_diagrams.txt', 'r')];

#returns true iff all the descriptions of the text files have been used
def generationFinished(txtFiles):
    for f in txtFiles:
        if not f.closed:
            return False;
    
    return True;



#pick a description in the file txtFile. If the file has been completely read, return "Tirez une autre carte"
def txtFileLineReturn(txtFile):
    if txtFile.closed:
        return "Tirez une autre carte"
    else:
        line = txtFile.readline()
        if line == "":
            txtFile.close()
            return "Tirez une autre carte"
        else:
            return line
        
#generate the file "cards.tex" that contains the latex descriptions of the cards
def generate():

    #to count the number of cards on a row (limited by nbCardsPerRow)
    nbCards = 1
    latexCardsFile = open('generated_cards.tex','w')
    
    while not generationFinished(txtFiles):
        if nbCards > nbCardsPerRow:
            nbCards = 1
            latexCardsFile.write("\n\\newrow\n")
            
        
        latexCardsFile.write('\\umlpiccard')
        for txtFile in txtFiles:
            latexCardsFile.write("\n{")
            latexCardsFile.write(txtFileLineReturn(txtFile))
            latexCardsFile.write("}")

        #the description in front of "?" is randomly chosen
        latexCardsFile.write("\n{")
        latexCardsFile.write(txtFileLineReturn(txtFiles[random.randint(0, 2)]))
        latexCardsFile.write("}\n")

        nbCards = nbCards + 1


    latexCardsFile.close();

    

generate()
