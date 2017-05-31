def lang_count(ch):
    for k in d.keys():
        if ch in d[k]:
            if k in lc.keys():
                lc[k] += 1
            else:
                lc[k] = 1


def max_lang():
    mv = 0
    ml = str()
    for k, v in sorted(lc.items()):
        if mv < v:
            ml, mv = k, v
    if ml not in lang_list:
        lang_list.append(ml)


lc = {}
d = {}
lang_list = []

while True:
    l = str(input())
    if l == "":
        break
    ss = l.split(" ")
    d[ss[0]] = tuple(ss[1])
while True:
    try:
        l = str(input()).lower()
        if not l:
            break
        for w in l.split(" "):
            for c in w:
                lang_count(c)
            max_lang()
            lc.clear()
        for l in sorted(lang_list):
            print(l, end=' ')
        print()
        lang_list.clear()
    except EOFError:
        break
