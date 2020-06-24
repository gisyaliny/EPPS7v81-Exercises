#!/usr/bin/env python
# coding: utf-8

# # Variable Types in Python
# * 4.1.1 [Variable types](#411)
# * 4.1.2 [Playing around with Variables](#412)
# * 4.2.2 [Comparing things](#422)
# * 4.3 [Flow control](#43)

# ## 4.1.1 Variable Types -1 <a id = '411'> </a>
# * Check every line for bugs

# **Original**

# In[1]:


# an integer is a "whole number" (i.e. one with no decimal point)
my_integer: int= 12
    my_integer


# **Modified**

# In[2]:


my_integer: int= 12
my_integer


# **Original**

# In[3]:


#a float is a numerical value with a decimal point
my_float = 12.1
#a string is text
my_string = "This is my string."
#You can check the data type of variables using the "type" method
 type(my_string)


# **Modified**

# In[4]:


#a float is a numerical value with a decimal point
my_float = 12.1
#a string is text**Modified****Modified**
my_string = "This is my string."
#You can check the data type of variables using the "type" method
type(my_string)


# **QUESTION 1: What type of variables do you think the following five are? DON'T use `type()` until you've had a guess.**

# In[5]:


var1 = "14" #str

var2 = 14 + 14 #int

var3 = 14 + 14.2 #float

var4 = "14 + 14.2" #str

var5 = 14.2 - 0.2 #float


# There are WAY more variable types than these integers, floats and strings are the three data types Python uses, but variables don't have to be used to store just data types they can store all sorts of more complex data #structures (i.e. things that collect bits of data together) like lists ordictionaries. But that's for later! 

# In[6]:


my_list = [var1, var2, var3, var4, var5]
for ele in my_list:
    print(type(ele),end= ' ')


# **QUESTION2: What do you think you will see if you use type() on my_list and my_dict? Have a guess and see if you're right.**

# In[7]:


my_dict = {"First Variable": var1, "Second Variable": var2, "Third Variable": var3, "Fourth Variable": var4, "Fifth Variable": var5}
print('List:',type(my_list))
print('Dict:',type(my_dict))


# ---

# ## 4.1.2 Playing around with Variables <a id ='412'> </a>
# * Check every line for bugs
# * Answer the questions for each block
# 

# Variables can be reassigned and overwritten:   
# Can you guess the value of new_var?  

# In[8]:


original_var = 30
new_var = original_var + 20  #50
new_var


# Can you guess the value of original_var2?

# In[9]:


original_var2 = 10
original_var2 = original_var2 + 10 #20
original_var2


# Can you guess what string1 will contain?   
# Notice the space at the beginning of the reassigned string1 below: why is that threre

# **Original**

# In[10]:


string1 = "This is the first part of the string."
string1 = string1 + " This is the second part of the string."
String1 # case sensitive


# **Modified**

# In[11]:


string1 = "This is the first part of the string."
string1 = string1 + " This is the second part of the string."
string1


# Try adding these two variables together, and explain what happens.

# In[12]:


first_bit = 14
second_bit = "14"
first_bit + second_bit # could not add one numeric type with a string


# **We can also convert variable types to different variable types, as follows:**   
#    
# To 'stringify' something, we can use str(VARIABLE). Below, I'll declare a variable which is an integer, then I'll use str(VARIABLE) to write the 'stringified' version to a new variable.

# **Original**

# In[13]:


my_integer_variable = 30
my_stringified_variable = st(my_integer_variable)


# **Modified**

# In[14]:


my_integer_variable = 30
my_stringified_variable = str(my_integer_variable)
my_stringified_variable


# To 'integerify' something, we can use int(VARIABLE). Below, I'll declare a variable which is a number written out as a string, then I'll use int(VARIABLE) to write the 'integerified' version to a new variable.

# **Original**

# In[15]:


my_string_variable = "30"
my_integerified_variable = in(my_string_variable)


# **Modified**

# In[16]:


my_string_variable = "30"
my_integerified_variable = int(my_string_variable)
my_integerified_variable


# To 'floatify' an integer, we can use float(VARIABLE). Below, I'll declare an integer variable, then I'll use float(VARIABLE) to write the 'floatified' version to a new variable. Try this for yourself in the shell.

# In[17]:


my_integer_variable = 30
my_floatified_variable = float(my_integer_variable)
my_floatified_variable


# **NOTE:** one way to convert an integer to a float is to just add 0.0 to it, as you can see below. Try this out in the shell:

# **Original**

# In[18]:


my_integer_variable = 30.O
my_floatified_variable = my_integer_variable + 0.0
type(my_floatified_variable)


# **Modified**

# In[19]:


my_integer_variable = 30.0
my_floatified_variable = my_integer_variable + 0.0
type(my_floatified_variable)


# Because a float is just an integer with a decimal (i.e. `floating`) point, all we have to do to `floatify` an integer is give it a decimal, even if that decimal has no numerical value. However, can you see a problem with this?   
# What if you want to 'floatify' a string by adding 0.0 to it? It makes no sense to add a decimal point to a string in this way, and that will cause an error.   
# * Try this in the shell: >>> `my_string_variable = "30" + 0.0   `    
# * Now try this: >>> `float(my_string_variable) `   
# Hence, using float(VARIABLE) is a better way to handle variable type conversions as a general rule.

# ## 4.2.2 Comparing things <a id = '422'> </a>
# * Check every line for bugs
# * Answer the questions for each block
# * Try Reformat file

# It often helps for us to be able to compare things in Python, to see if a variable matches some criteria that we establish, etc (see other word doc
# on social science applications for more detail). This becomes especially powerful when we combine it with things like IF, ELIF and ELSE statements
# (which we will do later), but for now, here are a list of ways in which we can compare things in Python. I have declared three variables below -
# try typing the comparisons I've listed into the Python shell and see what happens.

# In[20]:


a = 2
b = 3
c = 4


# In[21]:


a == b #The double-equals signifies an "is the same as" comparison.


# In[22]:


a != b #This signifies a "not the same as" comparison


# In[23]:


b > a #"is greater than"


# In[24]:


b >= a  # "is greater than or equal to"


# In[25]:


b < a  # "is less than"


# So here, the value that will be given when you type this into the Python shell will be the remainder that is left over when c is divided by a. The modulo is more of a calculation than a comparator, but it's mainly only relevant to us as a way of comparing things.

# In[26]:


c % a # This is called the "modulo", which effectively means the remainder.


# **QUESTION: You can also do calculations within comparisons. Can you guess what will result in the following cases? Have a guess, then type them into the Python shell to check.**   
# Add answer to each with quote

# In[27]:


a + 1 == b # True


# In[28]:


c - 1 >= b # True


# In[29]:


c / 4 > a # False


# In[30]:


a * 2 == c # True


# In[31]:


c % a == 0 # True


# ## 4.3 Flow control (and white space) <a id = '43'> </a>
# * Check every line for bugs
# * Answer the questions for each block

# Now we can compare things, we can get into more sophisticated stuff. Here is a script that takes a variable ("number") and runs various checks on it. If the number is evenly divisible by three (i.e. with no remainder), the code prints the string "Fizz". If the number is evenly divisible by five, the code prints the string "Buzz". If a number is evenly divisible by both three and five, the code prints "FizzBuzz".
# * First, run the script - what happens? Is that expected?

# In[32]:


number = 1

if number % 5 == 0 and number % 3 == 0:
    print("FizzBuzz")
elif number % 3 == 0:
    print("Fizz")
elif number % 5 == 0:
    print("Buzz")
else:
    print(number)


# * Second, change the value of the variable "number" in line 14 to the following values:
#     * 3, 98, 75, 55, 45, 29853    
# What happens? Is that expected?

# In[33]:


num_lst = [3,98,75,55,45,29853]
for number in num_lst:
    print(number,end= ': ')
    if number % 5 == 0 and number % 3 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)


# **Try this exercise and provide answer in comments**
# EXERCISE: Create a program which produces statements about numbers that you give it, with the following conditions:
# * if the number is over 100 print "Phew, that's a big number."
# * if the number is even, print "This one is even."
# * if the number is even and over 100 print "Stop. I can't even."
# * if the number doesn't satisfy any of these conditions, print the number.   
# 
# _This program can be written at the bottom of this script._

# In[34]:


num_lst = [3,98,102,55,45,29853]
for number in num_lst:
    print(number,end= ': ')
    if number % 2 == 0 and number > 100:
        print("Stop. I can't even")
    elif number > 100:
        print("Phew, that's a big number.")
    elif number % 2 == 0:
        print("This one is even.")
    else:
        print(number)

