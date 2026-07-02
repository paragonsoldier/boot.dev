def merge_sort(nums: list[int]) -> list[int]:
    # Input: `A`, an unsorted list of integers

    # If the length of `A` is less than 2, it's already sorted so return it
    if len(nums) < 2:
        return nums

    # Split the input array into two halves down the middle
    mid = len(nums) // 2
    left_side = nums[:mid]
    right_side = nums[mid:]

    # Call `merge_sort()` twice, once on each half
    left_side = merge_sort(left_side)
    right_side = merge_sort(right_side)

    # Return the result of calling `merge(sorted_left_side, sorted_right_side) on the results of the merge_sort() calls
    return merge(left_side, right_side)


def merge(first: list[int], second: list[int]) -> list[int]:
    # Inputs: `A` and `B`. Two sorted lists of integers

    # Create a new `final` list of integers.
    final = []

    # Set `i` and `j` equal to zero. They will be used to keep track of indexes in the input lists (`A` and `B`).
    i = 0
    j = 0

    # Use a loop to compare the current elements of `A` and `B`:
    # While `i < len(A)` and `j < len(B), compare `A[i]` and `B[j]`. 
    # Append the smaller or equal value to `final`.
    while i < len(first) and j < len(second):
        # compare `A[i]` and `B[j]`. Append the smaller or equal value to `final`. 
        if first[i] <= second[j]:
            final.append(first[i])

            # Increment the index for the list you just took from.
            i += 1
        else:
            final.append(second[j])

            # Increment the index for the list you just took from. 
            j += 1
        
        # Stop when either list is exhausted (handled by the while loop). 

    # After comparing all the items, there may be some items left over in either `A` or `B`. Add those extra items to the final list. 
    final.extend(first[i:])
    final.extend(second[j:])

    # Return the final list. 
    return final
