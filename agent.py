# %%
def ifAdjSafe(safe, back, statusM):
    M = statusM
    if M == '*':
        adj = m.adjacent()
        for i in adj:
            if i not in back:
                safe.append(i)


# %%
import map
m = map.Map()
safe = []
back = []

ifAdjSafe(safe, back, m.status())

while safe:
    nextstep = safe.pop()
    back.append(m.whereAmI())
    m.moveTo(nextstep)
    ifAdjSafe(safe, back, m.status())
    print(m.whereAmI())


# %%
