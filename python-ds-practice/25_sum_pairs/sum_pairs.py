def sum_pairs(nums, goal):
    """Return tuple of first pair of nums that sum to goal.

    For example:

        >>> sum_pairs([1, 2, 2, 10], 4)
        (2, 2)

    (4, 2) sum to 6, and come before (5, 1):

        >>> sum_pairs([4, 2, 10, 5, 1], 6) # (4, 2)
        (4, 2)

    (4, 3) sum to 7, and finish before (5, 2):

        >>> sum_pairs([5, 1, 4, 8, 3, 2], 7)
        (4, 3)

    No pairs sum to 100, so return empty tuple:

        >>> sum_pairs([11, 20, 4, 2, 1, 5], 100)
        ()
    """
    
    #creates empty set
    already_visited = Set()

    # for loop iterates through nums
    for num in nums:
        # sets target which is the goal minus current num
        target = goal - num

        # if the target number is in the already_visited set
        # the target number and current number will be returned as they are the first pair to matc the goals
        if target in already_visited:
            return (target, num)
        
        # the current num will be added to already_visited
        already_visited.add(num)

    # if no pairs add to goal return empty tuple
    return()




