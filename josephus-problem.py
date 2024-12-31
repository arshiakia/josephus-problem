def josephus(n, k):  
    if n == 1:  
        return 0  
    
    return (josephus(n - 1, k) + k) % n  

n = int(input("Enter the number of people (n): "))  
k = 2  

position = josephus(n, k) + 1  
print(f"The safe position is {position}")