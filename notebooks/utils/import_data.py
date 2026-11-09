import pandas as pd 
import matplotlib.pyplot as plt
from fuzzywuzzy import process 

class ImportData:
    def __init__(self):
        self.kaggle_prefix = '/kaggle/input/datasets/raghavdharwal/amazon-ml-challenge-2026/student_resource/'

    def import_training_data(self):
        ts1 = pd.read_csv('../data/dataset/train/train_source1.tsv', sep='\t')
        ts2 = pd.read_csv('../data/dataset/train/train_source2.tsv', sep='\t')
        ts3 = pd.read_csv('../data/dataset/train/train_source3.tsv', sep='\t')
        ts =  pd.concat([ts1, ts2, ts3], ignore_index=True)
        return ts
    def import_testing_data(self):
        ts1 = pd.read_csv('../data/dataset/test/test_source1.tsv', sep='\t')
        ts2 = pd.read_csv('../data/dataset/test/test_source2.tsv', sep='\t')
        ts3 = pd.read_csv('../data/dataset/test/test_source3.tsv', sep='\t')
        ts =  pd.concat([ts1, ts2, ts3], ignore_index=True)
        return ts
    def import_groundtruth(self):
        gtt = pd.read_csv('../data/dataset/train/train_ground_truth.tsv', sep='\t')
        gtt_exploded = (
            gtt.assign(matched_entity_ids=gtt['matched_entity_ids'].str.split(',')) # Inside of Assign Returns Python list which is then assigned to a column matched_entity_ids. Assign is breifer syntax than (gtt['matched_entity_ids'] = gtt['matched_entity_ids'].str.split(','))
            .explode('matched_entity_ids') # column matched_entity_ids contains lists [A,B,C] for each key. Explode to turn each li and key combination into its own row.
        )
        return gtt_exploded
    
    def import_subset(self, type='US'):
        if type == 'US':
            all_data = self.import_training_data()
            US_data = all_data[all_data['country'] == 'US']
            return US_data
