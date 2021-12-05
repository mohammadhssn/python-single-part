"""
    python pdb module
"""
import pdb

nums_list = [500, 300, 444]
alpha_list = ['x', 'y', 'z']


def nested_loop():
    pdb.set_trace()
    for number in nums_list:
        print(number)
        for letter in alpha_list:
            print(letter)


if __name__ == '__main__':
    nested_loop()
