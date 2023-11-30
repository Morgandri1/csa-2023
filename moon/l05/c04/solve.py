with open("/tmp/randomwordsnumbers.txt", "r") as file:
    data = file.read()
    
with open("/tmp/words.txt", "r") as f:
  	read = f.readlines()

wordNumbers = data.rstrip().split("\n")
out = []

for i in wordNumbers:
		i = int(i)
		out.append(read[i].rstrip())
    
print(" ".join(out))
