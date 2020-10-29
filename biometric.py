import readchar
from time import time

END_STRING = '\r'
TEST_WORDS = 'apple ball car doll elephant fish'

# Output: digraph dict
def createDigraph(table, count):
    digraph = dict(table)
    for key in digraph:
        digraph[key] /= count[key]
    return digraph

# Output: boolean
def isLastCharOfWord(char):
    if(char == ' ' or char == END_STRING):
        return True
    return False

# Output: list of digraph dict by word
def gatherData():
    print('Please print these words, when finish press enter: \n'+TEST_WORDS+'\n\n')
    
    timeStamp = []
    charInputs = []
    table = dict()
    count = dict()
    output = []

    # Input
    inputKey = ''
    while(inputKey != END_STRING):
        inputKey = readchar.readchar()
        timeStamp.append(time())
        charInputs.append(inputKey)
        print(inputKey)

    for i in range(len(charInputs)-1):
        key = charInputs[i] + charInputs[i+1]
        if(table.get(key) == None):
            table[key] = timeStamp[i+1] - timeStamp[i]
            count[key] = 1
        else:
            table[key] += timeStamp[i+1] - timeStamp[i]
            count[key] += 1
        if(isLastCharOfWord(charInputs[i+1])):
            output.append(createDigraph(table, count))
    return output

# Output: list of diffTime
def verify(template, attemp):
    word_number = min(len(template), len(attemp))
    diffTimeList = []
    for i in range(word_number):
        templateDigraph = template[i] 
        attempDigraph = attemp[i]
        summation = 0.00
        for key in attempDigraph:
            if(templateDigraph.get(key) != None):
                summation += abs(templateDigraph[key] - attempDigraph[key])
        diffTimeList.append(summation)
    return diffTimeList

def printResult(diffTimeList):
    for i in range(len(diffTimeList)):
        print('%d   %.2f'%(i+1, diffTimeList[i]))


print('Making template...\n')
template = gatherData()

print('Authentication...\n')
attemp = gatherData()

print('Verification...\n')
diffTimeList = verify(template, attemp)
printResult(diffTimeList)
