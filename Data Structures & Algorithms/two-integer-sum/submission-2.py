class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Case: 2->1 
        number_to_index_map = {}

        for i in range(len(nums)):
            number_to_index_map[nums[i]] = i
        
        for i in range(len(nums)):
            search_value = target - nums[i]
            if search_value in number_to_index_map.keys() and number_to_index_map[search_value] != i:
                return [i, number_to_index_map[search_value]]
            