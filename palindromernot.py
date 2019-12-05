###the string is palindrome are not###
string=raw_input("Enter a String:")
if(string==string[::-1]):
    print("The string is a palindrome")
else:
    print("The string isn't a palindrome:")
