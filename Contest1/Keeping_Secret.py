
def find(delay, forget, n, arr):
    mod = 10**9 + 7
    a = forget
    a -= delay
    if arr[n] != -1:
        return arr[n]
    j = 0
    sum_val = 0
    while a > 0 and n - delay - j > 0:
        a -= 1
        sum_val += find(delay, forget, n - delay - j, arr) % mod
        sum_val %= mod
        j += 1

    if n - forget > 0:
        arr[n] = sum_val % mod
    else:
        arr[n] = (sum_val + 1) % mod

    return arr[n]

def People_with_Secret(n, delay, forget):
    arr = [-1] * (n + 1)
    return find(delay, forget, n, arr)
    
 
n = int(input())
delay = int(input())
forget = int(input())
print(People_with_Secret(n, delay,forget))
