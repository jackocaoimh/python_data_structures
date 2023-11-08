def multiply_even_numbers(nums):

    evens = []

    for num in nums:
        if num % 2 == 0:
            evens.append(num)
        
    if len(evens) == 0:
        return 1
    elif len(evens) == 1:
        return evens[0]
    
    answer = 1

    for even_num in evens:
        answer * even_num

        return answer






    """Multiply the even numbers.
    
        >>> multiply_even_numbers([2, 3, 4, 5, 6])
        48
        
        >>> multiply_even_numbers([3, 4, 5])
        4
        
    If there are no even numbers, return 1.
    
        >>> multiply_even_numbers([1, 3, 5])
        1
    """