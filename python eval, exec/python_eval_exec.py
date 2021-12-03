"""
    eval() - exec()
"""

# show_name = 'print(name)'
#
# eval(show_name, {'name': 'mohammadhssn'})

# show_name = 'name="sara"\nprint(name)'
#
# exec(show_name)

show_name = '''
def show(name):
    print(f"welcome {name}")
show(my_name)
'''

exec(show_name, {'my_name': 'ali'})
