
import os
import sys


def Writer(directory, filename, data):
    with open(directory+filename, 'wb') as f:
        for item in data:
            f.write(item)
    f.close()
    return


def getStructureFromFile(fileName):
    directory = os.getcwd() + '/'
    if os.path.isfile(directory + '/' + fileName) is False:
        print "File does not exist! Provide a valid filename."
        print "Usage example: python Reset_Center_Mass.py 1tit.pdb"
        print "The pdb file should be present in the working directory."
        sys.exit()
    else:
        fileHandle = open(fileName)
        Structure = []
        massDict = {'H': 1, 'C': 12, 'N': 14, 'O': 16, 'P': 30, 'S': 32}
        for line in fileHandle.readlines():
            key = line[0:6].strip()
            if key == 'ATOM':
                x = float(line[30:38])
                y = float(line[38:46])
                z = float(line[46:54])
                atomType = line[77:78].strip()
                for item in atomType:
                    a = item
                    b = massDict[a]
                Structure.append([x, y, z, atomType, b])
                TotalAtoms = len(Structure)
        return Structure, TotalAtoms


def CenterMass(Structure, TotalAtoms):
    X = 0.0
    Y = 0.0
    Z = 0.0
    M = 0.0
    m = 0.0
    for i in Structure:
        m = float(i[4])
        X = X + float(i[0]) * m
        Y = Y + float(i[1]) * m
        Z = Z + float(i[2]) * m
        M = M + m
    X /= M
    Y /= M
    Z /= M
    return X, Y, Z


def NewCenter(X, Y, Z, Structure):
    New = []
    Xmax = []
    Ymax = []
    Zmax = []
    for i in Structure:
        x_new = round((float(i[0]) - X), 3)
        y_new = round((float(i[1]) - Y), 3)
        z_new = round((float(i[2]) - Z), 3)
        New.append([x_new, y_new, z_new])
        Xmax.append(x_new)
        Ymax.append(y_new)
        Zmax.append(z_new)
    Xrange = [max(Xmax), min(Xmax)]
    Yrange = [max(Ymax), min(Ymax)]
    Zrange = [max(Zmax), min(Zmax)]
    return New, Xrange, Yrange, Zrange


def NewFileWriter(oldfile, newfile, NewCenter):
    fileHandle = open(oldfile)
    i = 0
    DATA = ""
    for line in fileHandle.readlines():
        temp = line
        key = line[0:6].strip()
        if key == 'ATOM':
            foo = str(NewCenter[i][0])
            bar = str(NewCenter[i][1])
            fuz = str(NewCenter[i][2])
            temp = line[0:31] + (7-len(foo))*' ' + foo + (8-len(bar))*' ' + bar + (8-len(fuz))*' ' + fuz + " " + line[55:]
            i = i+1
        DATA = DATA+temp
    Writer("./", newfile, DATA)


if len(sys.argv) != 2:
    print "Usage example: python Reset_Center_Mass.py 1crn.pdb"
    print "Please provide pdb filename as the argument."
    sys.exit()
else:
    print """   The program takes a pdb file and and resets the center of mass to zero.
    Can be used for Molecular Modeling purposes. The file should be present
    the working directory. The resulting output file ends with a suffix
    "_new.pdb" """
    Structure, TotalAtoms = getStructureFromFile(sys.argv[1])
    X, Y, Z = CenterMass(Structure, TotalAtoms)
    print "================================================================"
    print "INPUT FILE: -", sys.argv[1]
    print 'Original Center of Mass: -'
    print 'X-Coordinate: ', X
    print 'Y-Coordinate: ', Y
    print 'Z-Coordinate: ', Z
    NewCoord, Xrange, Yrange, Zrange = NewCenter(X, Y, Z, Structure)
    NewFileWriter(sys.argv[1], sys.argv[1][0:-4]+'_new.pdb', NewCoord)
    Structure, TotalAtoms = getStructureFromFile(sys.argv[1][0:-4]+'_new.pdb')
    X, Y, Z = CenterMass(Structure, TotalAtoms)
    print "================================================================"
    print "OUTPUT FILE: -", sys.argv[1][0:-4]+'_new.pdb'
    print 'New Center of Mass: -'
    print 'X-Coordinate: ', X
    print 'Y-Coordinate: ', Y
    print 'Z-Coordinate: ', Z
    print "================================================================"
    print "Maximum and Minimum values of new coordinates are as follows:"
    print "X-coordinate:", Xrange
    print "Y-coordinate:", Yrange
    print "Z-coordinate:", Zrange
    print "================================================================"
