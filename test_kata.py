def kata(number):
    sum_of_num = 0
    if number == "":
        return 0

    if len(number) == 1:
        return int(number)

    for i in number:
        if i == ',':
            continue
        else:
            sum_of_num += int(i)
    return sum_of_num


def test_kata():
    assert kata("1,2,3,4,5") == 10