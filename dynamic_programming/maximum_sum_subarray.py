class MaximumSum:
    def max_sum_subarray(self, nums):
        result_sum = nums[0]
        new_max = nums[0]
        for i in range(1, len(nums)):
            if result_sum <= 0:
                result_sum = nums[i]
            else:
                result_sum += nums[i]
                new_max = max(result_sum, new_max)
        return new_max

m = MaximumSum()
print(m.max_sum_subarray([-2, 1]))