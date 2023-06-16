# Given a fixed-length integer array arr, duplicate each occurrence of zero,
# shifting the remaining elements to the right.

def duplicateZeros(self, original_arr):
    # move the elements from the array to the new array
    new_arr = original_arr[:]
    # clear the array 
    original_arr[:] = []
    
    # traverse through the array, and find where the array element is a 0
    for i in range(len(new_arr)):
    # if the elements in the array is a 0, then insert a 0 to the right of it
        if new_arr[i] == 0:
            original_arr.append(0)
        
        # if it is another element other than 0, then 
        original_arr.append(new_arr[i])
    
    # delete the length of the original array 
    del original_arr[len(new_arr):]



