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
def ScoreFinder(names,scores,name):
    i=0.5
    for c in range(len(names)):
        if name.upper()==names[c].upper():
            i=c
    if i==0.5:
        PrintOutput("player not found")
    else:
        strOut=names[i]+' got a score of '+str(scores[i])
        PrintOutput(strOut)
def Union(ls1,ls2):
    ls3=[]
    for c in range(len(ls1)):
        ls3.append(ls1[c])
    for x in range(len(ls2)):
        if ls2[x] not in ls3:
            ls3.append(ls2[x])
    return ls3
def Intersection(ls1,ls2):
    ls3=[]
    for c in range(len(ls1)):
        if ls1[c] in ls2:
            ls3.append(ls1[c])
    return ls3


