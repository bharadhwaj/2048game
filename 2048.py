from random import randrange, random

def getelement():
    return 2 if random() < 0.67 else 4

def generate_element(tiles):
	gen_x = randrange(0, 4)
	gen_y = randrange(0, 4)

	gen_n = getelement()

	if tiles[gen_x][gen_y] != 0:
		found = False
		for row in range(gen_x, 4):
			for column in range(gen_y, 4):
				if tiles[row][column] == 0:
					found = True
					tiles[row][column] = gen_n
					return tiles
		if found == False:
			for row in range(0, gen_x):
				for column in range(0, gen_y):
					if tiles[row][column] == 0:
						found = True
						tiles[row][column] = gen_n
						return tiles
		if found == False:
			return ['Error']
	else:
		tiles[gen_x][gen_y] = gen_n
		return tiles


	

def print_array(tiles):
	for row in tiles:
	    for val in row:
	        print '{:5}'.format(val),
	    print

def moveup(tiles):
	for row in range(1,4):
		for column in range(4):
			if tiles[row-1][column] == 0:
				i = row-1
				while tiles[i][column] == 0 and i >= 0 and i < 3:
					tiles[i][column] = tiles[i+1][column]
					tiles[i+1][column] = 0
					i -= 1
				if i == 0:
					if tiles[i][column] == tiles[i+1][column]:
						tiles[i][column] = 2*tiles[i+1][column]
						tiles[i+1][column] = 0
			else:	
				if tiles[row-1][column] == tiles[row][column]:
					tiles[row-1][column] = 2*tiles[row][column]
					tiles[row][column] = 0
					i = row
					while tiles[i][column] == 0 and i >= 0 and i < 3:
						tiles[i][column] = tiles[i+1][column]
						tiles[i+1][column] = 0
						i -= 1
					
	return tiles

def movedown(tiles):
	for row in range(3,0,-1):
		for column in range(4):
			if tiles[row][column] == 0:
				loop = True
				if tiles[row-1][column] != 0:
					i = row-1
				elif tiles[max(row-2, 0)][column] != 0:
					i = row-2
				elif tiles[max(row-3, 0)][column] != 0:
					i = row-3
				else:
					loop = False
				if loop:
					tiles[row][column],tiles[i][column] = tiles[i][column], 0
					if row < 3:
						if tiles[row+1][column] == tiles[row][column]:
							tiles[row+1][column] = 2*tiles[row][column]
							tiles[row][column] = 0
			else:	
				if tiles[row][column] == tiles[row-1][column]:
					tiles[row][column] = 2*tiles[row-1][column]
					tiles[row-1][column] = 0
	return tiles
	

def main():
    tiles = [[0 for i in range(4)] for j in range(4)]
    tiles = generate_element(tiles)
    print_array(tiles)
    keystroke = ''
    while keystroke != 'z':
		keystroke = raw_input("Movement? ")
		if keystroke != 'w' and keystroke != 'a' and keystroke != 's' and keystroke != 'd' and keystroke != 'z' and keystroke != 'W' and read != 'A' and read != 'S' and read != 'D' and read != 'Z':
			print 'Error: Wrong Input! Try again with valid Input!'
			continue
		if keystroke == 'w':
			tiles = moveup(tiles)
			tiles = generate_element(tiles)

		elif keystroke == 's':
			tiles = movedown(tiles)
			tiles = generate_element(tiles)

		print_array(tiles)


if __name__=='__main__':
    main()
