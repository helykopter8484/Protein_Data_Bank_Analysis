# Protein Data Bank Analysis

A few scripts for analyzing three dimensional protein structure data from the protein data bank.

### Prerequisites

The scripts are written in Python and use a few other libraries.

* Python
* Biopython

Biopython can be installed by using the Python Package Index - PIP.

```
pip install biopython
```

The functionality of the scripts is mentioned below:

### Center_Mass_Zero.py
Reset Center of Mass of PDB file to zero. Program takes the pdb filename as the argument.
The file should be present in the working directory.
The program calculates and prints the original center of mass, the new center of mass adjusted to zero and the range of the new X, Y and Z coordinates. Output filename ends with suffix "new.pdb." Useful for Molecular Modeling Purposes.
```
python Reset_Center_Mass.py 1crn.pdb
```

### Header_Pfam_Go.py
This program takes the pdb id and the chain id as inputs and prints out the Header, Pfam (Name, Accession, Start, End, Description, e-Value) and GO Information.
```
python Header_Pfam_Go.py 1ayo A
```

### PDB_Chain_Selector.py
This program takes a pdb file and chain id as an input and writes out a new file. Biopython module required for this program. The Atom and Hetatm information of a specific chain can be obtained.
```python Chain_Select.py 1ayo A
```
