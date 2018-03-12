
import os
import sys
import urllib
from math import *
from Bio.PDB import PDBParser
from xml.etree.ElementTree import parse


def GO_Data(pdbid, req_chain):
    # Gene Ontology Information.
    GO_url = 'http://www.rcsb.org/pdb/rest/goTerms?structureId='
    GO_u = urllib.urlopen(GO_url + pdbid.upper() + '.' + req_chain.upper())
    GO_data = GO_u.read()
    f = open(pdbid + '_GO.xml', 'wb')
    f.write(GO_data)
    f.close()
    GO_doc = parse(pdbid + '_GO.xml')
    root = GO_doc.getroot()
    GO_List = []
    for child in root:
        if child.attrib['structureId'] == pdbid.upper() and child.attrib['chainId'] == req_chain:
            GO_List.append(str(child.attrib['id']))
    return GO_List


def Pfam_Data(pdbid, req_chain):
    # Pfam Information.
    Pfam_url = 'http://www.rcsb.org/pdb/rest/hmmer?structureId='
    Pfam_u = urllib.urlopen(Pfam_url + pdbid)
    Pfam_data = Pfam_u.read()
    f1 = open(pdbid + '_Pfam.xml', 'wb')
    f1.write(Pfam_data)
    f1.close()
    Pfam_doc = parse(pdbid + '_Pfam.xml')
    root1 = Pfam_doc.getroot()
    for child in root1:
        if child.attrib['structureId'] == pdbid.upper() and child.attrib['chainId'] == req_chain:
            name1 = str(child.attrib['pfamName'])
            acces = str(child.attrib['pfamAcc'])
            start = str(child.attrib['pdbResNumStart'])
            end = str(child.attrib['pdbResNumEnd'])
            desc = str(child.attrib['pfamDesc'])
            evalue = str(child.attrib['eValue'])
    return name1, acces, start, end, desc, evalue


def Header_Data(pdbid, req_chain):
    # Data from the Header of the pdb files.
    directory = os.getcwd() + '/'
    pdbfile = directory + pdbid + ".pdb"
    Parser = PDBParser(QUIET=True)
    Structure = Parser.get_structure(pdbid, pdbfile)
    Name = Parser.header['name']
    Head = Parser.header['head']
    Reso = Parser.header['resolution']
    Keyw = Parser.header['keywords']
    Expt = Parser.header['structure_method']
    # Comp = BioParser.header['compound']
    return Name, Head, Reso, Keyw, Expt

if __name__ == "__main__":
    """ Select specific chains from a pdb file and obtain information
        regarding PDB Header, Gene Ontology and Pfam. """
    if len(sys.argv) != 3:
        print "Usage example: python Header_Pfam_Go.py 1ayo A"
        sys.exit()
    else:
        pdbid = sys.argv[1]
        chain = sys.argv[2]
        GO = GO_Data(pdbid, chain)
        GO = ', '.join(GO)
        a, b, c, d, e, f = Pfam_Data(pdbid, chain)
        Name, Head, Reso, Keyw, Expt = Header_Data(pdbid, chain)
        print "=" * 100
        print "PDBID:", pdbid
        print "Chain Id:", chain
        print "Name:", Name
        print "Header:", Head
        print "Keywords:", Keyw
        print "Experiment:", Expt
        print "Resolution:", Reso
        print "Gene Ontology:", GO
        print "Pfam Name:", a
        print "Pfam Accession:", b
        print "Pfam Start:", c
        print "Pfam End:", d
        print "Pfam Description:", e
        print "Pfam eValue:", f
        print "=" * 100
