def check_pwd(st):
	if len(st) > 20 or len(st) < 8:
		return False
	return True
