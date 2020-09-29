# while loops
'''
name = ''
while name != 'your name':
    print('Please enter your name.')
    name = input()

print('Thank you!')
'''

# while with break
'''
name = ''
while True:
    print('Please enter your name')
    input()
    if name == 'your name':
        break
'''

# continue
spam = 0
while spam < 5:
    spam += 1
    if spam == 3:
        continue
    print(f"spam is {spam}")


# for loops
print("My name is ")
for i in range(5):
    print(f'Jimmy five times {i}')

# add numbers 1 to 100
total = 0
for i in range(101):
    total = total + i
print(total)