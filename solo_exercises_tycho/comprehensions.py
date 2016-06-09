#http://www.diveintopython3.net/comprehensions.html
##########list comprehensions###############

a_list = [1,2,3,4,6,8]

compreh = [elem * 2 for elem in a_list]

print (compreh)

b_list = [elem * 2 for elem in a_list]

print (b_list)

uneven = [f for f in a_list if f % 2 == 1]

print (uneven)

uneven_and_multiple = [(f, f*2) for f in a_list if f % 2 == 1]

print (uneven_and_multiple)


############## Dictionary comprehensions ###############
dict = {f: f * 2 for f in a_list}

print (dict)

a_dict = {'a': 1, 'b': 2, 'c': 3}

print (a_dict)

dict_comp = {value:key for key, value in a_dict.items()}

print (dict_comp)

print (a_list)
print (a_list[1::2])

a_list.append([11,222,33])

print (a_list)

a_list.extend([111,33232])

print (a_list)

a_dict = {'a': 1, 'b': 2, 'c': 3}

print ('{a} has {av} items, while {d} has {dv} items'
.format(a = 'a', av = a_dict.get('a', 0), d = 'd', dv =a_dict.get('d', 0)))

a_dict.setdefault('d',2)

print (a_dict)