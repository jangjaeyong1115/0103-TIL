a = 'banana'

print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])
print(a[5])

#1.
# 반복 가능한 객체 : 각 요소가 필요할 때

for char in a:
    print(char)
print('=========')

# 2.
# 반복 가능한 객체 : 인덱스가 필요할 때
for i in range(len(a)):
    print(i, a[i])

