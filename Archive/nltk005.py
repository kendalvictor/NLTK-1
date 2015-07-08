import re

print(ord('e'))
print(hex(101))
print(int(0x0065))
a = 'hello world'
p = re.compile(r'\u0065')
f = re.findall(p, a)
print(f)

stop = 1

