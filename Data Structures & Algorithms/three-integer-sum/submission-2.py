class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result_set  = set()
        search_set = set()
        nums.sort()
        for i, outer_num in enumerate(nums):
            if outer_num in search_set:
                continue
            search_set.add(outer_num) # No re-checking
            target = -outer_num
            search_array = nums[i + 1:]
            two_sum_result = self.twoPointer(target, search_array)
            print(two_sum_result)
            for inner_loop_result in two_sum_result:
                num1, num2 = inner_loop_result
                result_set.add(tuple(sorted([outer_num, num1, num2])))
            
        
        return [list(t) for t in result_set]


    def twoPointer(self,  target: int, search_array: list[int]) -> list[tuple]:
        L, R = 0, len(search_array) - 1
        res = [] 
        while L < R:
            total = search_array[L] + search_array[R]
            if total < target:
                L += 1
            elif total > target:
                R -= 1
            else:
                res.append([search_array[L], search_array[R]])
                L += 1
                R -= 1
        return res 

    def twoSum(self, target: int, nums: List[int]) -> list[tuple]:
        seen = {}
        res = []
        for i, inner_num in enumerate(nums):
            match = target - inner_num
            if match in seen:
                res.append([match, inner_num])
            seen[inner_num] = i
        return res
                
