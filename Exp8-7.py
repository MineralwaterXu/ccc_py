a_list = eval(input("Please input a list:"))
def bubble_sorted(iterable):
    new_list = list(iterable)
    list_len = len(new_list)
    for i in range(list_len - 1):
        for j in range(list_len - 1, i, -1):
            if new_list[j] < new_list[j - 1]:
                new_list[j], new_list[j - 1] = new_list[j - 1], new_list[j]
    return new_list
print('sorted:', bubble_sorted(a_list))
input("Thank you.Press Enter button to exit.")