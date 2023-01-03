number1 = int(input("첫번째 정수를 입력하세요"))
number2 = int(input("두번째 정수를 입력하세요"))

if number1 == number2:
    print("False")
elif number1 > number2:
    array = []
    for i in range(number2+1,number1):
        array.append(i)
    print(array)
else:
    array = []
    for i in range(number1+1,number2):
        array.append(i)
    print(array)