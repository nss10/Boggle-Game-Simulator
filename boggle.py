# author : Sai Shanmukha Narumanchi
import random
dim=4
scoreDict = {3: 1, 4: 1, 5: 2, 6: 3, 7: 5}

def populateWordCollection():
    wordCollection = []
    with open("words.txt") as f:
        return [line.strip().upper() for line in f]  

def isAdjacent(pos,word,boggleTray,visited):
    if(len(word)==0):
        return True
    x,y=pos
    if((x not in range(dim) or y not in range(dim))):
        return False
    for i in range(x-1,x+2):
        for j in range(y-1,y+2):
            if((x==i and y==j) or (i not in range(dim) or j not in range(dim))):
                continue
            if(word[0]==boggleTray[i][j] or word[0:2] == boggleTray[i][j] and not visited[i][j]):
                visited[i][j]=True
                # print(boggleTray[i][j],i,j)
                nextWord = word[1:] if boggleTray[i][j]!='QU' else word[2:]
                if(isAdjacent((i,j), nextWord,boggleTray, visited)):
                    return True
                else:
                    visited[i][j]=False
                    # print(boggleTray[i][j],i,j,' X')
    return False

def isInGrid(word,boggleTray):
    visited=[[False for i in range(dim)] for j in range(dim)]
    for i in range(dim):
        for j in range(dim):
            if(boggleTray[i][j]==word[0] or word[0:2] == boggleTray[i][j]):
                # print(boggleTray[i][j],i,j)
                visited[i][j]=True
                nextWord = word[1:] if boggleTray[i][j]!='QU' else word[2:]
                if(isAdjacent((i,j), nextWord,boggleTray, visited)):
                    return True
                else:
                    visited[i][j]=False
                    # print(boggleTray[i][j],i,j,' X')
    return False

def computeScore(word,boggleTray):
    if(word not in wordCollection):
        return -1
    if(len(word)<3):
        return 0
    if(isInGrid(word,boggleTray)):
        if(len(word)>7):
            return 11
        return scoreDict[len(word)]

def printOutput(word,score):
    if score is None:
        print('The word '+word+' is not present in the grid.')
    elif (score<0):
        print('The word '+word+' is not a word.')
    elif(score<1):
        print('The word '+word+' is too short.')
    elif(score<2):
        print('The word '+word+' is worth 1 point.')
    else:
        print('The word '+word+' is worth '+str(score)+' points.')


def getRandomBoggleTray(diceCombination):
    return [[diceCombination[i+j][random.randint(0,len(diceCombination[0]))] for i in range(dim)] for j in range(dim)]


def printBoggleTray(boggleTray):
    for i in range(dim):
        for j in range(dim):
            print('['+boggleTray[i][j] + '] ',end='')
        print()


def readInput():
    wordList=[]
    while True:
        word = input().upper()
        if(word=='X'):
            break
        wordList.append(word)
    return wordList


if __name__ == "__main__":
    wordCollection = populateWordCollection()
    diceCombination = [['A', 'E', 'A', 'N', 'E', 'G'],['A', 'H', 'S', 'P', 'C', 'O'],['A', 'S', 'P', 'F', 'F', 'K'], ['O', 'B', 'J', 'O', 'A', 'B'], ['I', 'O', 'T', 'M', 'U', 'C'], ['R', 'Y', 'V', 'D', 'E', 'L'], ['L', 'R', 'E', 'I', 'X', 'D'], ['E', 'I', 'U', 'N', 'E', 'S'],['W', 'N', 'G', 'E', 'E', 'H'],['L', 'N', 'H', 'N', 'R', 'Z'], ['T', 'S', 'T', 'I', 'Y', 'D'],['O', 'W', 'T', 'O', 'A', 'T'],['E', 'R', 'T', 'T', 'Y', 'L'],['T', 'O', 'E', 'S', 'S', 'I'],['T', 'E', 'R', 'W', 'H', 'V'],['N', 'U', 'I', 'H', 'M', 'QU']]
    boggleTray = getRandomBoggleTray(diceCombination)
    printBoggleTray(boggleTray)
    print("Start typing your words! (press enter after each word and enter 'X' when done):")
    wordList = readInput()
    totalScore=0
    for i,word in enumerate(wordList):
        if(word in wordList[:i]):
            print('The word '+word+' has already been used.')
            continue
        score = computeScore(word,boggleTray)
        totalScore+=score if score is not None and score > 0 else 0
        printOutput(word,score)
    print('Your total score is '+str(totalScore)+' points!')
