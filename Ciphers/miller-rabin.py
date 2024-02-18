def isPrime (n):
    a = 0
    q = 0

    while(True):
        for k in range(1, 1000):
            for q in range(1000):
                if(q%2!=0):
                    if (n-1 == 2**k*q):
                        for i in range(n-1):
                            if i > 1 & i < n-1:
                                a = i
                                if((a**q)%n == 1):
                                    return "inconclusive"
                                else:
                                    for j in range(k):
                                        if((a**(2*j*q))%n==n-1):
                                            return "inconclusive"
        return "composite"                                 

# 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97      
result = isPrime(28)
print(result)