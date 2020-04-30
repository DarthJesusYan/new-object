# README

``` python
'''
DOC OF 'new(obj)'
This function is used to clone an object.
Use 'a=b', you may make 'a' and 'b' the same object, and changes on 'a' causes changes on 'b'.
But by using 'a=new(b)', you will clone 'b' to 'a', then changes on 'a' is only changes on 'a'.
'''
```
---

## In the past
We clone a object by using:  
`another = this`  
and that causes problems(e.g.): 
``` python
>>> class computer:
	def __init__(self, system, cpu, cores):
		self.system = system
		self.cpu = cpu
		self.cores = cores
>>> this = computer('win7', 'pentium', 2)
>>> another = this
>>> another.system = 'win10'
>>> this.system
'win10'
```
"Complain! I only want to upgrade one computer, but why both of them upgraded?"  

## Now Time Changes!
By using:  
``` python
from new import new
... ...
another = new(this)
```

**It solves that problem!**  

``` python
>>> from new import new
>>> class computer:
	def __init__(self, system, cpu, cores):
		self.system = system
		self.cpu = cpu
		self.cores = cores
>>> this = computer('win7', 'pentium', 2)
>>> print(this.system, this.cpu, this.cores)
win7 pentium 2
>>> print(another.system, another.cpu, another.cores)
win7 pentium 2
>>> another = new(this)
>>> another.system = 'win10'
>>> another.cpu = 'core i7'
>>> another.cores = 8
>>> print(this.system, this.cpu, this.cores)
win7 pentium 2
>>> print(another.system, another.cpu, another.cores)
win10 core i7 8
```
perfect!

