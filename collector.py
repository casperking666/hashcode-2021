


# input    {intersection ID : [[street,cars]]}

def Data_collection(basic_data:dict, street_dict:dict, car_list:list):
    output = {

    }

    street_count = {}

    #get the count of cars for each street
    for car in car_list:
        for street in car:
            if street_count[street]:
                street_count[street] = street_count[street]+1
            else:
                street_count[street] = 1


    for street, count in dict.items():
        intersection_ID:int = street_dict[street][1]
        output[intersection_ID] = [street,count]

    return output





