#!/usr/bin/env python3


def xml(tagname, text='', **kwargs):
    attributes = ''
    for key, value in kwargs.items():
        attributes += f' {key}="{value}"'
    return f"<{tagname}{attributes}>{text}</{tagname}>"


print(xml('foo'))
# <foo></foo>

print(xml('foo', 'bar'))
# # # # # <foo>bar</foo>

print(xml('p',
          xml('i',
              xml('b', 'Hello'))) )

# # # # # # <p><i><b>Hello</b></i></p>

print(xml('foo', 'bar', a=1))
# # # # # # <foo a="1">bar</foo>

print(xml('foo', 'bar', a=1, b=2))
# # # # # # <foo a="1" b="2">bar</foo>

print(xml('foo', 'bar', a=1, b=2, c=3, d=4))
# # # # # # <foo a="1" c="3" b="2" d="4">bar</foo>


# # def foo(a, b=10, **kwargs): # keyword arguments
# #     print(f"a = {a}, b = {b}, kwargs = {kwargs}")
    
