class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        zero_count = nums.count(0)
        output = [0] * n

        # Case 1: Two or more zeros -> every entry is 0
        if zero_count > 1:
            return output

        # Calculate product of all non-zero numbers
        total_product = 1
        for x in nums:
            if x != 0:
                total_product *= x

        # Case 2: Exactly one zero
        if zero_count == 1:
            for i in range(n):
                if nums[i] == 0:
                    output[i] = total_product
            return output

        # Case 3: No zeros -> safe to divide
        for i in range(n):
            output[i] = total_product // nums[i]

        return output

