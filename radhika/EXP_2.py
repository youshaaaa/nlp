nl = input ("Enter: ")
new=''
m=[]
for b in nl:
    if b==' ':
        m.append(new)
        new=''
    else:
        new+=b
print(m)

sent = input("Enter: ")
new_2=''
l=[]
for a in range(len(sent)):
    k=sent[a]
    for j in k:
        if j=='.' or j=='!' or j=='?':
            l.append(new_2)
            new_2=' '
        else:
            new_2+=j
print(l)
        
