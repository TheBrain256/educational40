first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']
comb_str = first_strings + second_strings

first_result = [x for x in first_strings if len(x) >= 5]
print(first_result)
second_result = [(x, y) for x in second_strings for y in first_strings if len(x) == len(y)]
print(second_result)
third_result = {x: len(x) for x in comb_str if len(x) % 2 == 0}
print(third_result)