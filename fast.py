'''
https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/129907609/synonyms/json
'''
from alive_progress import alive_bar
from retrying import retry
import requests


class PubchemCrawlFast():
    def __init__(self, cid_path, out_path):
        self.cid_path = cid_path
        self.out_path = out_path
        self.property_list = [
            "IUPACName",
            "IsomericSMILES",
            "MolecularFormula",
            "MolecularWeight",
            "HBondDonorCount",
            "HBondAcceptorCount"
        ]

    # def write_header(self):
    #     with open(self.out_path, 'w') as f:
    #         f.write(','.join(self.property_list.values())+'\n')

    def get_cid_list(self):
        with open(self.cid_path) as f:
            self.cid_list = [i.strip() for i in f.readlines()]
        self.length = len(self.cid_list)

    def get_property_from_cid(self):
        self.get_cid_list()
        limit = 300
        api = 'https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/'
        property_str = ','.join(self.property_list)
        return_type = 'json'
        for i in range(limit, self.length+limit, limit):
            cid_str = ','.join(self.cid_list[i-limit:i])
            url = f'{api}{cid_str}/property/{property_str}/{return_type}'
            res = requests.get(url).json()
            prp = res['PropertyTable']['Properties']
            print(len(prp))

    # def get_synonyms_from_cid(self, cid):
    #     api = 'https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/'
    #     url = f'{api}{cid_str}'

    # def get_cmp_data(self, cid):
    #     comp = Compound.from_cid(cid)
    #     data = ['"'+str(comp.__getattribute__(key))+'"' for key in self.maps]
    #     return data

    # def write_compound(self, data):
    #     with open(self.out_path, 'a') as f:
    #         f.write(','.join(data)+'\n')

    # def __main__(self):
    #     self.write_header()
    #     self.get_cid_list()
    #     with alive_bar(self.length) as bar:
    #         for cid in self.cid_list:
    #             try:
    #                 data = self.get_cmp_data(cid)
    #                 self.write_compound(data)
    #                 bar()
    #             except Exception as e:
    #                 print(f'cid: {cid}, exception: {e}')


if __name__ == '__main__':
    PubchemCrawlFast('cid.txt', 'data.json').get_property_from_cid()
