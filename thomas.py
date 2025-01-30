import numpy as np

def thomas(a,b,c,d):
    N = len(a)
   
    cp = np.zeros(N,dtype="float64")   
    dp = np.zeros(N,dtype="float64")   
    X = np.zeros(N,dtype="float64")    
    

    cp[0] = c[0]/b[0]                  
    dp[0] = d[0]/b[0]                
    
    #Forward Sweep

    for i in np.arange(1,(N),1):
        dnum = b[i] - a[i] * cp[i-1]   
        cp[i] = c[i]/dnum               
        dp[i] = (d[i]-a[i] * dp[i-1])/dnum  
        
    # Back substitution
    X[(N-1)] = dp[N-1]                  
    for i in np.arange((N-2),-1,-1):    
        X[i] = dp[i] - cp[i]*X[i+1]     
        
    return X

if __name__=="__main__":
    # Example system
    a = [0,-1,-1]    # Lower diagonal elements
    b = [4,4,4]      # Main diagonal elements
    c = [-1,-1,0]    # Upper diagonal elements
    d = [2,4,10]     # Right hand side values

    X = thomas(a,b,c,d)
    print("The Values of X are : ",X)




