Class Burglary:
    def rob(self, nums):
        max_value = 0
        if len(nums) == 0:
            return 0
        prev = 0
        prev2 = 0
        prev3 = 0
        index = 0
        current = 0
        while index < len(nums):
            current = nums[index]
            if prev2 > prev3:
                current += prev2
            else: current += prev3
            prev3 = prev2
            prev2 = prev
            prev = current
            index += 1
            if current > max_value:
                max_value = current
        return max_value
