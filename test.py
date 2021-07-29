import requests
with open('cid.txt') as f:
    cid_list = [i.strip() for i in f.readlines()[399:699]]
property_list = [
    "IUPACName",
    "IsomericSMILES",
    "MolecularFormula",
    "MolecularWeight",
    "HBondDonorCount",
    "HBondAcceptorCount"
]
api = 'https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/'
property_str = ','.join(property_list)
return_type = 'json'
cid_str = ','.join(cid_list)
url = f'{api}{cid_str}/property/{property_str}/{return_type}'
# print(url)
res = requests.get(url)
print(res.status_code)
# prp = res['PropertyTable']['Properties']
# print(len(prp))
