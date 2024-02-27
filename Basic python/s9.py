def binaryToDecimal(binary): 
# binary= binary
	decimal, i,n= 0, 0, 0 
	while (binary != 0):
		dec = binary % 10
		decimal = decimal + dec * pow (2, 1)
		binary = binary // 10
		i += 1
	print(decimal)
# Driver code
if __name__ == '__main__':
	binaryToDecimal(1010)
	binaryToDecimal(100)
	binaryToDecimal(10)