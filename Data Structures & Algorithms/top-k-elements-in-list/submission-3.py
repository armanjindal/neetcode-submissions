from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # k = 1
        # max_occurances = len(nums) case: [7,7,7,7]
        # Algorithm - naive map 
        # 1. Create maps the number to the number of time it occurs
        # 2. Iterate through and place values in an array where the index maps to the frequency
        # 3. Iterate backward - return first k results
        
        number_frequency_map = defaultdict(int)
        count_array = [[] for _ in range(len(nums))]
        result_array = []

        for num in nums:
            number_frequency_map[num] += 1 # key = 1, value = frequency of 1
        
        for key, value in number_frequency_map.items(): 
            count_array[value - 1].append(key)
        
        # Iterate backward
        for i in range(len(count_array) - 1, -1, -1):
            for number in count_array[i]:
                result_array.append(number)

        return result_array[0:k]

        # Min heap - use a data structure that stores the 