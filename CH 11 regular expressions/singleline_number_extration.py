import re
print(sum([ float(i) for i in re.findall('[0-9]+',open('regex_sum_367309.txt').read()) ]))

