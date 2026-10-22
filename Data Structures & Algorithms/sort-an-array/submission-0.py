class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)

        def sift_down(root: int, size: int) -> None:
            value = nums[root]

            # Move the larger child upward until the value can be placed
            while root < size // 2:
                child = 2 * root + 1

                if child + 1 < size and nums[child] < nums[child + 1]:
                    child += 1

                if value >= nums[child]:
                    break

                nums[root] = nums[child]
                root = child

            nums[root] = value


        for i in range(n // 2 - 1, -1, -1):
            sift_down(i, n)

        for end in range(n - 1, 0, -1):
            nums[0], nums[end] = nums[end], nums[0]
            sift_down(0, end)

        return nums