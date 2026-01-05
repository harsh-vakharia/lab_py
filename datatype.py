Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
x="how are you"
print(x)
how are you
x=40
print(x)
40
x=20.5
print(x)
20.5
x=1j
print(x)
1j
x=["apple","banana","cherry"]
print(x)
['apple', 'banana', 'cherry']
x=("apple","banana","cherry")
print(x)
('apple', 'banana', 'cherry')
x=range(6)
print(x)
range(0, 6)
x={"name":"john","age":21}
print(x)
{'name': 'john', 'age': 21}
x={"apple","banana","cherry"}
print(x)
{'apple', 'cherry', 'banana'}
x=range(8)
print (list (x) )
[0, 1, 2, 3, 4, 5, 6, 7]
x=frozenset({"apple","banana","cherry"})
print(x)
frozenset({'apple', 'cherry', 'banana'})
x=true
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    x=true
NameError: name 'true' is not defined. Did you mean: 'True'?
x='true'
print(x)
true
x=b"hello"
print(x)
b'hello'
x=byte array(6)
SyntaxError: invalid syntax
