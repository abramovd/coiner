# -*- coding: utf-8 -*-
from models.user import User
from models.wallet import Wallet
from models.Category import Category


class RegistrationError(Exception):
    pass

               
def login():
    username = raw_input("Имя пользователя: ")
    try:
        user = User.db_get(username=username)
    except Exception:
        print 'такого пользователя нет'
    password = raw_input("Пароль: ")
    user.login(password)
    return user

def registration():
    """
    Возвращает пользователя.
    Либо в случае неудачи raise RegistraionError
    
    """
    
    def get_password():
        """
        Ввести пароль и подтвердить его.
        Либо возвращает 1, если не получилось.
        Либо финальный пароль
        
        """
        password = raw_input("Пароль: ")
        repeat_password = raw_input("Повторите пароль: ")
        if password != repeat_password:
            print 'Пароли не совпадают'
            print '1 - Повторить ввод паролей'
            print 'Любой символ - выход'
            choice = raw_input("Ваш выбор: ")
            if choice == '1':
                get_password()
            else:
                return -1
        else:
            return password
        

    try:
        print 'Регистрация'
        username = raw_input("Имя пользователя: ")

        password = get_password()
        if password == -1:
            raise RegistrationError('Не зарегистрирован')

        name = raw_input(
            "Введите имя (не обязательно - нажать Enter): "
        ) or None

        if not isinstance(name, str):
            raise ValueError('Имя должно быть строкой')

        email = raw_input(
            "Введите Email (не обязательно - нажать Enter): "
        ) or None  

        if not isinstance(email, str):
            raise ValueError('Email должен быть строкой')

        if "@" not in email or "." not in email:
            raise ValueError('Некорректный формат Email-а')
     
        user = User(
            username=username,
            password=password,
            name=name,
            email=email
        )
       
        return user
     
    except ValueError as err:
        print 'Ошибка при регистрации:', err.message
        print '1 - Повторить регистрацию'
        print '2 - Другой символ'
        choice = raw_input("Выбор: ")
        if choice == '1':
            pass
        else:
            raise RegistrationError("Ошибка при регистрации")

def start():
    print 'Привет!'
    print 'Что вы хотите сделать: '
    print '1 - Войти\n2 - Зарегистрироваться'
    print 'Любой символ - выйти'
    choice = raw_input('Ваш выбор: ')
    
    if choice == '1':
        pass
    elif choice == '2':
        try:
            user = registration()
            return user
        except RegistrationError as err: 
            print 'Ошибка регистрации ', err.message
            start()
    else:
        exit()


if __name__ == '__main__':
    current_user = start()