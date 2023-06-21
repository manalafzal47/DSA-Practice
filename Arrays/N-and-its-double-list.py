''' 
Given an array arr of integers, check if there exist two indices i and j such that :

i != j
0 <= i, j < arr.length
arr[i] == 2 * arr[j]
 
'''

class Solution(object):
    def checkIfExist(self, arr):
        for i in range(len(arr)):
            for j in range(len(arr)):     
                if i != j and arr[i] == 2 * arr[j]:
                        return True
        return False