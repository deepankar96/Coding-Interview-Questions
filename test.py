def searchMatrix(self, A, B):
        def binarySearch(arr,l,u,x):
            mid = (l+u)/2
            while l<=u:
                if mid == x:
                    return 1
                elif mid > x:
                    u = mid
                elif mid < x:
                    l = mid +1
            return 0
            
        for i in range(len(A[0])):
            if B>A[0][i]:
                row = i-1
                temp = []
                for j in range(len(A)):
                    temp.append(A[row][j])
                return binarySearch(temp,0,len(A),B)
