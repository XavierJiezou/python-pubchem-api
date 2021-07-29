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
2. Write cid list to `cid.txt`.
3. Run `main.py`.
4. Results can be seen in `data.csv`.
# Tips
If the number of workers for `ThreadPoolExecutor` is greater than `4`, may raise the exception: `PUGREST.ServerBusy`.
# Reference
https://github.com/mcs07/PubChemPy