a = 12
b = 33
'''
c = a + b
print("Sum is",a)
'''

#c = a + b

#walrus operator
#print("Sum is",c := a + b)
#print("Sum of {} and {} is {}".format(a,b,c))

#f-strings - fast strings
print(f"Sum of {a=} and {b=} is {(c := a + b)}")

print(f"""
Add is {(c := a + b)}
Sub is {(c := a - b)}
Div is {(c := a / b)}
Mul is {(c := a * b)}
""")







