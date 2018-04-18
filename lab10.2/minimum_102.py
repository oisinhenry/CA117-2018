def minimum(nums):

	if len(nums) == 1:
		return nums[0]

	min_num = minimum(nums[:-1])

	if nums[-1] < min_num:
		return nums[-1]
	else:
		return min_num
