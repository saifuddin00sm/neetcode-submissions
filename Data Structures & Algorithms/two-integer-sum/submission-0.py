class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                is_equal = nums[i] + nums[j]
                if is_equal == target:
                    return [i, j]

        return []