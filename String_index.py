print("EXAMPLES USING INDEX()")

print("DESCRIPTION = Python string method index() determines if string str occurs in string or in a substring of string if starting index beg and ending index end are given.")
print("This method is same as find(), but raises an exception if sub is not found.")
print("__SYNTAX__ = str.index(str, beg = 0 end = len(string))")
print("*******__EXAMPLES ARE GIVEN BELOW__*******")

print("EXAMPLE 1: ")
str1 = "this is string example....wow!!!";
str2 = "exam";
print(str1.index(str2))
print(str1.index(str2, 10))

print("EXAMPLE 2:")
txt = "Hello, welcome to my world."
x = txt.index("welcome")
print(x)

print("EXAMPLE 3:")
text = "Hello, welcome to KL University."
print(text.index("K"))

print("EXAMPLE 4:")
text1 = 'Python is easy to learn'
result = text1.index("i")
print(result)

print("EXAMPLE 5:")

str6 = 'Welcome to Python Class'
print(str6.index("P"))

