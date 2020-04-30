def new(obj: object) -> object:
	'''
DOC OF 'new(obj)'
This function is used to clone an object.
Use 'a=b', you may make 'a' and 'b' the same object, and changes on 'a' causes changes on 'b'.
But by using 'a=new(b)', you will clone 'b' to 'a', then changes on 'a' is only changes on 'a'.
'''
	class nil: # create a nil class
		def __init__(self):
			pass
	new_obj = nil() # copy obj to new_obj
	for arg in obj.__dir__(): # get all attributes
		if arg[:2] != '__' and arg[-2:] != '__': # select user attributes
			if type(obj.__getattribute__(arg)) == type(''): # add quote if value is str
				exec('new_obj.%s = "%s"' % (arg, obj.__getattribute__(arg)))
			else:
				exec('new_obj.%s = %s' % (arg, str(obj.__getattribute__(arg))))
	new_obj.__class__ = obj.__class__
	return new_obj
