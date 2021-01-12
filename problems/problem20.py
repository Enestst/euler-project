goal =1
for i in range(1,101):
	goal *= i
target = 0

for i in str(goal):
	target += int(i)

print(target)
