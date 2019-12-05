###check the number is prime are not###
num=int(raw_input("Enter A Number:"))
if num > 1:
    for i in range(2,num):
        if (num%i)==0:
            print(num,"is not primenumber")
            break
    else:
        print(num,"is a prime number")   
