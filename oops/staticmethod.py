import random

class User:
	def __init__(self,username,password):
		self.username = username
		self.password = password
		
	@staticmethod
	def generate_password():
		return ''.join(random.choices('abcdefgh1234567890',k=8))
		
print(User.generate_password())