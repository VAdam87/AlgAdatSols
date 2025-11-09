# https://www.hackerrank.com/challenges/pylons
# Moho

def pylons(k, arr):
    counter = 0
    last_pylon = -1

    while last_pylon < len(arr) - k:
        right = k-1 if last_pylon == -1 else last_pylon+k*2-1
        left = max(last_pylon-1, -1)
        
        if last_pylon >= len(arr) - k:
            return counter

        for i in range(min(right, len(arr)-1), left, -1):
            if arr[i] == 1 and i != last_pylon:
                last_pylon = i
                counter += 1
                break

            if i == last_pylon or i == left+1:
                return -1
                
    return counter