#547-658-42567
import re
sentence="My mobile no is 547-657-9687"
pattern = re.compile("\d{3}-\d{3}-\d{4}")
print(pattern.search(sentence))