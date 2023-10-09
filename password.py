def is_valid_password(password):
    count = 0
    flag_1 = False
    flag_2 = False
    flag_3 = False   
    c = password.split(':')
    c = [int(i) for i in c]
    if len(c) == 3:
        if str(c[0]) == str(c[0])[::-1]:
            flag_1 = True
        for i in range(1, int(c[1]) + 1):
            if int(c[1]) % i == 0:
                count += 1
        if count == 2:
            flag_2 = True
        if int(c[2]) % 2 == 0:
            flag_3 = True
        if flag_1 == True and flag_2 == True and flag_3 == True:
            return True
        else:
            return False
    else:
        return False
psw = input("Введите пароль: ")
print(is_valid_password(psw))