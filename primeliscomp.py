###check the number is prime are not using list comprehension###
prime_list=[x for x in range (2,30) if all (x%y !=0 for y in range(2,x) )]
print(prime_list)
