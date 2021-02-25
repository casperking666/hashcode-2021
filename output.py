
def output(output_result:dict):


    f = open("output.txt", "w")
    elements = len(output_result)
    stt = str(elements) + "\n"
    f.write(stt)

    for key in output_result:
        stt2 = str(len(output_result[key])) + "\n"
        f.write(stt2)
        for values in output_result[key]:
            strin = str(values[0])+" "+ str(values[1]) + "\n"
            f.write(strin)

    f.close()




if __name__ == '__main__':
    content = {0:[["road1",12]],1:[["road 3",15],["road 5",20]]}
    output(content)






"""inputDic = {'intersection': [['streetName', 'time'], []], 'intersection2': [['streetName', 'time']]}


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
>>>>>>> Add files via upload
"""
