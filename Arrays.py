#!/usr/bin/env python
# coding: utf-8

# # Arrays

# 1. To find common elements between two arrays

# In[44]:


a = [1, 2, 3, 4, 5]
b = [3, 4, 5, 6, 7]

common = []

for x in a:
    if x in b:
        common.append(x)

print(common)


# 2. Find first and last element of Arraylist

# In[45]:


arr = [10, 20, 30, 40, 50]

print("First element:", arr[0])
print("Last element:", arr[-1])


# 3. Sort an array without using in-built method

# In[46]:


arr = [5, 2, 8, 1, 3]

for i in range(len(arr)):
    for j in range(0, len(arr) - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print(arr)


# 4. Remove Duplicates from an Array

# In[47]:


arr = [1, 2, 2, 3, 4, 4, 5]

result = []

for x in arr:
    if x not in result:
        result.append(x)

print(result)


# 5. Remove duplicates from an ArrayList

# In[48]:


arr = [1, 2, 2, 3, 4, 4, 5]

result = []

for x in arr:
    if x not in result:
        result.append(x)

print(result)


# 6. Find the missing number in an Array

# In[49]:


arr = [1, 2, 3, 5, 6]

n = len(arr) + 1

total = n * (n + 1) // 2
sum_arr = sum(arr)

missing = total - sum_arr

print("Missing number:", missing)


# 7. Find the largest and smallest element in an Array

# In[50]:


arr = [10, 5, 20, 3, 15]

largest = arr[0]
smallest = arr[0]

for x in arr:
    if x > largest:
        largest = x

    if x < smallest:
        smallest = x

print("Largest:", largest)
print("Smallest:", smallest)


# In[51]:


arr = [10, 20, 30, 40, 50]

x = int(input("Enter element to search: "))

found = False

for i in range(len(arr)):
    if arr[i] == x:
        print("Element found at index:", i)
        found = True
        break

if not found:
    print("Element not found")


# 9. Array consists of integers and special characters,sum only integers

# In[52]:


arr = [10, '@', 20, '#', 30, '$']

total = 0

for x in arr:
    if isinstance(x, int):
        total += x

print("Sum:", total)


# 10. Find Minimum and Maximum from an Array

# In[53]:


arr = [10, 5, 20, 3, 15]

minimum = arr[0]
maximum = arr[0]

for x in arr:
    if x < minimum:
        minimum = x

    if x > maximum:
        maximum = x

print("Minimum:", minimum)
print("Maximum:", maximum)


# 11. To count Odd and Even number from given array

# In[54]:


arr = [1, 2, 3, 4, 5, 6, 7]

odd = 0
even = 0

for x in arr:
    if x % 2 == 0:
        even += 1
    else:
        odd += 1

print("Odd numbers:", odd)
print("Even numbers:", even)


# 12. input array was given [ 1,1,2,2,3,4,5,5,6,6], Output – [3,4]

# In[55]:


arr = [1, 1, 2, 2, 3, 4, 5, 5, 6, 6]

result = []

for x in arr:
    if arr.count(x) == 1:
        result.append(x)

print(result)


# 13. to implement hashcode and equals

# In[56]:


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

    def __hash__(self):
        return hash((self.name, self.age))


s1 = Student("John", 20)
s2 = Student("John", 20)

print(s1 == s2)
print(hash(s1) == hash(s2))


# In[ ]:




