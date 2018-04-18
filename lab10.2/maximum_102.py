def maximum(nums):

	if len(nums) == 1:
		return nums[0]

	max_num = maximum(nums[:-1])

	if nums[-1] > max_num:
		return nums[-1]
	else:
		return max_num

