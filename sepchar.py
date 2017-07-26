#!/bin/env python
# -*- coding: utf-8 -*-

""" 
* author Allen.L
* \last modified 2017-07-18 10:55:49
""" 




def is_chinese(uchar):

	if uchar>=u'\u4e00' and uchar<= u'\u9fa5':
		return True
	else:
		return False

def is_number(uchar):
	uchar = uchar.decode ( 'utf8' )
	if uchar>=u'\u0030' and uchar<=u'\u0039':
		return True
	else:
		return False

def is_alpabet(uchar):
	uchar = uchar.decode ( 'utf8' )
	if (uchar >= u'\u0041' and uchar <=u'\u005a') or (uchar >= u'\u0061' and uchar <= u'\u007a'):
		return True
	else:
		return False

def is_other(uchar):
	uchar = uchar.decode ( 'utf8' )
	if not (is_chinese(uchar) or is_number(uchar) or is_number(uchar)):
		return True
	else:
		return False










