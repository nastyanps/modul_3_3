#1
def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(4, 8)
print_params(5, 7, 8)
print_params(b=25)
print_params(c=[1, 2, 3])

#2
values_list = [5, True, (1, 4, 7)]
print_params(*values_list)

values_dict = {'a': 5, 'b': True, 'c': (9, 4, 0)}
print_params(**values_dict)

#3
values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)
