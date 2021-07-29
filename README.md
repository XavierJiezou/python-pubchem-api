# Introduction
Crawl data of compounds from [PubChem](https://pubchem.ncbi.nlm.nih.gov/).
# Install
```bash
pip install pubchempy, alive_progress, retrying
```
# Usage
1. Git clone the repo.
```bash
git clone https://github.com/XavierJiezou/python-pubchem-api.git
```
2. Cd to the root path.
```python
cd python-pubchem-api
```
3. Write cid list to `cid.txt`.
4. Run `python main.py`.
5. Results can be seen in `data.csv`.
6. You can also modify the variable `self.maps` in [main.py](main.py) according to the `Compound Property Map` below.
```python
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
```
# Map
Compound Property Map from [pubchempy](https://github.com/mcs07/PubChemPy).
```python
PROPERTY_MAP = {
    'molecular_formula': 'MolecularFormula',
    'molecular_weight': 'MolecularWeight',
    'canonical_smiles': 'CanonicalSMILES',
    'isomeric_smiles': 'IsomericSMILES',
    'inchi': 'InChI',
    'inchikey': 'InChIKey',
    'iupac_name': 'IUPACName',
    'xlogp': 'XLogP',
    'exact_mass': 'ExactMass',
    'monoisotopic_mass': 'MonoisotopicMass',
    'tpsa': 'TPSA',
    'complexity': 'Complexity',
    'charge': 'Charge',
    'h_bond_donor_count': 'HBondDonorCount',
    'h_bond_acceptor_count': 'HBondAcceptorCount',
    'rotatable_bond_count': 'RotatableBondCount',
    'heavy_atom_count': 'HeavyAtomCount',
    'isotope_atom_count': 'IsotopeAtomCount',
    'atom_stereo_count': 'AtomStereoCount',
    'defined_atom_stereo_count': 'DefinedAtomStereoCount',
    'undefined_atom_stereo_count': 'UndefinedAtomStereoCount',
    'bond_stereo_count': 'BondStereoCount',
    'defined_bond_stereo_count': 'DefinedBondStereoCount',
    'undefined_bond_stereo_count': 'UndefinedBondStereoCount',
    'covalent_unit_count': 'CovalentUnitCount',
    'volume_3d': 'Volume3D',
    'conformer_rmsd_3d': 'ConformerModelRMSD3D',
    'conformer_model_rmsd_3d': 'ConformerModelRMSD3D',
    'x_steric_quadrupole_3d': 'XStericQuadrupole3D',
    'y_steric_quadrupole_3d': 'YStericQuadrupole3D',
    'z_steric_quadrupole_3d': 'ZStericQuadrupole3D',
    'feature_count_3d': 'FeatureCount3D',
    'feature_acceptor_count_3d': 'FeatureAcceptorCount3D',
    'feature_donor_count_3d': 'FeatureDonorCount3D',
    'feature_anion_count_3d': 'FeatureAnionCount3D',
    'feature_cation_count_3d': 'FeatureCationCount3D',
    'feature_ring_count_3d': 'FeatureRingCount3D',
    'feature_hydrophobe_count_3d': 'FeatureHydrophobeCount3D',
    'effective_rotor_count_3d': 'EffectiveRotorCount3D',
    'conformer_count_3d': 'ConformerCount3D',
}
```
Some hidden properties can also be available.
```python
PROPERTY_MAP = {
    'cid': 'CID',
    'synonyms': 'Synonyms'
}
```
# Tips
For faster speed, you can try multi-threading. However, if the number of workers in `ThreadPoolExecutor` is too large, an exception named `PUGREST.ServerBusy` may be raised. It is recommended that the maximum number of threads is less than 4.
# Reference
> [https://github.com/mcs07/PubChemPy](https://github.com/mcs07/PubChemPy)