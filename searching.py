import os
import json

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    file_path = os.path.join(cwd_path, file_name)
    with open ("sequential.json", mode="r") as data_file:
        data = json.load(data_file)
    for key in data.keys():
        if field == key:
            sequential_data = data[field]
            return sequential_data
        else:
            return None

def linear_search(sekvence, cislo):
    i = 0
    count = 0
    list_of_pos = []
    for index, number in enumerate(sekvence):
        if cislo == number:
            list_of_pos.append(index)
            count = +1
            i = i + 1
            count = cislo.count
    return {"positions":list_of_pos, "count":len(list_of_pos)}



def main():
    slovnik = linear_search(sekvence=[2,5,12,2,5,4,7,36], cislo=2)


if __name__ == '__main__':
    main()