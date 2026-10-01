#!/usr/bin/env python
# coding: utf-8

# Python-interview-programs

# Numbers

# 1. Program to Find Odd or Even number

# In[10]:


x = int(input("Enter the number: "))

if x % 2 == 0:
    print("The given number is even.")
else:
    print("The given number is odd.")


# In[11]:


x = int(input("Enter the number: "))

if x % 2 == 0:
    print("The given number is even.")
else:
    print("The given number is odd.")


# In[12]:


x = int(input("Enter the number: "))

if x % 2 == 0:
    print("The given number is even.")
else:
    print("The given number is odd.")


# 2. Program to find Prime number

# In[13]:


x = int(input("Enter the number: "))

if x <= 1:
    print("The given number is not prime")
else:
    for i in range(2, x):
        if x % i == 0:
            print("The given number is not prime")
            break
    else:
        print("The given number is prime")


# In[14]:


x = int(input("Enter the number: "))

if x <= 1:
    print("The given number is not prime")
else:
    for i in range(2, x):
        if x % i == 0:
            print("The given number is not prime")
            break
    else:
        print("The given number is prime")


# In[15]:


x = int(input("Enter the number: "))

if x <= 1:
    print("The given number is not prime")
else:
    for i in range(2, x):
        if x % i == 0:
            print("The given number is not prime")
            break
    else:
        print("The given number is prime")


# 3. Program to find Fibonacci series upto a given number range

# In[16]:


x = int(input("Enter the range: "))

a = 0
b = 1

while a <= x:
    print(a)
    c = a + b
    a = b
    b = c


# In[17]:


x = int(input("Enter the range: "))

a = 0
b = 1

while a <= x:
    print(a)
    c = a + b
    a = b
    b = c


# 4. To swap two numbers without using third variable

# In[18]:


x = 10 
y = 20
x,y = y,x
print(x,y)


# 5. To find Factorial on given Number

# In[20]:


n = int(input("Enter the number: "))

a = 1

for i in range(1, n + 1):
    a = a * i

print(a)


# 6. To Reverse Number

# In[21]:


n = (input("Enter the number: "))

reverse = int(n[::-1])

print(reverse)


# 7. To find Armstrong Number

# In[22]:


n = int(input("Enter the number: "))

original = n
total = 0

while n > 0:
    a = n % 10
    total = total + a**3
    n = n // 10

if total == original:
    print("The given number is an Armstrong number")
else:
    print("The given number is not an Armstrong number")


# 8. To find number of digits in given number

# In[23]:


n = int(input("Enter the number: "))

count = 0

while n != 0:
    n = n // 10
    count = count + 1

print("Number of digits:", count)


# 9. To find Palindrome number

# In[24]:


n = int(input("Enter the number: "))

original = n
reverse = int(str(n)[::-1])

if original == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")


# 10. To calculate the sum of digits of a number

# In[29]:


a = input("Enter the number: ")

sum_of_numbers = 0

for i in a:
    sum_of_numbers = sum_of_numbers + int(i)

print("Sum of digits:", sum_of_numbers)


# In[ ]:




