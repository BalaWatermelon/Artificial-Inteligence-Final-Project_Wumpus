class Map(object):
    def __init__(self, size=4):
        self.SIZE = size
        self.map = [['', '', 'W', ''],
                    ['', '', 'P', ''],
                    ['', 'P', '', ''],
                    ['', '', '', 'P']]
        self.neighbor_B_S()
        self.playerLocation = (0, 0)
        self.moveTo(self.playerLocation)

    def __str__(self):
        r = ''
        for row in self.map[::-1]:
            r += str(row)+'\n'
        return r

    def moveTo(self, location):
        ''' Move player to location and return that block info
        # Parameter

        - location = (x, y) : tuple

        # Return

        - 'SB':   Smell and Breeze
        - ''  :   Nothing
        - 'G' :   Glare
        '''
        col, row = self.playerLocation
        self.map[row][col] = self.map[row][col].strip('*')
        col, row = self.mapIn(location)
        self.playerLocation = (col, row)
        self.map[row][col] += '*'
        print(f'Move player to {self.mapOut(self.playerLocation)}')
        return self.map[row][col][:-1]

    def mapIn(self, location):
        col, row = location
        if row >= self.SIZE or col >= self.SIZE or row < 0 or col < 0:
            raise ValueError(
                f'Access map location out of border at {col, row}')
        else:
            return (col, row)

    def mapOut(self, location):
        x, y = location
        return (x+1, y+1)

    def status(self):
        col, row = self.playerLocation
        return self.map[col][row]

    def whereAmI(self):
        return self.playerLocation

    def adjacent(self):
        x, y = self.playerLocation
        adj = [(x-1, y), (x+1, y), (x, y+1), (x, y-1)]
        out = [cell for cell in adj if cell[0] < self.SIZE and cell[1] <
               self.SIZE and cell[0] >= 0 and cell[1] >= 0]
        return out

    def neighbor_B_S(self):
        world = self.map
        size = len(world)
        gold = None
        for i in range(size):
            for j in range(size):
                nei = None
                if 'W' in world[i][j]:
                    nei = 'S'
                if 'P' in world[i][j]:
                    nei = 'B'
                if nei != None:
                    top = i-1
                    down = i+1
                    left = j-1
                    right = j+1
                    if top >= 0:
                        world[top][j] += nei
                        if nei == 'S' and gold == None and 'P' not in world[top][j]:
                            world[top][j] += 'G'
                            gold = 1
                    if down <= size-1:
                        world[down][j] += nei
                        if nei == 'S' and gold == None and 'P' not in world[down][j]:
                            world[down][j] += 'G'
                            gold = 1
                    if left >= 0:
                        world[i][left] += nei
                        if nei == 'S' and gold == None and 'P' not in world[i][left]:
                            world[i][left] += 'G'
                            gold = 1
                    if right <= size-1:
                        world[i][right] += nei
                        if nei == 'S' and gold == None and 'P' not in world[i][right]:
                            world[i][right] += 'G'
                            gold = 1

