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

def encode_file(path):
	with open(path, "r") as f:
		text = f.read()
		return (encode(text))

def decode_file(path1):
	with open(path1, "r") as f:
		text = f.read()
		return (decode(text))


print(encode_file("mixed_typed_list.py"))