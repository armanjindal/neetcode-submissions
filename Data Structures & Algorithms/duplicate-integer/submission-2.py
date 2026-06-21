class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # track the counts each number in a dictionary
        seen = set()
        # Go through each number in the list
        for number in nums:
            if number in seen:
                return True
            else:
                seen.add(number)
        return False