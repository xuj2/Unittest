def check_pwd(st):
        l_flag = 0
        u_flag = 0
        d_flag = 0
        s_flag = 0
        symbols = "~`!@#$%^&*()_+-="
        if len(st) > 20 or len(st) < 8:
                return False
        for letter in st:
                if letter.islower():
                        l_flag = 1
                if letter.isupper():
                        u_flag = 1
                if letter.isdigit():
                        d_flag = 1
                if letter in symbols:
                        s_flag = 1
        if l_flag == 0 or u_flag == 0 or d_flag == 0 or s_flag == 0:
                return False
        return True
