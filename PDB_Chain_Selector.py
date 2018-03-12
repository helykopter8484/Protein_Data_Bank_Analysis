
import os
import sys
from Bio.PDB import PDBParser, PDBIO
from Bio.PDB.PDBIO import Select


class Chain_Select(Select):
    """This program takes a pdb file and chain id as an input
    and writes out a new file. Biopython module required
    or this program. Only Atom and Hetatm information of
    a specific chain can be obtained. Header information
    not included.
    The program uses the Select class from PDBIO in Biopython."""

    def __init__(self, chain_id):
        self.chain_id = chain_id

    def accept_chain(self, chain):
        return True if chain.id == self.chain_id else False

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print "Usage example: python Chain_Select.py 1ayo A"
        sys.exit()
    else:
        parser = PDBParser(PERMISSIVE=True, QUIET=True)
        structure_id = sys.argv[1]
        chain_id = sys.argv[2]
        directory = os.getcwd() + '/'
        pdbfile = structure_id + ".pdb"
        # Create a structure object from a local pdb file.
        structure = parser.get_structure(structure_id, directory + pdbfile)

    io = PDBIO()
    io.set_structure(structure)
    io.save(
        "{0}_{1}.pdb".format(structure_id, chain_id),
        Chain_Select(chain_id)
        )
    # print "This is the {0} class and {1}".format(parser, 'String')
