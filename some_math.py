def centered_average(nums):
  maxVal = nums[0]
  minVal = nums[0]
  sum = 0
  
  for val in nums:
    maxVal = max(maxVal, val)
    minVal = min(minVal, val)
    sum += val    

  sum -= maxVal
  sum -= minVal
  
  return sum / (len(nums)-2)
