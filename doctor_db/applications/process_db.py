from .db import retrieve_treatment_data_dead, retrieve_treatment_data_dead

def process_medicine(data, status):
    if data == None:
        return []
    new_list = []
    for x in data:
        new_list.append([x[9],x[10]])
    print(new_list)
    dict = {}
    for x in new_list:
        if x[0] != None:
            if x[0] not in dict:
                dict[x[0]] = 1
            else:
                dict[x[0]] += 1

    another_list = []
    for x in dict.keys():
        another_list.append([x, dict[x], 'red'])

    print(another_list)
    return another_list
