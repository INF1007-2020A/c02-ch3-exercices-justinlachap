#def dissipated_power(voltage, resistance):
    #return (voltage ** 2) / resistance


def orthogonal(v1, v2):
    produit = 0
    produit += v1[0] * v2[0]
    produit += v1[1] * v2[1]
    if produit == 0:
        return 'Vrai'
    else:
        return 'Faux'


def average(values):
    moy = 0
    for v in values:
        moy += v

    return moy/len(values)


def bills(value):
    twenties, tens, fives, twos, ones = 0,0,0,0,0
    while value != 0:
        if value >= 20:
            twenties += 1
            value -= 20
        elif value >= 10:
            tens += 1
            value -= 10
        elif value >= 5:
            fives += 1
            value -= 5
        elif value >= 2:
            twos += 1
            value -= 2
        else:
            ones += 1
            value -= 1


    return (twenties, tens, fives, twos, ones)


if __name__ == "__main__":
    #print(dissipated_power(69, 420))
    print(orthogonal((1, 1), (-1, 1)))
    print(average([1, 4, -2, 10]))
    print(bills(137))
