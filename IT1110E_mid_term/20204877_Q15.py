def elec(path):
    d = {}
    file = open(path,'r')
    for line in file:
        if 'PARTIES' in line:
            continue
        if 'VOTES' in line:
            continue
        x = line.replace('\n','')
        if x not in d:
            d[x] = 0
        else:
            d[x] += 1
    a = sorted(d.items(), key = lambda x:x[0])
    a.sort(key = lambda x: x[1], reverse = True)
    for i in a:
        print(i[0])
