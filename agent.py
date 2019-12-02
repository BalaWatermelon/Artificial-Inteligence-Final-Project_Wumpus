# %%
def ifAdjSafe(safe, back, statusM):
    M = statusM
    if M == '*':
        adj = m.adjacent()
        for i in adj:
            if i not in back:
                safe.append(i)


BREEZE = 'B'
SMELL = 'S'


def scanAll(brain, explored, m):
    hazards = [BREEZE, SMELL]
    for cell in explored:
        row, col = cell
        if BREEZE in brain[row][col]:
            possibleB = []
            for c in m.adjacent((row, col)):
                row, col = c
                if brain[row][col] == 'B?':
                    possibleB.append(c)
            if len(possibleB) is 1:
                r, c = possibleB[0]
                brain[r][c] = 'P'
        if SMELL in brain[row][col]:
            possibleS = []
            for c in m.adjacent((row, col)):
                row, col = c
                if brain[row][col] == 'W?':
                    possibleS.append(c)
            if len(possibleS) is 1:
                r, c = possibleS[0]
                brain[r][c] = 'W'


def printBrain(brain):
    r = ''
    for b in brain:
        r += str(b)+'\n'
    print(r)


# %%
import map
m = map.Map()
safe = []
back = []

brain = []
for _ in range(4):
    brain.append(['?', '?', '?', '?'])
brain[0][0] = ''

ifAdjSafe(safe, back, m.status())


def markHazard(brain, r, c):
    if BREEZE in brain[r][c]:
        adjacentDanger = [cell for cell in m.adjacent(
            (r, c)) if cell not in back]
        for danger in adjacentDanger:
            r, c = danger
            brain[r][c] = 'P?'
    if SMELL in brain[r][c]:
        adjacentDanger = [cell for cell in m.adjacent(
            (r, c)) if cell not in back]
        for danger in adjacentDanger:
            r, c = danger
            brain[r][c] = 'W?'


while safe:
    nextstep = safe.pop()
    back.append(m.whereAmI())
    m.moveTo(nextstep)
    r, c = m.whereAmI()
    brain[r][c] = m.status()
    markHazard(brain, r, c)
    ifAdjSafe(safe, back, m.status())
    scanAll(brain, back, m)
    print('MAP:')
    print(m)
    print('BRAIN:')
    printBrain(brain)
    print(f'Agent at: {m.whereAmI()}')


# %%
