#2
immutable_var = 1, 2, [3, 4], 'a', 'b'
print(immutable_var)

#3
immutable_var[0] = 20 #кортеж, в отличие от списка, относится к неизменяемому типу данных
print(immutable_var)

#4
mutable_list = [1, 2, 'a', 'b']
print(mutable_list)
mutable_list[0] = 20
print(mutable_list)