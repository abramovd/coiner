# -*- coding: utf-8 -*-
import hashlib


class User(object):
	def __init__(self, username, password, name=None, email=None):
		"""
		Конструктор класса

		:param username: Имя пользователя
		:type username: str
		:param password: Пароль
		:type password: str
		:param name: Имя
		:type name: str
		:param email: Email
		:type email: str
		:return: None
		:rtype: None
		"""
		self.username = username
		self.password = self._hash_password(password)
		self.name = name
		self.email = email
		self.is_login = False

	def _check_password(self, real_password):
		"""
		Провереряет равенство пароля класса
		User с real_password

		:param real_password: Пароль
		:type real_password: str
		:return: True or False
		:rtype: Bool
		"""
		return hashlib.md5(real_password.encode()).hexdigest() == self.password

	@staticmethod
	def _hash_password(real_password):
		"""
		Шифрует пароль

		:param real_password: Пароль
		:type real_password: str
		:return: Pfibahjdfyysq real_passwor
		:rtype: str
		"""
		return hashlib.md5(real_password.encode()).hexdigest()

	def login(self, real_password):
		"""
		Вход в профиль

		:param real_password: Пароль
		:type real_password: str
		:return: False or (True or False)
		:rtype: Bool
		"""
		if self.is_login:
			print "You already logged in"
			return False
		self.is_login = self._check_password(real_password)
		if self.is_login:
			print 'You have succefully logged id'
		else:
			print 'Not correct password'
		return self.is_login

	def logout(self):
		"""
		Выход из профиля
		"""
		if self.is_login: 
			self.is_login = False
		else:
			raise ValueError("Cannon log out. You not logged in")
			
	@classmethod
	def db_all(cls):
		"""
		return [User(), User(), User()]
		"""
		pass
    
	@classmethod
	def db_filter(cls, **kwargs):
		"""
		Возвращает отфильтрованный список пользователей
		return [User(), User(), User()]
		User.db_filter(username='test', email='em@em.ru', dsadas=21)
		{'username': 'test', 'email': 'em@em.ru', 'dsadas': 21}
		"""
		pass
    
	def db_get(cls, **kwargs):
		"""
		Возвращает лишь одно пользователя,
		удовлетворяющего критериям фильтра в kwargs,
		либо если такого пользователя нет или их больше,
		чем один, то raise DatabaseError
		"""
		pass