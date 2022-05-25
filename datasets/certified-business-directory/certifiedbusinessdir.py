import pandas as pd, numpy as np, matplotlib
from os import path
from rich import print
from matplotlib import pyplot as plt

def main():
    dc = DataCruncher('\\businesses.csv')
    dc.run()

class DataCruncher:
    def __init__(self, dataset_link):
        dirname = path.dirname(__file__)
        self.datalink = dirname + dataset_link
        self.full_dataset = pd.read_csv(self.datalink)
        # each business code ID exists as a key, and 
        # its value is the # of businesses in that category
        self.cob_category_codes = dict()

    def run(self):
        self.get_women_data()
        self.get_business_categories()
        print(sorted(self.cob_category_codes.items(), key=lambda item: item[1]))

    def get_women_data(self):
        df = pd.read_csv(self.datalink)
        self.women_owned_businesses = df.query('mbe_wbe_cert == "WBE" | mbe_wbe_cert == "WMBE"')

    def get_business_categories(self):
        for i, business in self.women_owned_businesses.iterrows():
            # for category in ("cob_category_codes1", "cob_category_codes2", "cob_category_codes3"):
            for category in ("cob_category_codes1",):
                cell_data = str(business[category])
                #skip empty cells
                if cell_data == 'nan': continue
                try: #increment the slot for the business category
                    self.cob_category_codes[cell_data] += 1
                except KeyError:
                    #this is the first occurance of the business type
                    self.cob_category_codes[cell_data] = 1

if __name__=="__main__":
    main()

