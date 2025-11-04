# https://www.hackerrank.com/challenges/pairs
# binaris kereses


nums = []
def bin_search(bal,jobb, target):
    global nums
    kozep = int((bal + jobb) / 2)

    if nums[kozep] == target:
        return 1

    if bal-jobb == 1:
        return 0

    if nums[kozep] > target:
        return bin_search(bal, kozep-1, target)
    else:
        return bin_search(kozep+1, jobb, target)

def pairs(k, arr):
    global nums
    nums = sorted(arr)
    mennyiseg = 0
    for i in arr:
        mennyiseg += bin_search(0, len(arr)-1, i+k)
        mennyiseg += bin_search(0, len(arr)-1, i-k)
    return int(mennyiseg/2)

