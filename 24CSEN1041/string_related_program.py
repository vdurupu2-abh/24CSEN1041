# String initialization
s1 = "Abhiram"
s2 = 'Python'
s3 = """Welcome Abhiram to string demo"""

print("s1 =", s1)
print("s2 =", s2)
print("s3 =", s3)
print()

# Accessing strings (indexing)
print("First character of s1:", s1[0])        # A
print("Last character of s1:", s1[-1])        # m
print()

# Basic operations
# Concatenation
s4 = s1 + " loves " + s2
print("Concatenation (s1 + ' loves ' + s2):", s4)

# Repetition
s5 = s1 * 2
print("Repetition (s1 * 2):", s5)

# Length
print("Length of s3:", len(s3))

# Membership
print("'Abi' in s1?", "Abi" in s1)
print("'Ram' not in s2?", "Ram" not in s2)
print()

# String slicing
text = "AbhiramCoding"
print("text =", text)

print("text[0:4]   =", text[0:4])     
print("text[3:]    =", text[3:])      
print("text[:5]    =", text[:5])      
print("text[-4:]   =", text[-4:])     
print("text[::2]   =", text[::2])     
print("text[::-1]  =", text[::-1])    
print()

# String functions and methods
sample = "   abhiram loves python   "
print("Original sample: '", sample, "'", sep="")

# strip: remove leading/trailing spaces
print("strip()       -> '", sample.strip(), "'", sep="")

# upper and lower
print("upper()       ->", sample.upper())
print("lower()       ->", sample.lower())

# replace
print("replace('python', 'Java') ->", sample.replace("python", "Java"))

# split (by whitespace)
words = sample.strip().split()
print("split() ->", words)

# join
joined = "-".join(words)
print("'-'.join(words) ->", joined)

# find
print("find('python') ->", sample.find("python"))

# count
print("count('a') ->", sample.count("a"))

# startswith / endswith
print("startswith('   ab') ->", sample.startswith("   ab"))
print("endswith('python   ') ->", sample.endswith("python   "))

# isalpha / isdigit
only_letters = "Abhiram"
only_digits = "2025"
print("'Abhiram'.isalpha() ->", only_letters.isalpha())
print("'2025'.isdigit() ->", only_digits.isdigit())

Output
s1 = Hello
s2 = D.V.Abhiram
s3 = Welcome to string demo

First character of s1: H
Last character of s1: o

Concatenation (s1 + ' ' + s2): Hello D.V.Abhiram
Repetition (s1 * 3): HelloHelloHello
Length of s3: 22
'Py' in s2? False
'java' not in s2? True

text = Programming
text[0:4]   = Prog
text[3:]    = gramming
text[:5]    = Progr
text[-4:]   = ming
text[::2]   = Pormig
text[::-1]  = gnimmargorP

Original sample: '   hello python world   '
strip()       -> 'hello python world'
upper()       ->    HELLO PYTHON WORLD   
lower()       ->    hello python world   
replace('python', 'Java') ->    hello Java world   
split() -> ['hello', 'python', 'world']
'-'.join(words) -> hello-python-world
find('python') -> 9
count('l') -> 3
startswith('   he') -> True
endswith('world   ') -> True
'HelloWorld'.isalpha() -> True
'12345'.isdigit() -> True
