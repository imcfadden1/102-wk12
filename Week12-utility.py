def PrintOutput(string1):
    print("OUTPUT", string1)
PrintOutput("Hello World")

def LoadFile(str1):
    out=[]
    with open(str1,'r') as file:
        for row in file:
            out.append(row)
    PrintOutput(out)

LoadFile('Caged.txt')
