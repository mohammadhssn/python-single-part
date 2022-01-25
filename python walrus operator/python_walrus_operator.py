"""
    walrus :=
        assign, return
"""

name = 'sara'
print(name)

print(name := 'ali')

###########################################

inputs = list()

while current := input('enter value: ') != 'quit':
    inputs.append(current)

###########################################

if x := len(name) < 4:
    print(x)
    print('error')
