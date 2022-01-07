def reverse(nums):
    start_index = 0
    end_index = len(nums) - 1

    while end_index > start_index:
        nums[start_index], nums[end_index] = nums[end_index], nums[start_index]
        start_index = start_index + 1
        end_index = end_index - 1


if __name__ == '__main__':
    n = [25, 5, 63, 21, 54]
    reverse(n)
    print(n)
    
    
