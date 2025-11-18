import re, random

def generate(lenght):
    a = [0,0,0]
    symbl = list('abcdefghijklmnopqrstuvwxyz')
    s2 = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    s3 = list('0123456789')
    s4 = list('!@#$%^&*')

    a[0] = input('Добавить заглавные буквы в пароль?(д/н):')
    a[1] = input('Добавить цифры в пароль?(д/н):')
    a[2] = input('Добавить спец.символы в пароль?(д/н):')
    if a[0].lower()=='д': symbl += s2
    if a[1].lower()=='д': symbl += s3
    if a[2].lower()=='д': symbl += s4

    password = ''
    for i in range(lenght):
        password += random.choice(symbl)

    a = input('Сохранить пароль в файл "password.txt"?(д/н):')
    if a.lower() == 'д':
        with open('password.txt','w') as f:
            f.write(password)
    return password

def check(password):
    if re.match(r'^[a-zA-Z]+$',password) or len(password) < 8:
        s = [0,0,0]
        if re.match(r'^[a-zA-Z]+$',password):
            s[0] = '\nAdd numbers'
        if len(password) < 8:
            s[1] = '\nDo password longer'
        
        q = password[0]
        for i in range(1,len(password)):
            if q != password[i]:
                q = ''
        if q:
            q = '\nAll symbls equally'

        return f'LowProtectionLever{s[0]}{s[1]}{q}'
    elif re.match(r'^[0-9a-zA-Z]+$',password) and len(password) >= 8:
        return f'MiddleProtectionLevel\nAdd Special Symbles'
    elif re.match(r'^[0-9a-zA-Z!@#$%^&*]+$',password) and len(password) >= 10:
        return 'HighProtectionLevel'
    return 'UnusablePassword\nYou use un correct symbles'

def main():
	p='Не выбран режим'
	a = input('Режим 1(Генерация) или 2(Проверка):')
	if a=='1':
		p = generate(int(input('Длина:')))
	elif a=='2':
		p = check(input('Ваш пароль:'))
	print(p)


if __name__ == '__main__':
	main()
