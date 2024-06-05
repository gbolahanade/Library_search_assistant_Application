import csv


def read_csv(file_name):
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        data = list(reader)
    return data


def get_location(classmark, classmarks_data):
    for row in classmarks_data:
        if classmark in row[0]:
            return row[1]
    return "Location not found"


def get_subject_names(classmark, subjects_data):
    names = []
    for row in subjects_data:
        if classmark == row[1]:
            names.append(row[0])
    return names


