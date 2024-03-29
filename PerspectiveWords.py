word1 = "LETS"
word2 = "GO"
word3 = "PRG!"

file_name = "system.xyz"

# This filter creates a bunch of blocks that appear as three different
# words from three different directions. Feel free to use and modify this
# script however you want, but please attribute SethBling.
# http://youtube.com/SethBling

# adapted to output a xyz molecule file by Kovas Palunas

import random
from numpy import sqrt

LetterPixels = {
    'A': [[0, 1, 0],
          [1, 0, 1],
          [1, 1, 1],
          [1, 0, 1],
          [1, 0, 1]],
    'B': [[1, 1, 0],
          [1, 0, 1],
          [1, 1, 0],
          [1, 0, 1],
          [1, 1, 0]],
    'C': [[0, 1, 1],
          [1, 0, 0],
          [1, 0, 0],
          [1, 0, 0],
          [0, 1, 1]],
    'D': [[1, 1, 0],
          [1, 0, 1],
          [1, 0, 1],
          [1, 0, 1],
          [1, 1, 0]],
    'E': [[1, 1, 1],
          [1, 0, 0],
          [1, 1, 0],
          [1, 0, 0],
          [1, 1, 1]],
    'F': [[1, 1, 1],
          [1, 0, 0],
          [1, 1, 0],
          [1, 0, 0],
          [1, 0, 0]],
    'G': [[0, 1, 1, 1],
          [1, 0, 0, 0],
          [1, 0, 1, 1],
          [1, 0, 0, 1],
          [0, 1, 1, 0]],
    'H': [[1, 0, 1],
          [1, 0, 1],
          [1, 1, 1],
          [1, 0, 1],
          [1, 0, 1]],
    'I': [[1, 1, 1],
          [0, 1, 0],
          [0, 1, 0],
          [0, 1, 0],
          [1, 1, 1]],
    'J': [[0, 1, 1, 1],
          [0, 0, 1, 0],
          [0, 0, 1, 0],
          [1, 0, 1, 0],
          [0, 1, 0, 0]],
    'K': [[1, 0, 1],
          [1, 0, 1],
          [1, 1, 0],
          [1, 0, 1],
          [1, 0, 1]],
    'L': [[1, 0, 0],
          [1, 0, 0],
          [1, 0, 0],
          [1, 0, 0],
          [1, 1, 1]],
    'M': [[1, 0, 0, 0, 1],
          [1, 1, 0, 1, 1],
          [1, 0, 1, 0, 1],
          [1, 0, 0, 0, 1],
          [1, 0, 0, 0, 1]],
    'N': [[1, 0, 0, 0, 1],
          [1, 1, 0, 0, 1],
          [1, 0, 1, 0, 1],
          [1, 0, 0, 1, 1],
          [1, 0, 0, 0, 1]],
    'O': [[0, 1, 0],
          [1, 0, 1],
          [1, 0, 1],
          [1, 0, 1],
          [0, 1, 0]],
    'P': [[1, 1, 0],
          [1, 0, 1],
          [1, 1, 0],
          [1, 0, 0],
          [1, 0, 0]],
    'Q': [[0, 1, 1, 0, 0],
          [1, 0, 0, 1, 0],
          [1, 0, 0, 1, 0],
          [1, 0, 1, 1, 0],
          [0, 1, 1, 0, 1]],
    'R': [[1, 1, 0],
          [1, 0, 1],
          [1, 1, 0],
          [1, 0, 1],
          [1, 0, 1]],
    'S': [[0, 1, 1, 1],
          [1, 0, 0, 0],
          [0, 1, 1, 0],
          [0, 0, 0, 1],
          [1, 1, 1, 0]],
    'T': [[1, 1, 1],
          [0, 1, 0],
          [0, 1, 0],
          [0, 1, 0],
          [0, 1, 0]],
    'U': [[1, 0, 0, 1],
          [1, 0, 0, 1],
          [1, 0, 0, 1],
          [1, 0, 0, 1],
          [0, 1, 1, 0]],
    'V': [[1, 0, 1],
          [1, 0, 1],
          [1, 0, 1],
          [1, 0, 1],
          [0, 1, 0]],
    'W': [[1, 0, 1, 0, 1],
          [1, 0, 1, 0, 1],
          [1, 0, 1, 0, 1],
          [1, 0, 1, 0, 1],
          [0, 1, 0, 1, 0]],
    'X': [[1, 0, 1],
          [1, 0, 1],
          [0, 1, 0],
          [1, 0, 1],
          [1, 0, 1]],
    'Y': [[1, 0, 1],
          [1, 0, 1],
          [0, 1, 0],
          [0, 1, 0],
          [0, 1, 0]],
    'Z': [[1, 1, 1],
          [0, 0, 1],
          [0, 1, 0],
          [1, 0, 0],
          [1, 1, 1]],
    '!': [[0, 1, 0],
          [0, 1, 0],
          [0, 1, 0],
          [0, 0, 0],
          [0, 1, 0]],
    }

class Box:
	def __init__(self, minx=0, maxx=50, miny=0, maxy=30,
				 minz=0, maxz=50):
		self.minx = minx
		self.maxx = maxx
		self.miny = miny
		self.maxy = maxy
		self.minz = minz
		self.maxz = maxz

def strToArray(s):
    ret = [[],[],[],[],[]]

    for ch in s:
        if not ch in LetterPixels:
            continue

        for row in range(5):
            ret[row].extend(LetterPixels[ch][row])
            ret[row].append(0)

    return ret

def getPixel(box, dim, array, (x1, y1, z1), (x2, y2, z2)):
    arraywidth = len(array[0])

    cx = (box.maxx + box.minx) / 2.0
    cy = (box.maxy + box.miny) / 2.0
    cz = (box.maxz + box.minz) / 2.0

    if dim == 0:
        frac = float(box.minx - x1) / (x2 - x1)
    elif dim == 1:
        slope = (z2 - z1) / (x2 - x1 + 0.0000001)
        zint = z1 + slope * (box.minx - x1)
        xeq = (box.minz-zint)/(1.0000001+slope) + box.minx
        zeq = z1 + slope * (xeq - box.minx)
        frac = float(xeq - x1) / (x2 - x1)
    elif dim == 2:
        frac = float(box.minz - z1) / (z2 - z1)

    (ix, iy, iz) = (x1 * (1-frac) + x2 * frac - cx,
                    y1 * (1-frac) + y2 * frac - cy,
                    z1 * (1-frac) + z2 * frac - cz)

    if dim == 0:
        (i, j) = (iy, iz)
    elif dim == 1:
        (i, j) = (iy, sqrt(2)*(box.minx-xeq))
    elif dim == 2:
        (i, j) = (iy, -ix)

    i = int(i + 2.5)
    j = int(j + arraywidth / 2)

    if i < 0 or i >= 5:
        return False
    if j < 0 or j >= arraywidth:
        return False


    if array[4-i][j] == 0:
        return False

    return True

#def createMarker(level, (x, y, z)):
def createMarker((x, y, z), array):
    #chunk = level.getChunk(int(x) / 16, int(z) / 16)
    #chunk.dirty = True

    setAtomAt(int(x), int(y)-2, int(z), 'S', array, 5)
    
def setAtomAt(x, y, z, type, array, mult):
	array.append([type, str(mult*x), str(mult*y), str(mult*z)])

def writeFile(filename, array):
	with open(filename, 'w') as file:
		file.write(str(len(array)) + '\n')
		#file.write(word1 + ' ' + word2 + ' ' + word3 + '\n')
		file.write('No secrets here... try a visualizer' + '\n')
		for atom in array:
			file.write(atom[0] + '\t' + atom[1] + '\t' + atom[2] + '\t' + atom[3] + '\n')
	print('Wrote atoms to ' + filename)
	
#def perform(level, box, options):
box = Box(0, 200, 0, 120, 0, 200)
atom_array = []

array1 = strToArray(word1)
array2 = strToArray(word3)
array3 = strToArray(word2)

cx = float(box.maxx + box.minx) / 2
cy = float(box.maxy + box.miny) / 2
cz = float(box.maxz + box.minz) / 2

width = box.maxx - box.minx
height = box.maxy - box.miny
depth = box.maxz - box.minz

pos1 = (box.minx - 30, cy, cz)
pos2 = (cx, cy, box.minz - 30)
pos3 = (box.minx - 30, cy, box.minz - 30)

createMarker(pos1, atom_array)
createMarker(pos2, atom_array)
createMarker(pos3, atom_array)

for x in xrange(box.minx, box.maxx):
    for y in xrange(box.miny, box.maxy):
        for z in xrange(box.minz, box.maxz):
            if getPixel(box, 0, array1, pos1, (x, y, z)) and getPixel(box, 2, array2, pos2, (x, y, z)) and getPixel(box, 1, array3, pos3, (x, y, z)):
                setAtomAt(x, y, z, 'C', atom_array, 5)

#level.markDirtyBox(box)

writeFile(file_name, atom_array)
