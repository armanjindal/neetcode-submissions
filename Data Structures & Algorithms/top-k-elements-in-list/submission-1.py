from collections import defaultdict
import math

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict = defaultdict(int)
        for num in nums:
            count_dict[num] += 1
        
        print(count_dict)

        result_array = []
        for i in range(k):
            max_number, max_count = -math.inf,-math.inf
            
            for number,count in count_dict.items():
                if count > max_count:
                    max_number = number
                    max_count = count
            
            result_array.append(max_number)
            count_dict.pop(max_number)
        
        return result_array


