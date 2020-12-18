#Python w3 resource strings

#1. Write a Python program to calculate the length of a string.


"""string=str(input("Enter a string: "))
print("The length of the string- '",string,"' including whitespace is ",len(string))"""



"""2.  Write a Python program to count the number of characters (character frequency) in a string. 
Sample String : google.com'
Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}"""


"""string=str(input("Enter a string: "))
frequency={}                            #initializing a dictionary
for i in string:                        #checks for all the characters in the given string
    char = frequency.keys()             # checking the frequency of occurances of the particular character in the given string
    if i in char:
        frequency[i]=frequency[i]+1     # if the character appears more than once
    else:
        frequency[i]=1                  #if the character appears once
print(frequency)                        #prints the dictionary with the characters and the number of times it appears in the given string
    
"""


"""3. Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string.
If the string length is less than 2, return instead of the empty string. 
Sample String : 'w3resource'          Expected Result : 'w3ce'
Sample String : 'w3'                  Expected Result : 'w3w3'
Sample String : ' w'                  Expected Result : Empty String """


"""prompt=str(input("Enter the string: "))
if len(prompt)<2:
    print("Empty string")
else:
    length=len(prompt)
    print(prompt[0:2]+prompt[length-2:length])"""      """prints the 1st 2 characters and the last 2 characters(counting always starts with 0.
                                                        + is added instead of, to concatnate it without spaces"""


"""4. Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$',
except the first char itself.
Sample String : 'restart'
Expected Result : 'resta$t'"""


"""prompt=input("Enter a string: ")
first=prompt[0:1]
prompt1=prompt[1:]
for i in range(1, len(prompt)-1):
        if first==prompt[i]:
            prompt1=prompt1.replace(prompt[i],"$")
print(first+prompt1) """


"""5. Write a Python program to get a single string from two given strings,
separated by a space and swap the first two characters of each string. 
Sample String : 'abc', 'xyz' 
Expected Result : 'xyc abz' """


"""string1=input("Enter 1st string: ")
string2=input("Enter 2nd string: ")
s11=string1[0:2]
s12=string1[2:]
s21=string2[0:2]
s22=string2[2:]
print(s21+s12,s11+s22)"""


"""6. Write a Python program to add 'ing' at the end of a given string (length should be at least 3).
If the given string already ends with 'ing' then add 'ly' instead.
If the string length of the given string is less than 3, leave it unchanged. 
Sample String : 'abc'        Expected Result : 'abcing' 
Sample String : 'string'     Expected Result : 'stringly'
Sample String : 'ab'         Expected Result : 'ab'"""


"""def ing():
    prompt=input("Enter a string: ")
    if len(prompt)<3:
        newstring=prompt
    else:
        if prompt[len(prompt)-3:].upper()=="ING":       # checking if the last 3 characters are "ing"
            newstring=prompt+"ly"
        else:
            newstring=prompt+"ing"
    print(newstring)"""


"""7. Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string,
if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'.
Return the resulting string. 
Sample String : 'The lyrics is not that poor!'
'The lyrics is poor!'
Expected Result : 'The lyrics is good!'
'The lyrics is poor!'   """ 

"""def notpoor():
    prompt=input("Enter a string with not/poor/good: ")
    
        promptnot=prompt.find("not")
        promptpoor=prompt.find("poor")
        if promptnot<promptpoor:
            prompt=prompt.replace(prompt[promptnot:promptpoor+4],"good")
        else:
            prompt=prompt
        print(prompt)
    

       """ #check this later

"""8. Write a Python function that takes a list of words and returns the length of the longest one.  
Sample Output:
Longest word: Exercises
Length of the longest word: 9"""

"""def longest():
    prompt="Y"
    largest=None
    while prompt.upper()=="Y":
        string=input("Enter a string: ")
        if largest is None or len(string)>largest:
            largest=len(string)
            larstring=string
        prompt=input("Do you want to enter more strings?(Y/N): ")
    print("Longest word: ",larstring)
    print("length of the longest word: ",largest)"""


# 9. Write a Python program to remove the nth index character from a nonempty string.

"""def removechar():
    string=input("enter a string: ")
    try:
        index=int(input("enter the index number of the character to be removed:(0 for the first character) "))
        if index>=2:
            string1=string[0:index]
            string2=string[index+1:]
            print(string1+string2)
        elif index==0:
            print(string[1:])
        elif index==1:
            print(string[0:1]+string[2:])
    except:
        print("enter integer")"""

"""10.Write a Python program to change a given string to a new string where the first and last chars have been exchanged."""


"""def firstlastxchange():

    string=input("Enter the string: ")
    length=len(string)
    st1=string[0:1]
    st2=string[length-1:length]
    st3=string[1:length-1]
    print("the new string: ",st2+st3+st1)"""


#11.Write a Python program to remove the characters which have odd index values of a given string


"""string=input("enter the string : ")
newstring=""
length=len(string)
for i in range(0,length,2):
    newstring=newstring+string[i]
print("string with odd index values removed: ",newstring)"""



# 12.Write a Python program to count the occurrences of each word in a given sentence.

"""def wordcount():
    string=input("Enter string: ")
    frequency=dict()
    words=string.split()
    print (words)
    for i in words:
        if i in frequency:
            frequency[i]=frequency[i]+1
        else:
            frequency[i]=1
    print(frequency)"""


#13.Write a Python script that takes input from the user and displays that input back in upper and lower cases.

"""string=input("Enter string: ")
print("the string in upper case- ",string.upper())
print("The string in lower case- ",string.lower())"""

#14. Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form (alphanumerically).




