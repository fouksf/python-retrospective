def what_is_my_sign(day, month):
    code = 1000 * month + day
    signs = {"Водолей": range(1020, 2019), "Риби": range(2019, 3021),
             "Овен": range(3021, 4021), "Телец": range(4021, 5021),
             "Близнаци": range(5021, 6021), "Рак": range(6021, 7022),
             "Лъв": range(7022, 8023), "Дева": range(8023, 9023),
             "Везни": range(9023, 10023), "Скорпион": range(10023, 11022),
             "Стрелец": range(11022, 12022)}
    for key, value in signs.items():
        if code in value:
            return key
    return "Козирог"
