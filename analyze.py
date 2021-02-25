
def getInput(input):
    inputDic = input
    count = 0
    Denominator = 0

    # outputDic = {}

    probability = []
    # write a func of processing inputs and compute

    # using for loop to get keys
    intersectionIn = inputDic.keys() # it is a list
    inputDetail = inputDic.values() # also a list
    # for i in intersectionIn:
    for intersection_ID,detail in inputDic.items():
        listOfMolecular = []
        Denominator = 0
        for street in detail:
            # print(street[1])
            listOfMolecular.append(street[1])
            Denominator += street[1]
        for h in listOfMolecular:
            # print(h)
            # print(h / Denominator)
            probability.append(h / Denominator)   
        
    # print("name: {name}, probability: {pro}".format(name = nameOfRoad[0], pro = probability[0]))


    for ProbabilityOfItem in probability:
        Denominator += ProbabilityOfItem
    for intersection_ID, detail in inputDic.items():
        for i in detail:
            i[1] = (probability[count] / Denominator) * 6
            count += 1

    return inputDic

    

if __name__ == '__main__':

    inputDic = {1: [['b', 2]],
                2: [['d', 2], ['e', 1]],
                3: [['a', 2]]
                }

    getInput(inputDic)

    print ("字典值 : %s" %  inputDic.items())
