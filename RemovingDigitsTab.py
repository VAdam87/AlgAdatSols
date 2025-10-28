#https://cses.fi/problemset/task/1637/
# Dinamikus Programozas

def gen_list(target):
    st = set([int(x) for x in str(target).strip() if x != '0'])
    lst = list(st)
    lst.sort(reverse=True)
    return lst


def rem_digits_tab(target):
    tab = [target] * (target+1)
    tab[target] = 0

    for i in range(target, -1, -1):
        if tab[i] == target:
            continue
        num_list = gen_list(i)
        for num in num_list:
            tab[i-num] = min(tab[i]+1, tab[i-num])
    return tab[0]

_t = int(input())
print(rem_digits_tab(_t))

