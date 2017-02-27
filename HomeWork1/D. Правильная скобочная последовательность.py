# D. Правильная скобочная последовательность
pair = {
    '}': '{',
    ')': '(',
    ']': '['
}


def check(s):
    s = list(s)
    stack = list()
    for i in s:
        if i == '{' or i == '(' or i == '[':
            stack.append(i)
        elif (i in pair) and (len(stack) != 0) and (pair[i] == stack[-1]):
            stack.pop()
        else:
            return 'no'
    if len(stack) != 0:
        return 'no'
    else:
        return 'yes'


n = int(input())
ans = [check(input()) for _ in range(0, n)]
for a in ans:
    print(a)
