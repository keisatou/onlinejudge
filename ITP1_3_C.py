while True:
    nums = input().split(' ')
    if (nums.count('0') == 2):
        break
    nums_sorted = sorted(nums)
    print(' '.join(nums_sorted))
