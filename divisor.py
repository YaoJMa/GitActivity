def divisor(n):
	i = 1
	while i <= n:	
		if (n % i==0):
			print(i) 
		i = i + 1

print("The divisors for 100 is: ")
divisor(100)
