from random import randrange

def generate_element(tiles):
	gen_x = randrange(0, 4)
	gen_y = randrange(0, 4)

	gen_n = randrange(0, 2)

	if gen_n == 0:
		elt = 2
	else:
		elt = 4

	if tiles[gen_x][gen_y] != 0:
		found = False
		for row in range(gen_x, 4):
			for column in range(gen_y, 4):
				if tiles[row][column] == 0:
					found = True
					tiles[row][column] = elt
					return tiles
		if found == False:
			for row in range(0, gen_x):
				for column in range(0, gen_y):
					if tiles[row][column] == 0:
						found = True
						tiles[row][column] = elt
						return tiles
		if found == False:
			return ['Error']
	else:
		tiles[gen_x][gen_y] = elt
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

		print_array(tiles)


if __name__=='__main__':
    main()