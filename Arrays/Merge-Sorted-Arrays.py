'''
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the 
first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

'''

def merge(self, nums1, m, nums2, n):
    
    # copies the m elements from nums1 array into the new array
    new_arr = nums1[:m]
    
    # appends elements from nums2 array into new array 
    new_arr.extend(nums2)
            
    # then sort the elements in increasing order 
    new_arr.sort()

    # update the length of nums1 array to hold the length of m and n combined
    # and also add the new_arr into the nums1
    nums1[:m+n] = new_arr

