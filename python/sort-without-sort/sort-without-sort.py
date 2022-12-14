# Sorting a list of numbers without using the built in sort function

unosrted_list = [-565, -5266, 1025, 3, 63, -64, 223, 706,-5, 7, 0,-56, 60]
sorted_list = []

while unosrted_list:
    minimum = unosrted_list[0]  # arbitrary number in list 
    for x in unosrted_list: 
        if x < minimum:
            minimum = x
    sorted_list.append(minimum)
    unosrted_list.remove(minimum)

print(sorted_list)