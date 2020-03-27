def num(numstring):
    sum_of_num = 0
    for i in numstring:
        if i == ',':
            continue
        else:
            sum_of_num += int(i)

    print(sum_of_num)


print(num("1,2,3,4"))