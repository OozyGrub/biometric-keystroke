import readchar
from time import time

END_STRING = '\r'
TEST_WORDS = 'apple ball car doll elephant fish'
weight = dict()

def gatherData(weight):
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
            if(weight != None):
                weight[key] = 1
        else:
            table[key] += timeStamp[i+1] - timeStamp[i]
            count[key] += 1
            if(weight != None):
                weight[key] += 1

    for key in table:
        table[key] /= count[key]
    weight = count
    return table

def verify(template, authen, weight):
    count = 0.00
    sum = 0.00
    for key in authen:
        if(template.get(key) != None):
            # and ' ' not in key and END_STRING not in key
            # sum += abs(template[key] - authen[key])/template[key] * weight[key] * 100 Per
            # count += weight[key]
            # return sum/count
            sum += abs(template[key] - authen[key])
            
            count += 1
    return sum
    



print('Making template...\n')
template = gatherData(None)

print('Authentication...\n')
authen = gatherData(weight)

print('Verification...\n')
diffPercentage = verify(template, authen, weight)
print('Different Percentage: %.2f'%(diffPercentage))