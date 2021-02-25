


# input    {intersection ID : [[street,cars]]}

def data_collection(basic_data:dict, street_dict:dict, car_list:list):
    output = {

    }

    street_count = {}

    #get the count of cars for each street
    for car in car_list:
        for street in car:
            if street_count.get(street):
                street_count[street] = street_count[street]+1
            else:
                street_count[street] = 1


    for street, count in dict.items(street_count):
        intersection_ID:str = street_dict[street][1]
        output[intersection_ID] = [street,count]

    return output



if __name__ == '__main__':
    streetdic={"road 1":["1","2",123],"road 2":["2","3",123],"road 3":["4","1",123]}
    car_l = [["road 1","road 2","road 3"],["road 2","road 3"]]
    print(data_collection({},streetdic,car_l))
