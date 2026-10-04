#!/usr/bin/env python
# coding: utf-8

# # Strings

# 1. To reverse a string

# In[16]:


text = input("Enter the String: ")

if text.isdigit():
    print("Please enter a string, not a number")
else:
    reverse = text[::-1]
    print(reverse)


# 2. To reverse each word of a given string

# In[57]:


s = input("Enter the String: ")

words = s.split()

for word in words:
    print(word[::-1], end=" ")


# In[24]:


a = input("Enter the string: ")

if a.isdigit():
    print("Please enter string or text next time.")
else:
    words = a.split()
    words.reverse()
    print(" ".join(words))


# 3. To find duplicate characters in a string

# In[26]:


str = input("Enter the String: ")

count = {}

for char in str:
    count[char] = count.get(char, 0) + 1

for char in count:
    if count[char] > 1:
        print(char)


# 4. To count Occurrences of Each Character in String

# In[27]:


str = input("Enter the String: ")

count = {}

for char in str:
    count[char] = count.get(char, 0) + 1

print(count)


# 5. To count the number of words in a string

# In[28]:


str = input("Enter the String: ")

words = str.split()

print("Number of words:", len(words))


# 6. To find all permutations of a given string

# In[29]:


str = input("Enter the String: ")

def permutation(s, answer=""):
    if len(s) == 0:
        print(answer)
        return

    for i in range(len(s)):
        permutation(s[:i] + s[i+1:], answer + s[i])

permutation(str)


# 7. To find if a string is Palindrome

# In[30]:


str = input("Enter the String: ")

str = str.lower()

if str == str[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")


# 8. To determine if Two Strings are Anagrams

# In[31]:


str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

if sorted(str1) == sorted(str2):
    print("Anagrams")
else:
    print("Not Anagrams")


# 9. To Count Vowels and Consonants in a given string

# In[32]:


str = input("Enter the String: ")

vowels = 0
consonants = 0

for char in str.lower():
    if char in "aeiou":
        vowels += 1
    elif char.isalpha():
        consonants += 1

print("Vowels:", vowels)
print("Consonants:", consonants)


# 10. To print unqiue characters

# In[33]:


str = input("Enter the String: ")

for char in str:
    if str.count(char) == 1:
        print(char)


# 11. To print even indexed characters

# In[34]:


str = input("Enter the String: ")

for i in range(0, len(str), 2):
    print(str[i])


# 12. To remove space from a given string

# In[35]:


str = input("Enter the String: ")

str = str.replace(" ", "")

print(str)


# 13. To print each letter twice from a given string

# In[36]:


str = input("Enter the String: ")

for char in str:
    print(char * 2, end="")


# 14. To swap two string without using 3rd variable

# In[37]:


str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

str1, str2 = str2, str1

print("After swapping:")
print("str1:", str1)
print("str2:", str2)


# 15. To gives Output: a2b2c3d2 for the Input String Str = 'aabbcccdd'

# In[38]:


s = input("Enter the String: ")

for char in "abcdefghijklmnopqrstuvwxyz":
    count = s.count(char)

    if count > 0:
        print(char, count, sep="", end="")


# 16. To gives two Output: 'abcde', 'ABCDE' for the Input String Str = 'aBACbcEDed'

# s = input("Enter the String: ")
# 
# lower = ""
# upper = ""
# 
# for char in s:
#     if char.islower():
#         lower += char
#     elif char.isupper():
#         upper += char
# 
# print("".join(sorted(lower)))
# print("".join(sorted(upper)))

# 17. To gives two Output: 'LakshmiMachineLearning', '123' for the Input String Str = 'Lakshmi123Machinelearning'

# In[40]:


s = input("Enter the String: ")

letters = ""
numbers = ""

for char in s:
    if char.isalpha():
        letters += char
    elif char.isdigit():
        numbers += char

print(letters)
print(numbers)


# 18. To gives Output: '32412120000' for the Input String Str = '32400121200'

# In[41]:


s = input("Enter the String: ")

result = ""

for char in s:
    if char != "0":
        result += char

result += "0" * (len(s) - len(result))

print(result)


# 19. To gives Output: '00003241212' for the Input String Str = '32400121200'

# In[42]:


s = input("Enter the String: ")

result = ""

for char in s:
    if char != "0":
        result += char

zeros = len(s) - len(result)

print("0" * zeros + result)


# 20. To find the longest without repeating characters

# In[43]:


s = input("Enter the String: ")

longest = ""

for i in range(len(s)):
    current = ""

    for j in range(i, len(s)):
        if s[j] in current:
            break
        current += s[j]

    if len(current) > len(longest):
        longest = current

print(longest)


# In[ ]:




