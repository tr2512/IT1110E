a = int(input())
b = int(input())
while True:
    if a == b:
        break
    if a % 3 == 0 and a > 0:
        a = a//3
        print(':3')
    elif a % 3 ==0 and a <0 :
        a = a + a*2//3
        print(':3')
    elif a % 3 == 1 and a >0:
        a -=1
        print('-1')
    elif a % 3 == 1 and a <0:
        a -= 2
        print('-2')
    elif a % 3== 2 and a <0:
        a -= 1
        print('-1')
    elif a % 3 == 2 and a >0:
        a -= 2
        print('-2')
