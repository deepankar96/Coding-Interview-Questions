class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def searchInsert(self, A, B):

        def binarySearch (arr, l, r, x): 
            if r >= l: 
          
                mid = (l+r)/2
          
                # If element is present at the middle itself 
                if arr[mid] == x: 
                    return mid 
                  
                # If element is smaller than mid, then it can only 
                # be present in left subarray 
                elif arr[mid] > x: 
                    binarySearch(arr, l, mid-1, x) 
          
                # Else the element can only be present in right subarray 
                else: 
                    binarySearch(arr, mid+1, r, x) 
          
            else: 
                # Element is not present in the array
                return 4
        print(binarySearch (A, 0, len(A), B))
