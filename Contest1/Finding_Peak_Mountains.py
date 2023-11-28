def find_peak_mountains(heights):

    peak_count = 0
    peak_heights = []

    for i in range(1, len(heights) - 1):
        if heights[i] > heights[i - 1] and heights[i] > heights[i + 1]:
            peak_count += 1
            peak_heights.append(heights[i])

    if heights[0] > heights[1]:
        peak_count += 1
        peak_heights.append(heights[0])
    if heights[-1] > heights[-2]:
        peak_count += 1
        peak_heights.append(heights[-1])

    print(peak_count)
    print(" ".join(map(str, peak_heights)))

try:
    input_str_1 = list(map(int, input().strip().split()))
    find_peak_mountains(input_str_1)
except:
    print("Input was not in a correct format")
