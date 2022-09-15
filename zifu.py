from collections import defaultdict

str  = input("Please input a string:")

str = str.lower()

chars = defaultdict(int)

for char in str:
    chars[char] += 1

chars = sorted(chars.items(),key=lambda x: x[1],reverse=True)

print(chars)
