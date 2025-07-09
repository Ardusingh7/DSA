def brute_force_min_swaps(arr):
    n = len(arr)
    total_ones = arr.count(1)
    if total_ones <= 1:
        print(0)

    min_swaps = float('inf')

    for i in range(n - total_ones+1):
        window = arr[i: i+total_ones]
        print(window)
        zeros_in_window = window.count(0)
        min_swaps = min(min_swaps, zeros_in_window)

    print(min_swaps)

# Example
arr = [1, 1, 0, 0, 0, 0, 1, 1]
brute_force_min_swaps(arr)
