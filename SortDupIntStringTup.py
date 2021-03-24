# -*- coding: utf-8 -*-

def read_data(path):
    try:
        with open(path, encoding="utf-8") as stops:
            stopslist = stops.readlines()[3:]
            return stopslist

    except FileNotFoundError:
        print ("keine Datei gefunden")
        return None


def prepare_data(inputData):
    stop_dict = {
        "stop_sequence": [],
        "stop_name": []
    }
    for stop in inputData:
        stop = stop.replace(", ", " ")
        stop = stop.replace('"', "")
        stop = stop.replace('\n', "")
        stop = stop.split(";")
        stop_dict["stop_sequence"].append(stop[4])
        stop_dict["stop_name"].append(stop[3])

    return stop_dict


def findDuplicatesAndReplace(data):
    temp = {
        "stop_sequence": [],
        "stop_name": []
    }
    if len(data["stop_sequence"]) > 1:
        for stop_name_i in range(0, len(data["stop_name"])):
            if not dictForEntry(temp, data["stop_name"][stop_name_i]):
                temp["stop_name"].append(data["stop_name"][stop_name_i])
                temp["stop_sequence"].append(data["stop_sequence"][stop_name_i])
                for stop_name_j in range(stop_name_i, len(data["stop_name"])):
                    if data["stop_name"][stop_name_i] == data["stop_name"][stop_name_j] \
                     and data["stop_sequence"][stop_name_i] < data["stop_sequence"][stop_name_j]:
                        temp["stop_sequence"][len(temp["stop_sequence"]) -1] = data["stop_sequence"][stop_name_j]
    return temp


def dictForEntry(temp, stop_name):
    for stop_name_k in temp["stop_name"]:
        if stop_name_k == stop_name:
            return True


def main():

    input_path = 'C:/Temp/STOPs.csv'
    data = read_data(input_path)

    if data is not None:
        data = prepare_data(data)
        data = findDuplicatesAndReplace(data)
        for i in range(0, len(data["stop_name"])):
            print(str(data["stop_sequence"][i]) + " " + data["stop_name"][i])

    else:
        print('error')


if __name__ == '__main__':
    main()