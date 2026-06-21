class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        result: list[int] = [] 
        # Algorithm 1 - Brute Force
        # for position in range(len(nums)):
        #     product = 1
        #     for i in range(len(nums)):
        #         if position == i:
        #             continue # exclude self from product
        #         product = product * nums[i]
        #     result.append(product)
        
        # Algorithm 2: 
        # 1.Precompute prefix product
        # 2. Precompute the suffix product
        # 3. Combine the two resutls by taking the 
        
        # Example = [1, 2, 4, 6] 
        # Prefix = [1, 2, 8, 48]
        # Suffix = [48, 48, 24 , 6]
        prefix_products = []
        prefix_aggregator = 1
        for num in nums:
            prefix_aggregator *= num
            prefix_products.append(prefix_aggregator)
        
        suffix_products = []
        suffix_aggregator = 1
        for num in reversed(nums):
            suffix_aggregator *= num
            suffix_products.append(suffix_aggregator)
        
        suffix_products = list(reversed(suffix_products))

        result = [0 for _ in range(len(nums))]

        for i in range(len(nums)):
            result[i] = (prefix_products[i - 1] if i > 0 else 1) * (suffix_products[i+1] if i < len(nums) - 1 else 1)
        
        return result