class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        list.sort(nums)
        n = len(nums)
        result = []

        for k in range(n-2):
            #nums[i] + nums[j] = -nums[k] = -num
            if nums[k] > 0:
                break
            
            if k > 0 and nums[k] == nums[k-1]:
                continue
            # solve 2 sum strictly on the subarray to the right of k
            target = -1 * nums[k]
            left = k + 1
            right = n - 1
            while (left < right):
                currentSum = nums[left] + nums[right]
                if (currentSum == target):
                    result.append([nums[left], nums[right], nums[k]])
                    left += 1
                    right -= 1
                    while (left < right) and nums[left]==nums[left-1]:
                        left +=1
                    while (left < right) and nums[right] == nums[right+1]:
                        right -= 1

                elif currentSum < target:
                    left += 1
                else:
                    right -= 1
        
        return result