def find_greater_numbers(nums):
    """Return # of times a number is followed by a greater number.

    For example, for [1, 2, 3], the answer is 3:
    - the 1 is followed by the 2 *and* the 3
    - the 2 is followed by the 3

    Examples:

        >>> find_greater_numbers([1, 2, 3])
        3

        >>> find_greater_numbers([6, 1, 2, 7])
        3

        >>> find_greater_numbers([5, 4, 3, 2, 1])
        0

        >>> find_greater_numbers([])
        0
    """
    find = 0
    if len(nums) > 0:
        minN = float('inf')
        for num in nums:
            if num < minN:
                minN = num

        index = nums.index(minN)
        nums2 = nums[index+1:]

        for i in range(len(nums2)):
            k = len(nums2[i:])
            find += k

    return find