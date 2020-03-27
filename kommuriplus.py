

def num(numstring):
    sub_str = ""
    sum_of_num = 0
    for i in numstring:
        sub_str += i
        if i == ',':
            sub_str = ""
        else:
            if len(sub_str) > 1:
                sum_of_num += int(sub_str)
                sum_of_num -= int(i)
            else:
                sum_of_num += int(sub_str)


print(num("1,22,3,4"))