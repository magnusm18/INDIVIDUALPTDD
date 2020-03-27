def kata(number):
    if number == "":
        return 0

    if len(number) == 1:
        return int(number)

def test_kata():
    assert kata("1") == 0