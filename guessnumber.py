import random
start = input('請定義開始數字')
end = input('請定義結束數字')
r = random.randint(int(start) , int(end))
i = 0
while True:
	i += 1
	x = input('請猜你的數字: ')
	x = int(x)
	if x == r:
		print('恭喜你猜對!!')
		break
	elif x > r:
		print('比答案大')
	else:
		print('比答案小')
	print('你已經猜了', i ,'次')
print('你已經猜了', i ,'次')