# YouTube : https://www.youtube.com/watch?v=R1PcJfzsUU0

# Regular expressions allow you to locate and change
# strings in very powerful ways.
# They work in almost exactly the same way in every
# programming language as well.

# Regular Expressions (Regex) are used to
# 1. Search for a specific string in a large amount of data
# 2. Verify that a string has the proper format (Email, Phone #)
# 3. Find a string and replace it with another string
# 4. Format data into the proper form for importing for example

# import the Regex module
import re

# ---------- Was a Match Found ----------

# Search for ape in the string
if re.search("ape", "The ape was at the apex"):
    print("There is an ape")

# ---------- Get All Matches ----------

# findall() returns a list of matches
# . is used to match any 1 character or space
allApes = re.findall("ape.", "The ape was at the apex")

for i in allApes:
    print(i)

# finditer returns an iterator of matching objects
# You can use span to get the location

theStr = "The ape was at the apex"

for i in re.finditer("ape.", theStr):
    # Span returns a tuple
    locTuple = i.span()

    print(locTuple)

    # Slice the match out using the tuple values
    print(theStr[locTuple[0]:locTuple[1]])

# ---------- Match 1 of Several Letters ----------

# Square brackets will match any one of the characters between
# the brackets not including upper and lowercase varieties
# unless they are listed

animalStr = "Cat rat mat fat pat"

allAnimals = re.findall("[crmfp]at", animalStr)
for i in allAnimals:
    print(i)

print()

# We can also allow for characters in a range
# Remember to include upper and lowercase letters
someAnimals = re.findall("[c-mC-M]at", animalStr)
for i in someAnimals:
    print(i)

print()

# Use ^ to denote any character but whatever characters are
# between the brackets
someAnimals = re.findall("[^Cr]at", animalStr)
for i in someAnimals:
    print(i)

print()

# ---------- Replace All Matches ----------

# Replace matching items in a string

owlFood = "rat cat mat pat"

# You can compile a regex into pattern objects which
# provide additional methods
regex = re.compile("[cr]at")

# sub() replaces items that match the regex in the string
# with the 1st attribute string passed to sub
owlFood = regex.sub("owl", owlFood)

print(owlFood)

# ---------- Solving Backslash Problems ----------

# Regex use the backslash to designate special characters
# and Python does the same inside strings which causes
# issues.

# Let's try to get "\\stuff" out of a string

randStr = "Here is \\stuff"

# This won't find it
print("Find \\stuff : ", re.search("\\stuff", randStr))

# This does, but we have to put in 4 slashes which is
# messy
print("Find \\stuff : ", re.search("\\\\stuff", randStr))

# You can get around this by using raw strings which
# don't treat backslashes as special
print("Find \\stuff : ", re.search(r"\\stuff", randStr))

# ---------- Matching Any Character ----------
# We saw that . matches any character, but what if we
# want to match a period. Backslash the period
# You do the same with [, ] and others

randStr = "F.B.I. I.R.S. CIA"

print("Matches :", len(re.findall(".\..\..", randStr)))

# ---------- Matching Whitespace ----------
# We can match many whitespace characters

randStr = """This is a long
string that goes
on for many lines"""

print(randStr)

# Remove newlines
regex = re.compile("\n")

randStr = regex.sub(" ", randStr)

print(randStr)

# You can also match
# \b : Backspace
# \f : Form Feed
# \r : Carriage Return
# \t : Tab
# \v : Vertical Tab

# You may need to remove \r\n on Windows

# ---------- Matching Any Single Number ----------
# \d can be used instead of [0-9]
# \D is the same as [^0-9]

randStr = "12345"

print("Matches :", len(re.findall("\d", randStr)))

# ---------- Matching Multiple Numbers ----------
# You can match multiple digits by following the \d with {numOfValues}

# Match 5 numbers only
if re.search("\d{5}", "12345"):
    print("It is a zip code")

# You can also match within a range
# Match values that are between 5 and 7 digits
numStr = "123 12345 123456 1234567"

print("Matches :", len(re.findall("\d{5,7}", numStr)))

# ---------- Matching Any Single Letter or Number ----------
# \w is the same as [a-zA-Z0-9_]
# \W is the same as [^a-zA-Z0-9_]

phNum = "412-555-1212"

# Check if it is a phone number
if re.search("\w{3}-\w{3}-\w{4}", phNum):
    print("It is a phone number")

# Check for valid first name between 2 and 20 characters
if re.search("\w{2,20}", "Ultraman"):
    print("It is a valid name")

# ---------- Matching WhiteSpace ----------
# \s is the same as [\f\n\r\t\v]
# \S is the same as [^\f\n\r\t\v]

# Check for valid first and last name with a space
if re.search("\w{2,20}\s\w{2,20}", "Toshio Muramatsu"):
    print("It is a valid full name")

# ---------- Matching One or More ----------
# + matches 1 or more characters

# Match a followed by 1 or more characters
print("Matches :", len(re.findall("a+", "a as ape bug")))

# ---------- Problem ----------
# Create a Regex that matches email addresses from a list
# 1. 1 to 20 lowercase and uppercase letters, numbers, plus ._%+-
# 2. An @ symbol
# 3. 2 to 20 lowercase and uppercase letters, numbers, plus .-
# 4. A period
# 5. 2 to 3 lowercase and uppercase letters

emailList = "db@aol.com m@.com @apple.com db@.com"

print("Email Matches :", len(re.findall("[\w._%+-]{1,20}@[\w.-]{2,20}.[A-Za-z]{2,3}",
                                        emailList)))
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
116
117
118
119
120
121
122
123
124
125
126
127
128
129
130
131
132
133
134
135
136
137
138
139
140
141
142
143
144
145
146
147
148
149
150
151
152
153
154
155
156
157
158
159
160
161
162
163
164
165
166
167
168
169
170
171
172
173
174
175
176
177
178
179
180
181
182
183
184
185
186
187
188
189
190
191
192
193
194
195
196
197
198
199
200
201
202
203
204
205
206
# Regular expressions allow you to locate and change
# strings in very powerful ways.
# They work in almost exactly the same way in every
# programming language as well.

# Regular Expressions (Regex) are used to
# 1. Search for a specific string in a large amount of data
# 2. Verify that a string has the proper format (Email, Phone #)
# 3. Find a string and replace it with another string
# 4. Format data into the proper form for importing for example

# import the Regex module
import re

# ---------- Was a Match Found ----------

# Search for ape in the string
if re.search("ape", "The ape was at the apex"):
    print("There is an ape")

# ---------- Get All Matches ----------

# findall() returns a list of matches
# . is used to match any 1 character or space
allApes = re.findall("ape.", "The ape was at the apex")

for i in allApes:
    print(i)

# finditer returns an iterator of matching objects
# You can use span to get the location

theStr = "The ape was at the apex"

for i in re.finditer("ape.", theStr):
    # Span returns a tuple
    locTuple = i.span()

    print(locTuple)

    # Slice the match out using the tuple values
    print(theStr[locTuple[0]:locTuple[1]])

# ---------- Match 1 of Several Letters ----------

# Square brackets will match any one of the characters between
# the brackets not including upper and lowercase varieties
# unless they are listed

animalStr = "Cat rat mat fat pat"

allAnimals = re.findall("[crmfp]at", animalStr)
for i in allAnimals:
    print(i)

print()

# We can also allow for characters in a range
# Remember to include upper and lowercase letters
someAnimals = re.findall("[c-mC-M]at", animalStr)
for i in someAnimals:
    print(i)

print()

# Use ^ to denote any character but whatever characters are
# between the brackets
someAnimals = re.findall("[^Cr]at", animalStr)
for i in someAnimals:
    print(i)

print()

# ---------- Replace All Matches ----------

# Replace matching items in a string

owlFood = "rat cat mat pat"

# You can compile a regex into pattern objects which
# provide additional methods
regex = re.compile("[cr]at")

# sub() replaces items that match the regex in the string
# with the 1st attribute string passed to sub
owlFood = regex.sub("owl", owlFood)

print(owlFood)

# ---------- Solving Backslash Problems ----------

# Regex use the backslash to designate special characters
# and Python does the same inside strings which causes
# issues.

# Let's try to get "\\stuff" out of a string

randStr = "Here is \\stuff"

# This won't find it
print("Find \\stuff : ", re.search("\\stuff", randStr))

# This does, but we have to put in 4 slashes which is
# messy
print("Find \\stuff : ", re.search("\\\\stuff", randStr))

# You can get around this by using raw strings which
# don't treat backslashes as special
print("Find \\stuff : ", re.search(r"\\stuff", randStr))

# ---------- Matching Any Character ----------
# We saw that . matches any character, but what if we
# want to match a period. Backslash the period
# You do the same with [, ] and others

randStr = "F.B.I. I.R.S. CIA"

print("Matches :", len(re.findall(".\..\..", randStr)))

# ---------- Matching Whitespace ----------
# We can match many whitespace characters

randStr = """This is a long
string that goes
on for many lines"""

print(randStr)

# Remove newlines
regex = re.compile("\n")

randStr = regex.sub(" ", randStr)

print(randStr)

# You can also match
# \b : Backspace
# \f : Form Feed
# \r : Carriage Return
# \t : Tab
# \v : Vertical Tab

# You may need to remove \r\n on Windows

# ---------- Matching Any Single Number ----------
# \d can be used instead of [0-9]
# \D is the same as [^0-9]

randStr = "12345"

print("Matches :", len(re.findall("\d", randStr)))

# ---------- Matching Multiple Numbers ----------
# You can match multiple digits by following the \d with {numOfValues}

# Match 5 numbers only
if re.search("\d{5}", "12345"):
    print("It is a zip code")

# You can also match within a range
# Match values that are between 5 and 7 digits
numStr = "123 12345 123456 1234567"

print("Matches :", len(re.findall("\d{5,7}", numStr)))

# ---------- Matching Any Single Letter or Number ----------
# \w is the same as [a-zA-Z0-9_]
# \W is the same as [^a-zA-Z0-9_]

phNum = "412-555-1212"

# Check if it is a phone number
if re.search("\w{3}-\w{3}-\w{4}", phNum):
    print("It is a phone number")

# Check for valid first name between 2 and 20 characters
if re.search("\w{2,20}", "Ultraman"):
    print("It is a valid name")

# ---------- Matching WhiteSpace ----------
# \s is the same as [\f\n\r\t\v]
# \S is the same as [^\f\n\r\t\v]

# Check for valid first and last name with a space
if re.search("\w{2,20}\s\w{2,20}", "Toshio Muramatsu"):
    print("It is a valid full name")

# ---------- Matching One or More ----------
# + matches 1 or more characters

# Match a followed by 1 or more characters
print("Matches :", len(re.findall("a+", "a as ape bug")))

# ---------- Problem ----------
# Create a Regex that matches email addresses from a list
# 1. 1 to 20 lowercase and uppercase letters, numbers, plus ._%+-
# 2. An @ symbol
# 3. 2 to 20 lowercase and uppercase letters, numbers, plus .-
# 4. A period
# 5. 2 to 3 lowercase and uppercase letters

emailList = "db@aol.com m@.com @apple.com db@.com"

print("Email Matches :", len(re.findall("[\w._%+-]{1,20}@[\w.-]{2,20}.[A-Za-z]{2,3}",
                                        emailList)))
