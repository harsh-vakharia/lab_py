Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#assignment operator
x=20
print(x)
20
#unary minus
a=10
print(-a)
-10
#relational
p=15
q=5
print(p>q)
True
print(p==q)
False
#logical
x='true'
y='false'
print(x and y)
false
print(x or y)
true
print(not x)
False
#boolean
is_pass=true
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    is_pass=true
NameError: name 'true' is not defined. Did you mean: 'True'?
is_pass='true'
print(is_pass)
true
#bitwise
a=5
b=2
print(a & b)
0
print(a | b)
7
#membership
numbers=[1,2,3,4,5,6]
print(2 in numbers)
True
print(5 not in numbers)
False
#identify
x=20
y=20
print(x is y)
True
print(x is not y)
False
