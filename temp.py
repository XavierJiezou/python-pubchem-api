'''Reference
https://github.com/simonholmes001/pubchem_api
'''
import pubchem_api
import pandas as pd
from tqdm import tqdm
from pubchem_api import pubchem_api
base_url = "https://pubchem.ncbi.nlm.nih.gov/rest/pug/"
compound_cid_selector = "compound/cid/"
with open('cid.txt') as f:
    # list of molecules to retrieve simultanesouly
    cid_list = [i.strip() for i in f.readlines()]
for cid in tqdm(cid_list):
    search_id = f"{cid}/"  # compound cid for molecule in question
    property = "property/"
    property_list = ["IUPACName", "IsomericSMILES", "CanonicalSMILES", "MolecularFormula", "MolecularWeight",
                     "HBondDonorCount", "HBondAcceptorCount"]  # list of properties to retrieve for all molecules given above
    # indicates that we will retrieve all of the above chemical properties for all compounds
    output_property = ','.join(property_list)+"/"
    output_format = "CSV"  # output format from the REST API call
    output_file_name = "test_data"  # output data will be saved as 'test_data.csv'
    pubchem_api.ApiGetFeatures(base_url, compound_cid_selector, search_id, property, output_property, output_format, output_file_name)
df = pd.read_csv('test_data.csv')
df = df.iloc[::2]
df.to_csv('data.csv', index=0)
# import pubchem_api
# from pubchem_api import pubchem_api
# base_url = "https://pubchem.ncbi.nlm.nih.gov/rest/pug"
# compound_cid_selector = "compound/cid/"
# with open('cid.txt') as f:
#     cid_list = [i.strip() for i in f.readlines()]  # list of molecules to retrieve simultanesouly
# cid_list = cid_list[0]
# search_id = ','.join(cid_list)+"/"  # concatenation of molecule cid's
# property = "property/"
# property_list = ["IUPACName", "IsomericSMILES", "CanonicalSMILES", "MolecularFormula", "MolecularWeight", "HBondDonorCount",
#                  "HBondDonorCount", "HBondAcceptorCount"]  # list of properties to retrieve for all molecules given above
# # indicates that we will retrieve all of the above chemical properties for all compounds
# output_property = ','.join(property_list)+"/"
# output_format = "CSV"  # output format from the REST API call
# output_file_name = "test_data"  # output data will be saved as 'test_data.csv'
# pubchem_api.ApiGetFeatures(base_url, compound_cid_selector, search_id, property, output_property, output_format, output_file_name)