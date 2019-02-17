import csv

from consts import LOCAL_PATH_MASTER, LOCAL_PATH_PETS


def find_pets(city):
    with open(LOCAL_PATH_MASTER, newline='') as csvfile:
        master = csv.reader(csvfile, delimiter=',')
        city_masters = []
        for row in master:
            if city in row:
                city_masters.append(row[0])

    with open(LOCAL_PATH_PETS, newline='') as csvfile:
        pets_csv = csv.reader(csvfile, delimiter=',')
        pets = {'pets': []}
        for row in pets_csv:
            for master in city_masters:
                if master == row[1]:
                    pets['pets'].append(row[0])

    return pets
