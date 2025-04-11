# Mohammad Zafari
# mhdzafari80@gmail.com
 
HAVE_ANSWER = False

def findPair(arr1, arr2, sum): 
    
    global HAVE_ANSWER
    
    m = len(arr1) 
    n = len(arr2) 
    
    #indexes of result pair 
    res_l = 0
    res_r = 0

    l = n - 1
    r = m - 1 

    for i in range(0 , m + n) :
         
        res_l = l 
        res_r = r

        if arr2[l] + arr1[r] > sum:                
            r -= 1
        elif arr2[l] + arr1[r] < sum:  
            l -= 1
        else:  
            #arr2[l] + arr1[r] == sum
            HAVE_ANSWER = True 
            break  
            

    if HAVE_ANSWER == True:
        print('The pair with sum = {} is b[{}] = {}  and  A[{}] = {}'
                .format(sum, res_l, arr2[res_l], res_r, arr1[res_r])) 
    else:
        print("this pair doesn't found !!!!!")


"""
A = [1, 4,7,15,23,48]
B = [17,16,12,10,9,8,3,1,0] 
x=25
findPair(A, B, x) 
"""