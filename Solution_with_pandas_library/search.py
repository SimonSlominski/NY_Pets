import pandas as pd

from consts import LOCAL_PATH_MASTER, LOCAL_PATH_PETS

def merge_tables(master_csv, pets_csv):
    master_df = pd.read_csv(LOCAL_PATH_MASTER, delimiter=',')
    pets_df = pd.read_csv(LOCAL_PATH_PETS, delimiter=',')

    master_df.columns=['master', 'address'] # change the name of the column in master.csv, unify the names with pets.csv
    return master_df.merge(pets_df, on='master')


def find_pets(city):
    df = merge_tables(LOCAL_PATH_PETS, LOCAL_PATH_MASTER) # get merged data
    filtered_data = df[df.address == city] # get dataframe for desired city

    pets = {'pets': []}
    for row in filtered_data.itertuples():
        pet_name = row.name
        pets['pets'].append(pet_name)

    return pets
