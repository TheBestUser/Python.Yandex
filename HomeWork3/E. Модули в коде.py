import re

modules_list = set()
fr = False
with open('input.txt') as f:
    for line in f:
        ws = re.sub('[;]', '', line.strip().lower()).split(" ")
        for i in range(len(ws)):
            if ws[i] == "from":
                fr = True
                modules_list.add(ws[i + 1])
            elif ws[i] == "import":
                if fr:
                    fr = False
                    continue
                j = i + 1
                while ws[j][-1] == ',':
                    modules_list.add(ws[j][:-1])
                    j += 1
                modules_list.add(ws[j])
print(", ".join("{}".format(k) for k in sorted(modules_list),))
