word = 'mangoe'

# 'e' 있으면 1 출력
# 'e' 없으면 0 출력

is_end = False #T/F
for char in word:
    if char == 'e':
        print(1)
        is_end = True
        break

if is_end:
    print(1)
else:
    print(0)

for char in word:
    if char == 'e':
        print(1)
        break
else: 
    print(0)
