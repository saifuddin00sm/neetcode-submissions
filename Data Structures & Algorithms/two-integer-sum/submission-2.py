class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                is_target_num = nums[i] + nums[j]
                if is_target_num == target:
                    return [i, j]

        return []