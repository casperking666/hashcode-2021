inputDic = {1:[['b',2]],
        2:[['d',2],['e',1]],
}

# outputDic = {}

nameOfRoad = []
probability = []
# write a func of processing inputs and compute


def getInput():
    # using for loop to get keys
    intersectionIn = inputDic.keys() # it is a list
    inputDetail = inputDic.values() # also a list
    # for i in intersectionIn:
    for i in intersectionIn:
        listOfMolecular = []
        Denominator = 0
        for j in inputDetail:
            for z in range(len(j)):
                nameOfRoad.append(j[z][0])
                listOfMolecular.append(j[z][1])
                Denominator += j[z][1]
        for h in listOfMolecular:
            # print(h)
            probability.append(h / Denominator)
        
    print("name: {name}, probability: {pro}".format(name = nameOfRoad[0], pro = probability[0]))

# def wrapping():
#     # using for loop to put elements in
#     intersectionIn = inputDic.keys()
#     for i in intersectionIn:
#         outputDic = {(int)intersectionID : [["streetName", (int)car_number]];}
#         return outputDic

getInput()
