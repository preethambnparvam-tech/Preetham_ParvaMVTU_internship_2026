sentence = "My name is Preetham"

# String Methods
# upper
print(f"Sentence in Uppercase: {sentence.upper()}")

# lower
print(f"Sentence in Lowercase: {sentence.lower()}")

# title
print(f"Sentence in Title Case: {sentence.title()}")

#swapcase
print(f"Sentence in Swap Case: {sentence.swapcase()}")

#capitalize
print(f"Sentence in Capitalized Case: {sentence.capitalize()}")

#find
print(f"A is found at {sentence.find('a')} position")

#index
print(f"E is found at {sentence.index('e')} position")

#rfind
print(f"Last A is found at {sentence.rfind('a')} position")

#rindex
print(f"Last E is found at {sentence.rindex('e')} position")

#count
print(f"Number of times 'e' is found: {sentence.count('e')}")

#startswith
print(f"Does the sentence start with 'my'? {sentence.startswith('my')}")

#endswith
print(f"Does the sentence end with 'Preetham'? {sentence.endswith('Preetham')}")

#len
print(f"Length of the sentence: {len(sentence)}")

#isalpha
string = "Preetham"
str1 = "preetham123"
str2 = "1234"
str3 = "123.4"
print(f"Is the string only alphabets? {string.isalpha()}")
print(f"Is str1 only alphabets? {str1.isalpha()}")

#isdigit
print(f"Is str2 only digits? {string.isdigit(), str1.isdigit(), str2.isdigit(), str3.isdigit()}")

#isdecimal
print(f"Is str2 only decimal? {string.isdecimal(), str1.isdecimal(), str2.isdecimal(), str3.isdecimal()}")

#isalnum
print(f"Is str1 only alphanumeric? {string.isalnum(), str1.isalnum(), str2.isalnum(), str3.isalnum()}")

#lower
print(f"Is the sentence in lowercase? {"preetham".islower(), "Preetham".islower()}")

#upper
print(f"Is the sentence in uppercase? {"PREETHAM".isupper(), "Preetham".isupper()}")

#title
print(f"Is the sentence in title case? {"Preetham".istitle(), "preetham".istitle()}")