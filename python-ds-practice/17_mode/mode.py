def mode(nums):



    # Make frequency counter of num:freq - dictionary
    counts = {}



    for num in nums:
        # if num is not yet a key it returns 0, frequency increments by +1
        counts[num] = counts.get(num, 0 ) + 1

    #Finds highest frequency 
    max_value = max(counts.values())

    # Iterates through each key:value pair in counts
    for (num, freq) in counts.items():
            # if value freq is equal to max_value
            if freq == max_value:
                # the corresponding key which is num is returned
                return num

