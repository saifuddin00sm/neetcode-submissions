class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique_items = set()

        for item in nums:
            if item in unique_items:
                return True

            unique_items.add(item)


        return False