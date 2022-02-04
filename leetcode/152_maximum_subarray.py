nums = list(map(int, input().split()))

def maxProduct(nums):
    maxnum = big = small = nums[0]
    for n in nums[1:]:
        big, small = max(n, n * big, n * small), min(n, n * big, n * small)
        maxnum = max(maxnum, big)
    return maxnum


maxProduct(nums)

