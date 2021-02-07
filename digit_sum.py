num = int(input('մուտքագրել երկնիշ թիվ՝ '))
print(num//10+num%10)


# #extended version

# while True:
# 	num = input('Մուտքագրեք երկնիշ թիվ՝ ')

# 	if len(num)!=2:
# 		print("Թույլատրվող նիշերի քանակն է ԵՐԿՈՒ:\n")
# 	else:
# 		try:
# 			num = int(num)
# 		except:
# 			print("Թույլատրվում են միայն ԹՎԵՐ:\n")
# 		else:
# 			print(num//10+num%10)
# 			break