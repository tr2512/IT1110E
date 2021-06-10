def mysum(n):
    sum = 0
    for i in range (1,n+1):
        sum += i**2 * (-1)**(i+1)
    return sum
