def kata(number):
    sub_str = ""
    sum_of_num = 0
    if number == "":
        return 0

    if len(number) == 1:
        return int(number)

    for i in number:
        if i == ',' or i == "\n":
            sum_of_num += int(sub_str)
            sub_str = ""
        else:
            sub_str += i
    return sum_of_num


def test_kata():
    assert kata("1000,2") == 6