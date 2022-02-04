nums = list(map(int, input().split()))

def minimumArray(nums):
    left = 0
    right = len(nums) - 1
    mid = (left + right) // 2

    while left <= right:
        if nums[mid] > nums[left]:
            right = mid - 1
        elif nums[mid]




minimumArray(list)

