dust = int(input('미세먼지 농도를 입력하시오 : '))

if dust > 150:
    print('매우나쁨')
elif dust > 80:
    print('나쁨')
elif dust > 30:
    print('보통')
elif dust >= 0:
    print('좋음')

print('미세먼지 확인 완료')