arr = list(map(int, input("Enter the values: ").split()))

k = int(input("Enter the rotations needed: "))
k = k % len(arr)
nums = arr[-k:] + arr[:-k]
print(nums)