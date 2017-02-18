# -*- coding: utf-8 -*-
class Keeper(object):
	def __init__(self, name, total_money=0):
		"""
		Конструктор класса

		:param name: Сумма денег
		:type name: str
		:return: None
		:rtype: None
		"""
		self.name = name
		self.total_money = total_money

	def add_money(self, money):
		"""
		Добавляет деньги

		:param money: Сумма денег
		:type money: float
		:return: None
		:rtype: None
		"""
		self.total_money += money

	def move_money(self, money, destination_obj):
		"""
		Переносит деньги из одного кошелька 
		в другой.

		:param money: Сумма денег
		:type money: float
		:param destination: Объект 
		:type destination: models.mixins.Keeper
		:return: None
		:rtype: None
		"""
		if money > self.total_money:
			raise ValueError('Not enough money!')
		else:
			destination_obj.add_money(money)
			self.total_money -= money