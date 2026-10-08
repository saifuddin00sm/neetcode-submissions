class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = len(nums)
        for i in range(m):
            for j in range(i + 1, m):
                is_target_num = nums[i] + nums[j]
                if is_target_num == target:
                    return [i, j]

        return []