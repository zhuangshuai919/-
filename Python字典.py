Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
>>> 
>>> dict1 = {'ds':1617193144}
>>> dict1
{'ds': 1617193144}
>>> dict1['ds']
1617193144
>>> dict1['ds'] = 161
>>> dict1['ds']
161
>>> del dict1['ds']
>>> dict1['ds']

Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    dict1['ds']
KeyError: 'ds'
>>> dict1
{}
>>>  users = {
    'A':{
    'first':'du',
    'last':'shuang',
    'location':'hs',
    },
    'B':{
    'first':'si',
    'last':'bo',
    'location':'hs',    
    },
}
 
  File "<pyshell#10>", line 2
    users = {
    ^
IndentationError: unexpected indent
>>>  users = {
    'A':{
    'first':'yu',
    'last':'lei',
    'location':'hs',
    },
    'B':{
    'first':'liu',
    'last':'wei',
    'location':'hs',    
    },
}
 
  File "<pyshell#11>", line 2
    users = {
    ^
IndentationError: unexpected indent
>>> 
>>> users = {
	'A':{
		'first':'du',
		'last':'shuang',
		'location':'hs',
		},
	}
>>> for username,userinfo in users.items():
	print("userid��" + username)
	print("userinfo:" + userinfo)

	
userid��A

Traceback (most recent call last):
  File "<pyshell#23>", line 3, in <module>
    print("userinfo:" + userinfo)
TypeError: cannot concatenate 'str' and 'dict' objects
>>> 
>>>  for username, userinfo in users.items():
	print("userid��" + username)
	print("userinfo:" + str(userinfo))
	
  File "<pyshell#25>", line 2
    for username, userinfo in users.items():
    ^
IndentationError: unexpected indent
>>>  for username, userinfo in users.items():
	 print("userid��" + username)print("userinfo:" + str(userinfo))
	 
  File "<pyshell#26>", line 2
    for username, userinfo in users.items():
    ^
IndentationError: unexpected indent
>>>  for username, userinfo in users.items():
	 print("userid��" + username)
	 print("userinfo:" + str(userinfo))
	 
  File "<pyshell#27>", line 2
    for username, userinfo in users.items():
    ^
IndentationError: unexpected indent
>>> for username,userinfo in users.items():
	print("userid: " + username)
	print("userinfo:" + str(userinfo))

	
userid: A
userinfo:{'last': 'shuang', 'location': 'hs', 'first': 'du'}
>>> dict = {'Name':'Tom','Age':7}
>>> print "Value : %s" % dict.keys()
Value : ['Age', 'Name']
>>> for key in dick.keys():
	print key

	

Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    for key in dick.keys():
NameError: name 'dick' is not defined
>>>  print "Key : %s" % dict.keys()
 
  File "<pyshell#37>", line 2
    print "Key : %s" % dict.keys()
    ^
IndentationError: unexpected indent
>>> print "Key : %s" % dict.keys()
Key : ['Age', 'Name']
>>> for key in dict.keys():
	print key

Age
Name
>>> for key in dict.keys():
	print dict[key]

7
Tom
>>> 
