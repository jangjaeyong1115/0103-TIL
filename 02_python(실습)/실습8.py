number1 = int(input('정수를 입력하세요 : '))

for i in range(1,10):
    if i % 2 == 1:
        print(i, end=" ")
        break
    
    elif i > 0 :
        print(False)