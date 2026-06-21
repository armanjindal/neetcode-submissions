class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        result: list[int] = [] 
        # Case = [0, 1]
        for position in range(len(nums)):
            product = 1
            for i in range(len(nums)):
                if position == i:
                    continue # exclude self from product
                product = product * nums[i]
            result.append(product)
        
        return result