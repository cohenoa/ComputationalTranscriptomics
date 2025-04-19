
import pandas as pd

if __name__ == '__main__':
    file = 'C:/Users/noa/PycharmProjects/BioinformaticsLab/BioinformaticsLab/data/data_outputs/features_Bacillus clausii.pickle'
    species_df = pd.read_pickle(file)
    print(species_df.head())

    file = r'C:\Users\noa\PycharmProjects\BioinformaticsLab\BioinformaticsLab\data\data_outputs\species_Bacillus clausii.pickle'
    species_obj = pd.read_pickle(file)
    print(species_obj.name)
    print(len(species_obj.sequence))