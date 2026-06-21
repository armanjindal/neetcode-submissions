class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result_set  = set()
        search_set = set()

        for i, outer_num in enumerate(nums):
            if outer_num in search_set:
                continue
            search_set.add(outer_num) # No re-checking
            target = -outer_num
            search_array = nums[i + 1:]
            two_sum_result = self.twoSum(target, search_array)
            for inner_loop_result in two_sum_result:
                num1, num2 = inner_loop_result
                result_set.add(tuple(sorted([outer_num, num1, num2])))
            
        
        return [list(t) for t in result_set]

    def twoSum(self, target: int, nums: List[int]) -> list[tuple]:
        seen = {}
        res = []
        for i, inner_num in enumerate(nums):
            match = target - inner_num
            if match in seen:
                res.append([match, inner_num])
            seen[inner_num] = i
        return res
                
