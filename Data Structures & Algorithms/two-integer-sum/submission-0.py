class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) < 2:
            return [-1, -1] # Invalid input
        
        index_hashmap = {}

        for index, num in enumerate(nums):
            target_array_num = target - num
            if target_array_num not in index_hashmap:
                index_hashmap[num] = index
            else:
                return [index_hashmap[target_array_num], index]

            
        