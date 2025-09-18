# https://cses.fi/problemset/task/1070
_n = int(input())

def sol():
    szam_fele = int(_n/2)

    for i in range(szam_fele):
        print(i*2+2, sep=" ", end=" ")

    for i in range(szam_fele):
        print(i * 2 + 1, sep=" ", end=" ")

    if int(str(_n)[-1]) % 2 != 0:
        print(_n, sep=" ", end=" ")


if  1 < _n < 4:
    print("NO SOLUTION")
else:
   sol()









