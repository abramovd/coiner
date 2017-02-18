import hashlib
from settings import SECRET_KEY


class User(object):
	def __init__(self, username, password, name=None, email=None):
		self.usename = username
		self.password = self._hash_password(password)
		self.name = name
		self.email = email
		self.is_login = False

	def _check_password(self, real_password):
		return hashlib.md5(real_password.encode()).hexdigest() == self.password

	def _hash_password(self, real_password):
		return hashlib.md5(real_password.encode()).hexdigest()

	def login(self, real_password):
		if self.is_login:
			print "You already logged in"
			return False
		self.is_login = self._check_password(real_password)
		if self.is_login:
			print 'You have succefully logged id'
		else:
			print 'Not correct password'
		return self.is_login

