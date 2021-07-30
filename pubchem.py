import os, csv, json, requests


class PubchemCrawlFast():
    def __init__(self, cid_path, out_path):
        """Initialization function.

        Args:
            cid_path (str): Input file path of cid list
            out_path (str): Output file path of crawled data 
        """
        self.cid_path = cid_path
        self.out_path = out_path
        self.property_list = [
            'IUPACName',
            'IsomericSMILES',
            'MolecularFormula',
            'MolecularWeight',
            'HBondDonorCount',
            'HBondAcceptorCount'
        ]

    def get_cid_list(self):
        """Get the cid list from the local file
        """
        if os.path.exists(self.cid_path):
            with open(self.cid_path) as f:
                self.cid_list = [i.strip() for i in f.readlines()]
        else:
            self.cid_list = []
            cid = input('Please inpute the CID list below: \n')
            while cid != '':
                self.cid_list.append(cid)
                cid = input()
        self.length = len(self.cid_list)

    def get_property_from_cid(self):
        """Get the property from cid
        """
        limit = 300
        api = 'https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/'
        property_str = ','.join(self.property_list)
        return_type = 'json'
        self.prp = []
        for i in range(limit, self.length+limit, limit):
            cid_str = ','.join(self.cid_list[i-limit:i])
            url = f'{api}{cid_str}/property/{property_str}/{return_type}'
            res = requests.get(url).json()
            self.prp += res['PropertyTable']['Properties']

    def get_synonyms_from_cid(self):
        """Get the synonym from cid
        """
        limit = 300
        api = 'https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/'
        return_type = 'json'
        self.syn = []
        for i in range(limit, self.length+limit, limit):
            cid_str = ','.join(self.cid_list[i-limit:i])
            url = f'{api}{cid_str}/synonyms/{return_type}'
            res = requests.get(url).json()
            self.syn += res['InformationList']['Information']
        for i in range(len(self.syn)):
            if 'Synonym' not in self.syn[i]:
                self.syn[i]['Synonym'] = []

    def save_as_csv(self, data):
        """Save the crawled data in CSV format
        """
        csv_name = self.out_path.split('.')[0]+'.csv'
        header_list = ['CID']+self.property_list+['Synonym']
        # with open(csv_name, 'w') as f:
        #     f.write(','.join(header_list)+'\n')
        # with open(csv_name, 'a') as f:
        #     for item in data:
        #         line = ['"'+str(item[each])+'"' for each in header_list]
        #         f.write(','.join(line)+'\n')
        with open(csv_name,'w', newline='') as f:
            writer = csv.DictWriter(f, header_list)
            writer.writeheader()
            writer.writerows(data)

    def __main__(self):
        print('Getting CID list: ')
        self.get_cid_list()
        print('CID list acquisition is complete!')
        print('--------------------------------------------')
        print('Querying property list: ')
        self.get_property_from_cid()
        print('Property list query is complete!')
        print('--------------------------------------------')
        print('Querying synonym: ')
        self.get_synonyms_from_cid()
        print('Synonym query is complete!')
        print('--------------------------------------------')
        dt = {
            'InfoList': {
                'Info': [dict(d1, **d2) for d1, d2 in zip(self.prp, self.syn)]
            }
        }
        json_str = json.dumps(dt, indent=2)
        print('The data is being written to the JSON file: ')
        with open(self.out_path, 'w') as f:
            f.write(json_str)
        print('Finished writing the JSON file! ')
        print('--------------------------------------------')
        print('The data is being written to the CSV file: ')
        self.save_as_csv(dt['InfoList']['Info'])
        print('Finished writing the CSV file! ')
        os.system('pause')


if __name__ == '__main__':
    PubchemCrawlFast('cid.txt', 'data.json').__main__()
