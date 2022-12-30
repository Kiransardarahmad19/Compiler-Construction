import re
reguarexpression = "a+(b*c)"
x = re.findall("\w", reguarexpression)
y = re.split("\w", reguarexpression,5)
print(x,y)
