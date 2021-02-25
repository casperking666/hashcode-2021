import read_file

# output    {intersection ID : [[street,cars]]}

def data_collection(basic_data:dict, street_dict:dict, car_list:list):
    output = {}
    street_count = {}

    #get the count of cars for each street, put the result into 'street_count' dictionary
    for car in car_list:
        for street in car:
            if street_count.get(street):
                street_count[street] = street_count[street]+1
            else:
                street_count[street] = 1


    # formatting the output
    for street, count in dict.items(street_count):
        intersection_ID = int(street_dict[street][1])
        if output.get(intersection_ID):
            output[intersection_ID] += [[street,count]]
        else:
            output[intersection_ID] = [[street,count]]

    return output


if __name__ == '__main__':
    baseinfo,street_dict,car_info = read_file.readfile("a.txt")
    n = data_collection(baseinfo, street_dict, car_info)
    print(n)
