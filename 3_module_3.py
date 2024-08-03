def print_params(a=1, b='строка', c=True, *params):
    print(a, b, c, )


print('--------------------------1 пункт-------------------------')
print_params('ЭДИК', (1, 2))
print_params(b=25)
print_params(c=[1, 2, 3])

print('---------------2 пункт---------------------')
values_list = [1, 'streight', True, [1, 2, 3], (1, 2, 3)]
values_dict = {'a': 1, 'b': 'строка', 'c': True}
print_params(*values_list)

print('-----------------------3 пункт-------------------------')
values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)
