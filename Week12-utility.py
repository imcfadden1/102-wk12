def PrintOutput(string1):
    print("OUTPUT", string1)


def LoadFile(str1):
    out=[]
    with open(str1,'r') as file:
        for row in file:
            out.append(row)
    PrintOutput(out)

def UpdateString(str1,char,i):
    str2=''
    for c in range(len(str1)):
        if c==i:
            str2+=char
        else:
            str2+=str1[c]
    PrintOutput(str2)

def FindWordCount(ls1,str1):
    count=0
    for c in range(len(ls1)):
        if ls1[c]==str1:
            count+=1
    PrintOutput(count)
