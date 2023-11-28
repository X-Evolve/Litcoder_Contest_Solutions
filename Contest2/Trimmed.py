import heapq

def find_kth_smallest_trimmed_number(original_numbers, queries):
    result = []
    for i in range(len(queries)):
        k, trim = queries[i]
        min_heap = []
        
        for j in range(len(original_numbers)):
            temp = original_numbers[j]
            trimmed = temp[-trim:]
            heapq.heappush(min_heap, (trimmed, j))
        
        top = None
        while min_heap and k > 0:
            trimmed, top = heapq.heappop(min_heap)
            k -= 1
        
        result.append(top)
        
    return result


original_numbers1 = input().split()
n = int(input())

queries1 = [tuple(map(int, input().split())) for i in range(n)]

output1 = find_kth_smallest_trimmed_number(original_numbers1, queries1)
for i in output1:
    print(i, end=' ')