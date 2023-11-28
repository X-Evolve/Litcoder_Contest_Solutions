def Transform(start, end):
    n = len(start)
    i = j = 0

    while i < n and j < n:

        while i < n and start[i] == 'X':
            i += 1
        while j < n and end[j] == 'X':
            j += 1
        if (i < n and j == n) or (i == n and j < n) or (i < n and j < n and start[i] != end[j]):
            return False

        if i < n and j < n:
            if start[i] == 'L' and i < j:
                return False
            if start[i] == 'R' and i > j:
                return False

        i += 1
        j += 1

    return True

start = input()
end = input()
print(Transform(start, end)) 

