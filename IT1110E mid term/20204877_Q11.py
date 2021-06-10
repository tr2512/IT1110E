def is_decreasing(lst):
    for i in range (1,len(lst)):
        if lst[i] >= lst[i-1]:
            print('NO')
            return None
    print('YES')
