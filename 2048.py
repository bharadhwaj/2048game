from random import randrange, random

def getelement():
    return 2 if random() < 0.67 else 4

def  checker(tiles):
	if 'Error' not in tiles:
	    for row in tiles:
	    	if 2048 in row:
	    		return True
	    return False


def generate_element(tiles):
	gen_x = randrange(0, 4)
	gen_y = randrange(0, 4)

	gen_n = getelement()

	if tiles[gen_x][gen_y] != 0:
		found = False
		for row in range(0, 4):
			for column in range(0, 4):
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
					tiles[row][column], tiles[i][column] = tiles[i][column], 0
					if row < 3:
						if tiles[row+1][column] == tiles[row][column]:
							tiles[row+1][column] = 2*tiles[row][column]
							tiles[row][column] = 0
			else:	
				if tiles[row][column] == tiles[row-1][column]:
					tiles[row][column] = 2*tiles[row-1][column]
					tiles[row-1][column] = 0
	return tiles
	
def moveleft(tiles):
	for row in range(4):
		for column in range(1, 4):
			if tiles[row][column-1] == 0:
				i = column-1
				while tiles[row][i] == 0 and i >= 0 and i < 3:
					tiles[row][i] = tiles[row][i+1]
					tiles[row][i+1] = 0
					i -= 1
				if i == 0:
					if tiles[row][i] == tiles[row][i+1]:
						tiles[row][i] = 2*tiles[row][i+1]
						tiles[row][i+1] = 0
			else:	
				if tiles[row][column-1] == tiles[row][column]:
					tiles[row][column-1] = 2*tiles[row][column]
					tiles[row][column] = 0
					i = column
					while tiles[row][i] == 0 and i >= 0 and i < 3:
						tiles[row][i] = tiles[row][i+1]
						tiles[row][i+1] = 0
						i -= 1
					
	return tiles

def moveright(tiles):
	for row in range(4):
		for column in range(3,0,-1):
			if tiles[row][column] == 0:
				loop = True
				if tiles[row][column-1] != 0:
					i = column-1
				elif tiles[row][max(column-2, 0)] != 0:
					i = column-2
				elif tiles[row][max(column-3, 0)] != 0:
					i = column-3
				else:
					loop = False
				if loop:
					tiles[row][column],tiles[row][i] = tiles[row][i], 0
					if column < 3:
						if tiles[row][column+1] == tiles[row][column]:
							tiles[row][column+1] = 2*tiles[row][column]
							tiles[row][column] = 0
			else:	
				if tiles[row][column] == tiles[row][column-1]:
					tiles[row][column] = 2*tiles[row][column-1]
					tiles[row][column-1] = 0
	return tiles

def main():
    found = False
    tiles = [[0 for i in range(4)] for j in range(4)]
    tiles = generate_element(tiles)
    print_array(tiles)
    keystroke = ''
    while keystroke != 'z' or keystroke != 'Z':
		keystroke = raw_input("Movement? ")
		if keystroke == 'w' or keystroke == 'W':
			tiles = moveup(tiles)
			tiles = generate_element(tiles)
		elif keystroke == 's' or keystroke == 'S':
			tiles = movedown(tiles)
			tiles = generate_element(tiles)
		elif keystroke == 'a' or keystroke == 'A':
			tiles = moveleft(tiles)
			tiles = generate_element(tiles)
		elif keystroke == 'd' or keystroke == 'D':
			tiles = moveright(tiles)
			tiles = generate_element(tiles)
		elif keystroke == 'z' or keystroke == 'Z':
			break
		else:
			print 'Error: Wrong Input! Try again with valid Input!'
			continue
		if 'Error' not in tiles:
			print_array(tiles)
		else:
			print 'Failed: Sorry! No move moves allowed!'
			return

		found = checker(tiles)
		if found:
			print 'Success. You won the game.'
			return


if __name__=='__main__':
    main()