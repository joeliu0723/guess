import random
r = random.randint(1 , 100)

while True:
	x = input('請猜1~100之間的數字')
	x = int(x)
	if x == r:
		print('恭喜你猜對!!')
		break
	elif x > r:
		print('比答案大')
	else:
		print('比答案小')