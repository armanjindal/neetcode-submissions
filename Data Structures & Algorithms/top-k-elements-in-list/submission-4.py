from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        number_frequency_map = defaultdict(int)
        count_array = [] # [[frequency, number]] --> sorted by frequency
        result_array = []

        for num in nums:
            number_frequency_map[num] += 1 # key = 1, value = frequency of 1
        
        for number, count in number_frequency_map.items():
            count_array.append([count, number])

        # Sort by frequency desc
        count_array.sort()

        while len(result_array) < k:
            result_array.append(count_array.pop()[1])

        return result_array

        # Min heap - use a data structure that stores the 