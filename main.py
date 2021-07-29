from alive_progress import alive_bar
from pubchempy import Compound
from retrying import retry


class PubchemCrawl():
    def __init__(self, cid_path, out_path, max_workers=4):
        self.cid_path = cid_path
        self.out_path = out_path
        self.max_workers = max_workers
        self.maps = {
            'cid': 'CID',
            'iupac_name': 'IUPACName',
            'isomeric_smiles': 'IsomericSMILES',
            'molecular_formula': 'MolecularFormula',
            'molecular_weight': 'MolecularWeight',
            'synonyms': 'Synonyms',
            'h_bond_donor_count': 'HBondDonorCount',
            'h_bond_acceptor_count': 'HBondAcceptorCount',
        }

    def write_header(self):
        with open(self.out_path, 'w') as f:
            f.write(','.join(self.maps.values())+'\n')

    def get_cid_list(self):
        with open(self.cid_path) as f:
            self.cid_list = [i.strip() for i in f.readlines()]
        self.length = len(self.cid_list)

    @retry
    def get_cmp_data(self, cid):
        comp = Compound.from_cid(cid)
        data = ['"'+str(comp.__getattribute__(key))+'"' for key in self.maps]
        return data

    def write_compound(self, data):
        with open(self.out_path, 'a') as f:
            f.write(','.join(data)+'\n')

    def __main__(self):
        self.write_header()
        self.get_cid_list()
        with alive_bar(self.length) as bar:
            for cid in self.cid_list:
                try:
                    data = self.get_cmp_data(cid)
                    self.write_compound(data)
                    bar()
                except Exception as e:
                    print(f'cid: {cid}, exception: {e}')


if __name__ == '__main__':
    PubchemCrawl('cid.txt', 'data.csv').__main__()
