from .db import retrieve_treatment_data_dead, retrieve_treatment_data_dead

def process_medicine(data):
    dict = {}
    for x in data:
        if x[0] not in dict:
            dict[x[0]] = 1
        else:
            dict[x[0]] += 1
    return dict
