import sys

BREEZE = 'B'
STENCH = 'S'
PIT = 'P'
WUMPUS = 'W'
POSSIBLEWUMPUS = 'W?'
POSSIBLEPIT = 'P?'
GOLD = 'G'
allCell = []
FoundWumpus = False
EXITGOLD = False


def ifAdjSafe(safe, back, statusM, brain):
    M = statusM
    if M == '*':
        adj = m.adjacent()
        for i in adj:
            if i not in back:
                safe.append(i)
                r, c = i
                brain[r][c] = 'o'


for i in range(4):
    for j in range(4):
        allCell.append((i, j))


def scanAllB_S(brain, m):
    global FoundWumpus
    for cell in allCell:
        row, col = cell
        if BREEZE in brain[row][col]:
            possibleB = []
            l = [cell for cell in m.adjacent((row, col)) if cell not in back]
            for c in l:
                row, col = c
                if POSSIBLEPIT in brain[row][col] or PIT in brain[row][col]:
                    possibleB.append(c)
            if len(possibleB) is 1:
                r, c = possibleB[0]
                brain[r][c] = 'P'
        if STENCH in brain[row][col]:
            possibleS = []
            l = [cell for cell in m.adjacent((row, col)) if cell not in back]
            for c in l:
                row, col = c
                if POSSIBLEWUMPUS in brain[row][col] or WUMPUS in brain[row][col]:
                    possibleS.append(c)
            if len(possibleS) is 1:
                r, c = possibleS[0]
                brain[r][c] = 'W'
                FoundWumpus = True
                #print('Found wumpus')


def scanAllP_W(brain, m):
    for cell in allCell:
        row, col = cell
        if POSSIBLEWUMPUS in brain[row][col]:
            possible = True
            for adj in m.adjacent(cell):
                r, c = adj
                if brain[r][c] is not '?' and brain[r][c] is not 'o' and STENCH not in brain[r][c]:
                    possible = False
            if not possible:
                brain[row][col] = brain[row][col].replace(POSSIBLEWUMPUS, '')
                if brain[row][col] == '?':
                    brain[row][col] = 'o'
                    safe.append(cell)
        if POSSIBLEPIT in brain[row][col]:
            possible = True
            for adj in m.adjacent(cell):
                r, c = adj
                if brain[r][c] is not '?' and brain[r][c] is not 'o' and BREEZE not in brain[r][c]:
                    possible = False
            if not possible:
                brain[row][col] = brain[row][col].replace(POSSIBLEPIT, '')
                if brain[row][col] == '?':
                    brain[row][col] = 'o'
                    safe.append(cell)


def printBrain(brain):
    r = ''
    for b in brain[::-1]:
        r += str(b)+'\n'
    print(r)


# %%
import map
m = map.Map()
print('MAP')
print(m)
safe = []
back = []

brain = []
for _ in range(4):
    brain.append(['?', '?', '?', '?'])
brain[0][0] = ''

ifAdjSafe(safe, back, m.status(), brain)


def markHazard(brain, r, c):
    global FoundWumpus
    if BREEZE in brain[r][c]:
        adjacentDanger = [cell for cell in m.adjacent(
            (r, c)) if cell not in back]
        for danger in adjacentDanger:
            r, c = danger
            if brain[r][c] is not 'o':
                brain[r][c] += 'P?'
    if STENCH in brain[r][c]:
        adjacentDanger = [cell for cell in m.adjacent(
            (r, c)) if cell not in back]
        for danger in adjacentDanger:
            r, c = danger
            if brain[r][c] is not 'o' and not FoundWumpus:
                brain[r][c] += 'W?'


while safe:
    input()
    nextstep = safe.pop()
    back.append(m.whereAmI())
    m.moveTo(nextstep)
    r, c = m.whereAmI()
    brain[r][c] = m.status()
    markHazard(brain, r, c)
    ifAdjSafe(safe, back, m.status(), brain)
    scanAllB_S(brain, m)
    scanAllP_W(brain, m)
    scanAllB_S(brain, m)
    scanAllP_W(brain, m)
    scanAllB_S(brain, m)
    scanAllP_W(brain, m)
    print('MAP:')
    print(m)
    print('BRAIN:')
    printBrain(brain)
    x, y = m.whereAmI()
    print(f'Agent at: {(x+1,y+1)}')
    if GOLD in m.status() and EXITGOLD:
        print('Gold found!! Win!!')
        sys.exit(0)

# %%
