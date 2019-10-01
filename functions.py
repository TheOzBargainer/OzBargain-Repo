# some practice coding
i = 10
while i < 11:
    print("damn")
    i = i + 1

items = [1, 2, 3]

def parse_lists(some_list):
    str_list_items = []
    num_list_items = []
    for i in some_list:
        if isinstance(i, float) or isinstance(i, int):
            num_list_items.append(i)
        elif isinstance(i, str):
            str_list_items.append(i)
        else:
            pass
    return str_list_items, num_list_items

print(parse_lists(items))

list_item = [123, 3234, "adfasd"]
items2 = ["Mic", "Phone", list_item]

items5 = [200, 300, 400]

def my_sum(my_num_list):
    total = 0
    for i in my_num_list:
        if isinstance(i, float) or isinstance(i, int):
            total += i
    return total


print(my_sum(items5))
