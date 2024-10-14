string = input()
N = len(string)

if string == string[::-1]:
    print("Palindrome King!")
else:
    print("Bukan King!")