def readfile(filename):
    f = open(filename, "r")
    first_line_list = f.readline().split()
    base_info = {
       "simulation_duration": first_line_list[0],
       "number_of_intersections": first_line_list[1],
       "number_of_streets": first_line_list[2],
       "number_of cars": first_line_list[3],
       "bonus_point":first_line_list,
    }

    street = {}

    for i in range(0, int(base_info["number_of_streets"])):
        street_line_list = f.readline().split()
        street_name = street_line_list.pop(2)
        street[street_name] = street_line_list

    cars = []

    for n in range(0, int(base_info["number_of cars"])):
        car_line_list = f.readline().split()
        car_line_list.pop(0)
        cars.append(car_line_list)

    return base_info, street, cars


if __name__ == '__main__':
    base, street, car = readfile("a.txt")
