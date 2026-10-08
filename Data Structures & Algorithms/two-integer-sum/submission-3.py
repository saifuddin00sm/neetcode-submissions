class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                is_target_num = nums[i] + nums[j]
                if is_target_num == target:
                    return [i, j]

        return []