import readchar
from time import time

END_STRING = '\r'
TEST_WORDS = 'apple ball car doll elephant fish'

def gatherData():
    print('Please print these words, when finish press enter: \n'+TEST_WORDS+'\n\n')
    
    timeStamp = []
    charInputs = []
    table = dict()
    count = dict()

    # Input
    inputKey = ''
    while(inputKey != END_STRING):
        inputKey = readchar.readchar()
        timeStamp.append(time())
        charInputs.append(inputKey)
        print(inputKey)
    # print(timeStamp)
    # print(charInputs)

    for i in range(len(charInputs)-1):
        key = charInputs[i]+charInputs[i+1]
        if(table.get(key) == None):
            table[key] = timeStamp[i+1] - timeStamp[i]
            count[key] = 1
        else:
            table[key] += timeStamp[i+1] - timeStamp[i]
            count[key] += 1

    for key in table:
        table[key] /= count[key]
    return table

def verify(template, authen):
    count = 0.00
    sum = 0.00
    for key in authen:
        if(template.get(key) != None):
            sum += abs(template[key] - authen[key])
            count += 1
    return sum
    



print('Making template...\n')
template = gatherData()

print('Authentication...\n')
authen = gatherData()

print('Verification...\n')
diffTime = verify(template, authen)
print('Summation of diff time: %.2f'%(diffTime))