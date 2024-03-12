txt_index = "Ваш индекс Руфье: "
txt_workheart = "Работоспособность сердца: "
txt_nodata = 'нет данных для такого возраста'
txt_res = []
txt_res.append('низкая. Срочно обратитесь к врачу!')
txt_res.append('удовлетворительная. Обратитесь к врачу!')
txt_res.append('средняя. Возможно, стоит дополнительно обследоваться у врача.')
txt_res.append('выше среднего')
txt_res.append('высокая')


def ruffier_index(puls1, puls2, puls3):
    res = (4 * (puls3 + puls1 + puls2) - 200) / 10
    return res

def age_test(age, ruff_index):
    if age < 7:
        return txt_index + '0', txt_nodata
    if age >= 7 and age <= 8:
        if ruff_index >= 21:
            return txt_index + str(ruff_index)+ ', '+ "\n"+ txt_workheart + txt_res[0]
        if ruff_index > 17 and ruff_index < 21:
            return txt_index + str(ruff_index)+ ', '+ "\n"+ txt_workheart+ txt_res[1]
        if ruff_index > 12 and ruff_index < 16:
            return txt_index + str(ruff_index)+ ', '+ "\n"+ txt_workheart+ txt_res[2]
        if ruff_index > 6.5 and ruff_index < 11:
            return txt_index + str(ruff_index)+ ', '+ "\n"+ txt_workheart+ txt_res[3]
        if ruff_index <= 6:
            return txt_index + str(ruff_index)+ ', '+ "\n"+ txt_workheart+ txt_res[4]

    if age > 9 and age <= 10:
        if ruff_index >= 19.5:
            return txt_index + str(ruff_index)+ ', '+ "\n"+ txt_workheart+ txt_res[0]
        if ruff_index > 15.5 and ruff_index < 19.5:
            return txt_index + str(ruff_index)+ ', '+ "\n"+ txt_workheart+ txt_res[1]
        if ruff_index > 10.5 and ruff_index < 14.5:
            return txt_index + str(ruff_index)+ ', '+ "\n"+ txt_workheart+ txt_res[2]
        if ruff_index > 5 and ruff_index < 9.5:
            return txt_index + str(ruff_index)+ ', '+ "\n"+ txt_workheart+ txt_res[3]
        if ruff_index <= 4.5:
            return txt_index + str(ruff_index)+ ', '+ "\n"+ txt_workheart+ txt_res[4]

    if age > 11 and age <= 12:
        if ruff_index >= 18:
            return txt_index + str(ruff_index)+ ', '+ "\n"+ txt_workheart+ txt_res[0]
        if ruff_index > 14 and ruff_index < 18:
            return txt_index + str(ruff_index)+ ', '+ "\n"+ txt_workheart+ txt_res[1]
        if ruff_index > 9 and ruff_index < 13:
            return txt_index + str(ruff_index)+ ', '+ "\n"+  txt_workheart+ txt_res[2]
        if ruff_index > 3.5 and ruff_index < 8:
            return txt_index + str(ruff_index)+ ', '+ "\n"+ txt_workheart+ txt_res[3]
        if ruff_index <= 3:
            return txt_index + str(ruff_index)+ ', '+ "\n"+  txt_workheart+ txt_res[4]

    if age > 13 and age <= 14:
        if ruff_index >= 16.5:
            return txt_index + str(ruff_index)+ ', '+ "\n"+ txt_workheart+ txt_res[0]
        if ruff_index > 12.5 and ruff_index < 16.5:
            return txt_index + str(ruff_index)+ ', '+ "\n"+ txt_workheart+ txt_res[1]
        if ruff_index > 7.5 and ruff_index < 11.5:
            return txt_index + str(ruff_index)+ ', '+ "\n"+ txt_workheart+ txt_res[2]
        if ruff_index > 2 and ruff_index < 6.5:
            return txt_index + str(ruff_index)+ ', '+ "\n"+ txt_workheart+ txt_res[3]
        if ruff_index <= 1.5:
            return txt_index + str(ruff_index)+ ', '+ "\n"+ txt_workheart+ txt_res[4]

    if age >= 15:
        if ruff_index >= 15:
            return txt_index + str(ruff_index)+ ', '+ "\n"+ txt_workheart+ txt_res[0]
        if ruff_index > 11 and ruff_index < 15:
            return txt_index + str(ruff_index)+ ', '+ "\n"+ txt_workheart+ txt_res[1]
        if ruff_index > 6 and ruff_index < 10:
            return txt_index + str(ruff_index)+ ', '+ "\n"+ txt_workheart+ txt_res[2]
        if ruff_index > 0 and ruff_index < 5.5:
            return txt_index + str(ruff_index)+ ', '+ "\n"+ txt_workheart+ txt_res[3]
        if ruff_index <= 0:
            return txt_index + str(ruff_index)+ ', ' + "\n" + txt_workheart+ txt_res[4]


def test(puls1, puls2, puls3, age_res):
    ruff_index = ruffier_index(int(puls1), int(puls2), int(puls3))
    result = age_test(int(age_res), int(ruff_index))
    return result




