def isPairSum(lst, x):
 
    # initialize left pointer to index 1
    l_ptr = 0
 
    # initialize right pointer to last index
    r_ptr = len(lst) - 1

    # Loops until left and right pointers cross paths
    while(l_ptr < r_ptr):
       
        # Check if pair is equal to target value
        if (lst[l_ptr] + lst[r_ptr] == x):
            return True
 
        # If sum of elements at current pointers is
        # less than target, move left pointer rightward

        elif(lst[l_ptr] + lst[r_ptr] < x):
            l_ptr += 1
 
        # If sum of elements at current pointers is
        # higher than target, move right pointer leftward
        else:
            r_ptr -= 1
        
    # Returns False if target value not found.
    return False
 
print(isPairSum([10, 20, 35, 50, 75, 80], 70))