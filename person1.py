
import random

chars = '''ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789,./;'[]!@#$%^&*()_+~\|:"<>?'''
times = int(input('[.]Number of passwords?\n[.]'))
length = int(input('[.]Password length?\n[.]'))

f = open('path/location','w')

while(true)
	password = ''
	for j in range(length):
		password += random.choice(chars)

	print('[.]',password,sep='')
