print("Muhammad Bassam")
print("18B-077-CS(A)")
print("Lab - 05")
print("Home Task - 4\n\n")

def check_palindrome(string):
    string = string.casefold()
    reverse = string[::-1]
    if reverse==string:
        print("\nYes, this string is Palindrome")
    else:
        print("\nNo, this string is not Palindrome")

user = input("Please enter a string to check wether its Palindrome or not : ")
check_palindrome(user)
