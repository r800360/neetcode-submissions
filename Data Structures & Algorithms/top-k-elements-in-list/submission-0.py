class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_nums = defaultdict(int)
        for num in nums:
            count_nums[num] += 1
        
        # k largest keys in count_nums using bucket sort
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, count in count_nums.items():
            buckets[count].append(num)
        
        result = []
        for bucket in reversed(buckets):
            for element in bucket:
                result.append(element)
                if len(result) == k:
                    return result
        return result