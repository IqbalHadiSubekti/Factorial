count = 0

while count == 0:
	def factorial(n):
	    if 1 <= n <= 2:
	        return n
	    elif 3 <= n <= 5:
	        return n + 1
	    elif 6 <= n <= 8:
	        return n + 2
	    elif 9 <= n <= 11:
	        return n + 3
	    else:
	    	print("Input Salah")

	n = int(input("Input: "))
	print("Output:",factorial(n))

	ulangi = str(input("Hitung ulang? ya/tidak: "))

	if ulangi == "ya":
		pass
	elif ulangi == 'tidak':
		break 



