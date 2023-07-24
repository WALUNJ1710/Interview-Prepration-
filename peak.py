def find_peak_element(nums):
    n = len(nums)

    #Check if the first or last element is peak
    if n==1 or nums[0] >= nums[1]:
        return nums[0]
    if nums[n - 1] >= nums[n - 2]:
        return nums[n - 1]

    # Check the middle elements
    for i in range(1, n-1):
        if nums[i] >= nums[i - 1] and nums[i] >= nums[i+1]:
            return nums[i]

    #If no peak is found, return None or any other sentinal value
    return None

#Example usage:
# 1. Static
#nums = [1,2,3,1] #Peak elements are 3 and 1
#peak_element = find_peak_element(nums)
#print("Peak Element:", peak_element)

# 2. Dynamic
nums = input("Enter a list of numbers seperated by space: ").split()
nums = [int(num) for num in nums]
peak_elements = find_peak_element(nums)
print("Peak Elements:", peak_elements)
