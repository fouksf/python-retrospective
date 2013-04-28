SIGNS = {"Водолей": range(120, 219), "Риби": range(219, 321),
         "Овен": range(321, 421), "Телец": range(421, 521),
         "Близнаци": range(521, 621), "Рак": range(621, 722),
         "Лъв": range(722, 823), "Дева": range(823, 923),
         "Везни": range(923, 1023), "Скорпион": range(1023, 1122),
         "Стрелец": range(1122, 1222)}


def what_is_my_sign(day, month):
    """Return zodiac sign by given day and month of birth."""
    zodiac_code = 100 * month + day

    for key, value in SIGNS.items():
        if zodiac_code in value:
            return key
        else:
            "Козирог"
