f = open('frequency.txt')
line = f.readline()
frequency = 0
print("Calculating frquency")

while line:
	if "+" in line:
		line = line.replace('+','')
		frequency += int(line)
	if "-" in line:
		line = line.replace('-','')
		frequency -= int(line)
	line = f.readline()
f.close()
print("--------")
print(frequency)