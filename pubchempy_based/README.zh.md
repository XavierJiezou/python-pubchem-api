[English](README.md) | 简体中文
# 简介
从[PubChem](https://pubchem.ncbi.nlm.nih.gov/)爬取化合物的数据（基于Python的第三方库[PubChemPy](https://github.com/mcs07/PubChemPy)）。
# 安装
```bash
pip install pubchempy, alive_progress, retrying
```
# 用法
1. 克隆仓库。
```bash
git clone https://github.com/XavierJiezou/python-pubchem-api.git
```
2. `Cd`到根目录。
```bash
cd python-pubchem-api
```
3. 将`cid`列表复制到`cid.txt`。
4. 运行命令`python ./pubchempy_based/temp.py`。
5. 爬取结果保存在`data.csv`。
6. 你也可以根据下面的`Compound Property Map`修改[temp.py](temp.py)中的变量`self.maps` 

```python
class PubchemCrawl():
    def __init__(self, cid_path, out_path):
        self.cid_path = cid_path
        self.out_path = out_path
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
# 映射
Compound Property Map 来自 [PubChemPy](https://github.com/mcs07/PubChemPy)。
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
一些隐藏的属性也可以获得。
```python
PROPERTY_MAP = {
    'cid': 'CID',
    'synonyms': 'Synonyms'
}
```
# 提示
使用多线程编写可以获得更快的速度。但是`ThreadPoolExecutor`的线程数不能太大，不能会报错`PUGREST.ServerBusy` ，最大线程数最好不要超过4。
# 参考
> [https://github.com/mcs07/PubChemPy](https://github.com/mcs07/PubChemPy)