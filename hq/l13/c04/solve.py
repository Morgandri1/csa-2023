import base64, string

with open('temp.txt','r') as f:
	strings = [line.strip() for line in f.readlines()]

target = ''
for index, s in enumerate(strings):
	decoded = base64.b64decode(s).decode()
	print(f"index: {index} " + decoded)
	if all(char in string.hexdigits for char in decoded):
		print('found')
		target = s
		break

print(target.lower()) # wtf????
