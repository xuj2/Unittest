def check_pwd(st):
        l_flag = 0
        if len(st) > 20 or len(st) < 8:
                return False
        for letter in st:
                if letter.islower():
                        l_flag = 1
        if l_flag == 0:
                return False
        return True
