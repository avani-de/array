# LeetCode 1 - Two Sum

def twoSum(nums, target):
    hashmap = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in hashmap:
            return [hashmap[complement], i]
        hashmap[num] = i

# Example
print(twoSum([2, 7, 11, 15], 9))  # Output: [0, 1]
