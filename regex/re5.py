#landline number pattern
#9144-22590000
#914572-256987
#1) 12 digit (r'\d{12}')
#2)(r'\d{4,6}')
#3)(r'\d{6,8}')
#4)(r'(91))
#re.compile(r'((91)\d{2,4})-([1-9][0-9]{5,7})')
import re


landLinePattern = re.compile(r'((91)\d{2,4})-([1-9][0-9]{5,7})')
present =landLinePattern.search("My number is 9144-25689742")
print(present.group())









