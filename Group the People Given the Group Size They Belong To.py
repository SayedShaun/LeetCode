def groupThePeople(groupSizes):
    my_dict = {}
    result = []
    for i, value in enumerate(groupSizes):
        if value in my_dict:
            my_dict[value] = i
            if my_dict[value] == i:
                result.append([i])
        else:
            my_dict[value] = i

    print(my_dict)
    return result


groupSizes = [3, 3, 3, 3, 3, 1, 3]
print(groupThePeople(groupSizes))
