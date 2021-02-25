# inputDic = {'intersection': [['streetName', 'time'], []], 'intersection2': [['streetName', 'time']]}


def writeFile(inputDic):
    output = open('file.txt', 'w')
    output.write(str(len(inputDic)) + "\n")
    for i in inputDic.keys():
        output.write(i+"\n")
        for j in inputDic[i]:
            output.write("{0} {1}\n".format(j[0], j[1]))
    output.close()
