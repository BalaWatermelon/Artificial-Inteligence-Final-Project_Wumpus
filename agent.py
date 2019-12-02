#%%
def ifAdjSafe(safe,statusM):
    M=statusM
    if M=='*':
        adj=m.adjacent()
        for i in adj:
            safe.append(i)

    
    
#%%
import map
m=map.Map()
safe=[]

ifAdjSafe(safe,m.status())

while safe:
    nextstep=safe.pop()
    m.moveTo(nextstep)
    ifAdjSafe(safe,m.status())
    print(m.whereAmI())
    




# %%
