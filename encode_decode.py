def decode(bin_text):
	result = ""
	for index in range(0,len(bin_text),8):
		cut =slice(index, index+8)
		i=0
		decoded = 0
		for idx in bin_text[cut][::-1]:
			decoded += int(idx)*2**i
			i+=1
		result += chr(decoded)
	return result

def encode(some_text):
	bin_txt=""
	for letter in some_text:
		let_bin = ord(letter)
		res = ""
		while let_bin !=0:
			res+=str(let_bin % 2)
			let_bin //= 2
		add_zero = "0"*(8-len(res))+res[::-1] #adds missing zeroes
		bin_txt += add_zero
	return bin_txt



# to_decode = "01011001011011110111010100100000011011010111010101110011011101000010000001110011011001010110111001100100001000000110000101101110011100110111011101100101011100100111001100100000011101000110111100100000011001010111100001100101011100100110001101101001011100110110010101110011001000000011010000100000011010000110111101110101011100100111001100100000011000100110010101100110011011110111001001100101001000000111010001101000011001010010000001101100011001010111001101110011011011110110111000101110"
# to_encode = "You must send answers to exercises 4 hours before the lesson."
to_encode = "ասդ"
to_decode = "00110001"

#print(decode(to_decode))
print(encode(to_encode))