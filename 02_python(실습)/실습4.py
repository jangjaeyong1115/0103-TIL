number = int(input('정수를 입력하시오 : '))

if number > 100:
    print('에러')

elif number >= 60 :
    print('합격')


elif number < 60:
    print('불합격')


elif number < 0:
    print('에러')