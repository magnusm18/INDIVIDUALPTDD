def kata(number):
    sub_str = ""
    sum_of_num = 0
    if number == "":
        return 0

    if len(number) == 1:
        return int(number)

    for i in number:
        sub_str += i
        if i == ',':
            sub_str = ""
        else:
            if len(sub_str) > 1:
                sum_of_num += int(sub_str)
                sum_of_num -= int(i)
            else:
                sum_of_num += int(sub_str)
    return sum_of_num


def test_kata():
    assert kata("10,2,5,22,1,1") == 15