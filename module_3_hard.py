



data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]



def calkulate_structure_sum(data):
    count = 0
    if isinstance(data, int):
        count += data
    elif isinstance(data, str):
        count += len(data)
    elif isinstance(data, (list, tuple, set)):
        for item in data:
            count += calkulate_structure_sum(item)
    elif isinstance(data, dict):
        for key, value in data.items():
            count += calkulate_structure_sum(key)
            count += calkulate_structure_sum(value)
    return count


result = calkulate_structure_sum(data_structure)
print(result)




