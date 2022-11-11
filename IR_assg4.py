from collections import defaultdict
file1 = open('fileName.txt', 'r')
Lines = file1.readlines()
totalWords=[]
for i in Lines:
    words=i.split(' ')    
    totalWords.extend(words)
characters=defaultdict(int)
for i in range(len(totalWords)):
    currentWord=totalWords[i]
    for j in range(len(currentWord)):
        if((currentWord[j]>='a' and currentWord[j]<='z') or (currentWord[j]>='A' and currentWord[j]<='Z')):
            characters[currentWord[j]]+=1
for i in characters:
    print(i,end=" : ")
    print(characters[i])


'''

    Input :

    hi everyone

    Output : 

    h : 1
    i : 1
    e : 3
    v : 1
    r : 1
    y : 1
    o : 1
    n : 1

'''