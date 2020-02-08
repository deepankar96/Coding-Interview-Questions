def prettyPrint(A):
        size = A + (A-1)
        list1=[]
        
        for i in range(size):
            temp=[0]*size
            list1.append(temp)
        
        def spiralPrint(m, n, a,A) : 
            k = 0; l = 0
          
            ''' k - starting row index 
                m - ending row index 
                l - starting column index 
                n - ending column index 
                i - iterator '''
              
          
            while (k < m and l < n) : 
                  
                # Print the first row from 
                # the remaining rows  
                for i in range(l, n) : 
                    a[k][i]=A 
                      
                k += 1
          
                # Print the last column from 
                # the remaining columns  
                for i in range(k, m) : 
                    a[i][n - 1]=A 
                      
                n -= 1
          
                # Print the last row from 
                # the remaining rows  
                if ( k < m) : 
                      
                    for i in range(n - 1, (l - 1), -1) : 
                        a[m - 1][i]=A 
                      
                    m -= 1
                  
                # Print the first column from 
                # the remaining columns  
                if (l < n) : 
                    for i in range(m - 1, k - 1, -1) : 
                        a[i][l]=A 
                      
                    l += 1
                
                A-=1
            
        spiralPrint(size-1, size-1,list1,A)
            
            
        return list1

print(prettyPrint(3))