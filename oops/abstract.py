from abc import *
class Bank(ABC):
	@abstractmethod
	def calculateInterest(self):
		pass
		
		
class SBI(Bank):
	def calculateInterest(self):
		return 5
	
sbi = SBI()
print(sbi.calculateInterest())