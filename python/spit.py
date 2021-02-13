panagram = """there 
quick \t thing never 
quit"""

words = panagram.split()
print(words)

numbers = "9,323,433,133,343,324,234,123"
print(numbers.split(","))

generated_list = ['9', ' ',
                  '2', '2', '3', ' ',
                  '3', '7', '2', ' ',
                  '0', '5''8', ' ',
                  '7', '7', '5'' ',
                  '8', '0', '7']
values = "".join(generated_list)
print(values)

values_list = values.split()
print(values_list)
for index in range(len(values_list)):
    values_list[index] = str(values_list[index])

print(values_list)

integer_values = []
for value in values_list:
    integer_values.append(int(value))

    print(integer_values)
