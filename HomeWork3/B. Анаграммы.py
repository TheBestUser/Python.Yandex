d = {}
for i in range(int(input())):
    s = input().lower()
    if len(s) < 2:
        continue
    r = str(sorted(s))
    if r not in d.keys():
        d[r] = list()
    if s not in d[r]:
        d[r].append(s)
ll = []
for l in d.keys():
    if len(d[l]) > 1:
        d[l].sort()
        ll.append(d[l])
ll.sort()
for l in ll:
    for w in l:
        print(w, end=' ')
    print()
