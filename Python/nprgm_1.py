#!/usr/bin/python
def firstex(*args):
	for arg in args:
		print(arg)

def secex(**kwargs):
	if kwargs is not None:
		for key, val in kwargs.iteritems():
			print ("Key=%r, Val=%r" % ( key, val))

firstex('one', 'two', 'three', 'four');
mylist =('apple', 'orange', 3 , 7 );
firstex(*mylist)
secex(lava="1");
mydic = {"one":1, "two":2, "three":3, "four":4};
secex(**mydic);
