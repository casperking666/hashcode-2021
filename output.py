inputDic = {'intersection': [['streetName', 'time'], []], 'intersection2': [['streetName', 'time']]}


def writeFile(inputDic):
    output = open('file.txt', 'w')
    length = len(inputDic)
    output.write('%d\n' % length)
    count = 0
    for i in inputDic:
        temp = list(inputDic.keys())[i]
        output.write(str(temp))
        for j in inputDic[i]:
            if isinstance(inputDic[i][j], list):
                count += 1
        output.write('%d\n' % count)


writeFile(inputDic)
