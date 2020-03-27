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
    assert kata("10,2,5,22,1,1") == 15